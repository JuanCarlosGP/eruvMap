import exifr from 'exifr'

export interface PhotoLocationResult {
  lat: number
  lng: number
  source: 'exif' | 'browser'
}

export async function readPhotoGps(
  file: File,
): Promise<{ lat: number; lng: number } | null> {
  try {
    const gps = await exifr.gps(file)
    if (gps?.latitude != null && gps?.longitude != null) {
      return { lat: gps.latitude, lng: gps.longitude }
    }
  } catch {
    /* ignore */
  }
  return null
}

export function readBrowserLocation(): Promise<PhotoLocationResult> {
  return new Promise((resolve, reject) => {
    if (!navigator.geolocation) {
      reject(new Error('unsupported'))
      return
    }
    navigator.geolocation.getCurrentPosition(
      (pos) => {
        resolve({
          lat: pos.coords.latitude,
          lng: pos.coords.longitude,
          source: 'browser',
        })
      },
      () => reject(new Error('denied')),
      { enableHighAccuracy: true, timeout: 15000 },
    )
  })
}
