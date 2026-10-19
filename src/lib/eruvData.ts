import type { Locale } from '../i18n/translations'
import type { EruvCollection, EruvFeature, EruvProperties } from '../types/eruv'
import type { Feature, FeatureCollection, Point, Position } from 'geojson'

export function isPartialPerimeter(note?: string | null): boolean {
  return Boolean(note && /partial/i.test(note))
}

export function eruvDisplayName(
  props: EruvProperties,
  locale: Locale,
): string {
  if (locale === 'he' && props.name_he) return props.name_he
  return props.name_en
}

export function normalizeFeatures(collection: EruvCollection): EruvFeature[] {
  return collection.features.map((f, index) => {
    const props = f.properties
    const id = String(props?.id ?? f.id ?? `feature-${index}`)
    return {
      ...f,
      id,
      properties: {
        ...props,
        id,
        is_partial:
          props.geometry_kind === 'perimeter' &&
          isPartialPerimeter(props.note ?? null),
      },
    }
  }) as EruvFeature[]
}

export function perimeterFeatures(
  features: EruvFeature[],
): FeatureCollection {
  const out: EruvFeature[] = []
  for (const f of features) {
    if (f.properties.geometry_kind !== 'perimeter') continue
    out.push({
      ...f,
      properties: {
        ...f.properties,
        eruv_id: String(f.id),
      } as EruvProperties & { eruv_id: string },
    })
    if (
      f.geometry.type === 'Polygon' &&
      f.properties.is_partial
    ) {
      out.push({
        type: 'Feature',
        id: `${f.id}__outline`,
        properties: {
          ...f.properties,
          eruv_id: String(f.id),
        } as EruvProperties & { eruv_id: string },
        geometry: {
          type: 'LineString',
          coordinates: f.geometry.coordinates[0],
        },
      })
    }
  }
  return { type: 'FeatureCollection', features: out }
}

function ringWithoutClose(ring: Position[]): Position[] {
  if (ring.length < 2) return ring
  const first = ring[0]
  const last = ring[ring.length - 1]
  if (first[0] === last[0] && first[1] === last[1]) return ring.slice(0, -1)
  return ring
}

function pointInRing(lon: number, lat: number, ring: Position[]): boolean {
  let inside = false
  for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
    const xi = ring[i][0]
    const yi = ring[i][1]
    const xj = ring[j][0]
    const yj = ring[j][1]
    const crosses = (yi > lat) !== (yj > lat)
    if (!crosses) continue
    const xAtLat = ((xj - xi) * (lat - yi)) / (yj - yi) + xi
    if (lon < xAtLat) inside = !inside
  }
  return inside
}

function pointInPolygon(lon: number, lat: number, rings: Position[][]): boolean {
  if (!pointInRing(lon, lat, rings[0])) return false
  for (let hole = 1; hole < rings.length; hole++) {
    if (pointInRing(lon, lat, rings[hole])) return false
  }
  return true
}

function ringAbsArea(ring: Position[]): number {
  const open = ringWithoutClose(ring)
  let sum = 0
  for (let i = 0; i < open.length; i++) {
    const next = open[(i + 1) % open.length]
    sum += open[i][0] * next[1] - next[0] * open[i][1]
  }
  return Math.abs(sum / 2)
}

function interiorOfPolygon(rings: Position[][]): [number, number] {
  const outer = ringWithoutClose(rings[0])
  if (outer.length === 0) return [0, 0]
  const candidates: [number, number][] = []
  let sx = 0
  let sy = 0
  for (const [lon, lat] of outer) {
    sx += lon
    sy += lat
  }
  candidates.push([sx / outer.length, sy / outer.length])
  for (let i = 0; i < outer.length; i++) {
    const a = outer[i]
    const b = outer[(i + 1) % outer.length]
    const c = outer[(i + 2) % outer.length]
    candidates.push([(a[0] + b[0] + c[0]) / 3, (a[1] + b[1] + c[1]) / 3])
  }
  for (const [lon, lat] of candidates) {
    if (pointInPolygon(lon, lat, rings)) return [lon, lat]
  }
  return [outer[0][0], outer[0][1]]
}

function markerCoordinate(feature: EruvFeature): [number, number] | null {
  const geometry = feature.geometry
  if (geometry.type === 'Point') {
    return [geometry.coordinates[0], geometry.coordinates[1]]
  }
  if (geometry.type === 'Polygon') {
    return interiorOfPolygon(geometry.coordinates)
  }
  if (geometry.type === 'MultiPolygon') {
    let best = geometry.coordinates[0]
    let bestArea = -1
    for (const polygon of geometry.coordinates) {
      const area = ringAbsArea(polygon[0])
      if (area > bestArea) {
        best = polygon
        bestArea = area
      }
    }
    return best ? interiorOfPolygon(best) : null
  }
  if (geometry.type === 'LineString') {
    const mid = geometry.coordinates[Math.floor(geometry.coordinates.length / 2)]
    return mid ? [mid[0], mid[1]] : null
  }
  if (geometry.type === 'MultiLineString') {
    const line = geometry.coordinates[0]
    const mid = line?.[Math.floor(line.length / 2)]
    return mid ? [mid[0], mid[1]] : null
  }
  return null
}

export function pointMapFeatures(features: EruvFeature[]): Feature<Point>[] {
  const points: Feature<Point>[] = []
  for (const feature of features) {
    const coordinate = markerCoordinate(feature)
    if (!coordinate) continue
    points.push({
      type: 'Feature',
      id: feature.id,
      properties: {
        ...feature.properties,
        eruv_id: String(feature.id),
      },
      geometry: { type: 'Point', coordinates: coordinate },
    })
  }
  return points
}
