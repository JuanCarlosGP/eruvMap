import type { EruvFeature } from '../types/eruv'
import type { Feature, Geometry } from 'geojson'

export function featureCentroid(feature: EruvFeature): [number, number] {
  const { geometry } = feature
  if (geometry.type === 'Point') {
    return [geometry.coordinates[0], geometry.coordinates[1]]
  }
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
  if (geometry.type === 'MultiLineString') {
    const line = geometry.coordinates[0]
    const mid = line[Math.floor(line.length / 2)] ?? line[0]
    return [mid[0], mid[1]]
  }
  const coords = geometry.coordinates
  const mid = Math.floor(coords.length / 2)
  const c = coords[mid] ?? coords[0]
  return [c[0], c[1]]
}

export function featureCenterForMap(feature: EruvFeature): [number, number] {
  return featureCentroid(feature)
}

/** Zoom level for flying to an eruv from the sources list or search. */
export function flyZoomForFeature(feature: EruvFeature): number {
  const { geometry_kind, geometry_precision } = feature.properties
  if (geometry_kind === 'point') {
    return geometry_precision === 'approximate' ? 12 : 13
  }
  if (feature.geometry.type === 'Polygon') return 11
  return 12
}

export function geometryCenter(
  feature: Feature<Geometry> | { geometry: Geometry },
): [number, number] {
  const g = feature.geometry
  if (g.type === 'Point') {
    return [g.coordinates[0], g.coordinates[1]]
  }
  if (g.type === 'Polygon') {
    const ring = g.coordinates[0]
    const n = Math.max(ring.length - 1, 1)
    let lng = 0
    let lat = 0
    for (let i = 0; i < n; i++) {
      lng += ring[i][0]
      lat += ring[i][1]
    }
    return [lng / n, lat / n]
  }
  if (g.type === 'MultiLineString') {
    const line = g.coordinates[0]
    const mid = line[Math.floor(line.length / 2)] ?? line[0]
    return [mid[0], mid[1]]
  }
  if (g.type === 'LineString') {
    const mid = g.coordinates[Math.floor(g.coordinates.length / 2)]
    return [mid[0], mid[1]]
  }
  return [0, 0]
}
