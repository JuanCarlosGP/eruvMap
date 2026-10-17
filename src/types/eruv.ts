import type {
  Feature,
  FeatureCollection,
  LineString,
  MultiLineString,
  Point,
  Polygon,
} from 'geojson'

export type GeometryKind = 'perimeter' | 'point'
export type EruvStatus = 'active' | 'unknown'
export type GeometryPrecision = 'exact' | 'approximate'

export interface EruvProperties {
  id: string
  name_en: string
  name_he?: string | null
  city: string
  country: string
  geometry_kind: GeometryKind
  status: EruvStatus
  source: string
  source_url: string
  license: string
  verified_at: string
  contact_url?: string | null
  geometry_precision: GeometryPrecision
  note?: string | null
  osm_id?: string
  coordinate_source?: string
  /** Derivado en carga: nota indica perímetro parcial */
  is_partial?: boolean
}

export type EruvGeometry =
  | Point
  | LineString
  | Polygon
  | MultiLineString

export type EruvFeature = Feature<EruvGeometry, EruvProperties> & {
  id: string
}

export type EruvCollection = FeatureCollection<EruvGeometry, EruvProperties>

export type EruvStatusFilter = EruvStatus | 'all'
