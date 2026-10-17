import type { EruvFeature } from '../types/eruv'
import type { Feature, Point } from 'geojson'

export function featureCentroid(feature: EruvFeature): [number, number] {
  const { geometry } = feature
  if (geometry.type === 'Polygon') {
    const ring = geometry.coordinates[0]
    const n = Math.max(ring.length - 1, 1)
    let lng = 0
    let lat = 0
    for (let i = 0; i < n; i++) {
      lng += ring[i][0]
      lat += ring[i][1]
    }
    return [lng / n, lat / n]
  }
  const coords = geometry.coordinates
  const mid = Math.floor(coords.length / 2)
  const c = coords[mid] ?? coords[0]
  return [c[0], c[1]]
}

export function toCentroidFeatures(
  features: EruvFeature[],
): Feature<Point>[] {
  return features.map((f) => ({
    type: 'Feature',
    id: f.id,
    properties: { ...f.properties, eruv_id: String(f.id) },
    geometry: {
      type: 'Point',
      coordinates: featureCentroid(f),
    },
  }))
}
