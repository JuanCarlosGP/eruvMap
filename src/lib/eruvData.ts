import type { Locale } from '../i18n/translations'
import type { EruvCollection, EruvFeature, EruvProperties } from '../types/eruv'
import type { Feature, FeatureCollection, Point } from 'geojson'

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

export function pointMapFeatures(features: EruvFeature[]): Feature<Point>[] {
  return features
    .filter((f) => f.properties.geometry_kind === 'point')
    .map((f) => ({
      type: 'Feature',
      id: f.id,
      properties: {
        ...f.properties,
        eruv_id: String(f.id),
      },
      geometry: f.geometry as Point,
    }))
}
