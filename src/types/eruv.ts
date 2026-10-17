import type { Feature, FeatureCollection, LineString, Polygon } from 'geojson'

export type TipoGeometria = 'linea' | 'poligono'
export type EruvEstado = 'activo' | 'desconocido'

export interface EruvProperties {
  nombre: string
  ciudad: string
  pais: string
  pais_nombre: string
  tipo_geometria: TipoGeometria
  estado: EruvEstado
  fuente: string
  fecha_verificacion: string | null
  contacto_url: string | null
  es_ejemplo: boolean
  notas?: string
}

export type EruvFeature = Feature<Polygon | LineString, EruvProperties> & {
  id: string
}

export type EruvCollection = FeatureCollection<Polygon | LineString, EruvProperties>

export type EruvEstadoFilter = EruvEstado | 'all'
