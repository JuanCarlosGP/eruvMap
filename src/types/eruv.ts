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
  /** US state / territory code (e.g. NY, CA) */
  state?: string | null
  official_boundary_map?: string | null
  boundary_map_url?: string | null
  stated_terms?: string | null
  hotline_or_contact?: string | null
  status_as_of?: string | null
  evidence?: string | null
  extra_note?: string | null
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
