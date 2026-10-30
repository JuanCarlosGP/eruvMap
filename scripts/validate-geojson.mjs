#!/usr/bin/env node
/**
 * Valida data/eruvs.geojson contra el esquema de propiedades de eruvMap.
 * Uso: npm run validate:geojson
 */
import { readFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { dirname, join } from 'node:path'

const __dirname = dirname(fileURLToPath(import.meta.url))
const GEOJSON_PATH = join(__dirname, '..', 'data', 'eruvs.geojson')

const REQUIRED_PROPS = [
  'id',
  'name_en',
  'city',
  'country',
  'geometry_kind',
  'status',
  'source',
  'source_url',
  'license',
  'verified_at',
  'geometry_precision',
]

const GEOMETRY_KIND = new Set(['perimeter', 'point'])
const STATUS = new Set(['active', 'unknown'])
const PRECISION = new Set(['exact', 'approximate'])

const OPTIONAL_STRING_PROPS = [
  'name_he',
  'contact_url',
  'note',
  'osm_id',
  'coordinate_source',
  'state',
  'official_boundary_map',
  'boundary_map_url',
  'stated_terms',
  'hotline_or_contact',
  'status_as_of',
  'evidence',
  'extra_note',
  'boundary_basis',
]

const PERIMETER_GEOMS = new Set(['Polygon', 'LineString', 'MultiLineString'])
const POINT_GEOMS = new Set(['Point'])

function fail(message) {
  console.error(`❌ ${message}`)
  process.exit(1)
}

let raw
try {
  raw = readFileSync(GEOJSON_PATH, 'utf8')
} catch {
  fail(`No se pudo leer ${GEOJSON_PATH}`)
}

let data
try {
  data = JSON.parse(raw)
} catch (e) {
  fail(`JSON inválido: ${e.message}`)
}

if (data.type !== 'FeatureCollection') {
  fail('La raíz debe ser type: "FeatureCollection"')
}

if (!Array.isArray(data.features) || data.features.length === 0) {
  fail('features debe ser un array no vacío')
}

const ids = new Set()

for (const [index, feature] of data.features.entries()) {
  const prefix = `features[${index}]`
  const props = feature.properties

  if (feature.type !== 'Feature') {
    fail(`${prefix}: type debe ser "Feature"`)
  }

  const id = props?.id ?? feature.id
  if (id == null || String(id).trim() === '') {
    fail(`${prefix}: falta properties.id`)
  }
  const idStr = String(id)
  if (ids.has(idStr)) {
    fail(`id duplicado: ${idStr}`)
  }
  ids.add(idStr)

  if (!feature.geometry?.type) {
    fail(`${prefix} (${idStr}): geometry requerida`)
  }

  if (!props || typeof props !== 'object') {
    fail(`${prefix} (${idStr}): properties requeridas`)
  }

  if (props.id !== idStr) {
    fail(`${prefix} (${idStr}): properties.id debe coincidir con el id de la feature`)
  }

  for (const key of REQUIRED_PROPS) {
    if (!(key in props)) {
      fail(`${prefix} (${idStr}): falta properties.${key}`)
    }
  }

  if (typeof props.name_en !== 'string' || !props.name_en.trim()) {
    fail(`${prefix} (${idStr}): name_en debe ser string no vacío`)
  }

  if (
    props.name_he != null &&
    props.name_he !== undefined &&
    typeof props.name_he !== 'string'
  ) {
    fail(`${prefix} (${idStr}): name_he debe ser string o omitido`)
  }

  if (!GEOMETRY_KIND.has(props.geometry_kind)) {
    fail(`${prefix} (${idStr}): geometry_kind debe ser "perimeter" o "point"`)
  }

  if (!STATUS.has(props.status)) {
    fail(`${prefix} (${idStr}): status debe ser "active" o "unknown"`)
  }

  if (!PRECISION.has(props.geometry_precision)) {
    fail(
      `${prefix} (${idStr}): geometry_precision debe ser "exact" o "approximate"`,
    )
  }

  if (typeof props.verified_at !== 'string' || !props.verified_at.trim()) {
    fail(`${prefix} (${idStr}): verified_at debe ser string ISO`)
  }

  if (typeof props.source_url !== 'string' || !props.source_url.trim()) {
    fail(`${prefix} (${idStr}): source_url debe ser URL string`)
  }

  if (
    props.contact_url != null &&
    props.contact_url !== undefined &&
    typeof props.contact_url !== 'string'
  ) {
    fail(`${prefix} (${idStr}): contact_url debe ser string URL o null`)
  }

  for (const key of OPTIONAL_STRING_PROPS) {
    if (!(key in props) || props[key] == null) continue
    if (typeof props[key] !== 'string') {
      fail(`${prefix} (${idStr}): ${key} debe ser string u omitido`)
    }
  }

  if (props.state != null && props.state !== undefined) {
    if (props.country !== 'US') {
      fail(`${prefix} (${idStr}): state solo aplica cuando country es "US"`)
    }
    if (!/^[A-Z]{2}$/.test(props.state)) {
      fail(`${prefix} (${idStr}): state debe ser código US de 2 letras (p. ej. NY)`)
    }
  }

  if (props.geometry_kind === 'point') {
    if (!POINT_GEOMS.has(feature.geometry.type)) {
      fail(`${prefix} (${idStr}): geometry_kind point requiere geometry Point`)
    }
    if (props.geometry_precision !== 'approximate') {
      fail(
        `${prefix} (${idStr}): los puntos deben usar geometry_precision "approximate"`,
      )
    }
  } else if (!PERIMETER_GEOMS.has(feature.geometry.type)) {
    fail(
      `${prefix} (${idStr}): geometry_kind perimeter requiere Polygon, LineString o MultiLineString`,
    )
  }


  if ('boundary_verified' in props && props.boundary_verified != null) {
    if (typeof props.boundary_verified !== 'boolean') {
      fail(`${prefix} (${idStr}): boundary_verified debe ser boolean`)
    }
  }

  const BOUNDARY_BASIS = new Set([
    'municipal_osm',
    'admin_osm',
    'neighborhood_osm',
    'residential_osm',
    'unverified',
  ])
  if ('boundary_basis' in props && props.boundary_basis != null) {
    if (!BOUNDARY_BASIS.has(props.boundary_basis)) {
      fail(`${prefix} (${idStr}): boundary_basis valor no permitido`)
    }
    if (props.boundary_verified !== false) {
      fail(`${prefix} (${idStr}): boundary_basis solo aplica cuando boundary_verified es false`)
    }
  }

  if ('es_ejemplo' in props) {
    fail(`${prefix} (${idStr}): el campo es_ejemplo ya no forma parte del esquema`)
  }
}

console.log(
  `✅ GeoJSON válido: ${data.features.length} feature(s), ${ids.size} id(s) únicos`,
)
