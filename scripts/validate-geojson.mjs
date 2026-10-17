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
  'nombre',
  'ciudad',
  'pais',
  'pais_nombre',
  'tipo_geometria',
  'estado',
  'fuente',
  'fecha_verificacion',
  'contacto_url',
  'es_ejemplo',
]

const TIPO_GEOMETRIA = new Set(['linea', 'poligono'])
const ESTADO = new Set(['activo', 'desconocido'])
const GEOM_BY_TIPO = {
  linea: 'LineString',
  poligono: 'Polygon',
}

function fail(message) {
  console.error(`❌ ${message}`)
  process.exit(1)
}

function warn(message) {
  console.warn(`⚠️  ${message}`)
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

  if (feature.type !== 'Feature') {
    fail(`${prefix}: type debe ser "Feature"`)
  }

  const id = feature.id ?? feature.properties?.id
  if (id == null || String(id).trim() === '') {
    fail(`${prefix}: falta id en la feature`)
  }
  const idStr = String(id)
  if (ids.has(idStr)) {
    fail(`id duplicado: ${idStr}`)
  }
  ids.add(idStr)

  if (!feature.geometry || !feature.geometry.type) {
    fail(`${prefix} (${idStr}): geometry requerida`)
  }

  const props = feature.properties
  if (!props || typeof props !== 'object') {
    fail(`${prefix} (${idStr}): properties requeridas`)
  }

  for (const key of REQUIRED_PROPS) {
    if (!(key in props)) {
      fail(`${prefix} (${idStr}): falta properties.${key}`)
    }
  }

  if (!TIPO_GEOMETRIA.has(props.tipo_geometria)) {
    fail(
      `${prefix} (${idStr}): tipo_geometria debe ser "linea" o "poligono"`,
    )
  }

  const expectedGeom = GEOM_BY_TIPO[props.tipo_geometria]
  if (feature.geometry.type !== expectedGeom) {
    fail(
      `${prefix} (${idStr}): geometry.type debe ser ${expectedGeom} (tipo_geometria=${props.tipo_geometria})`,
    )
  }

  if (!ESTADO.has(props.estado)) {
    fail(`${prefix} (${idStr}): estado debe ser "activo" o "desconocido"`)
  }

  if (typeof props.es_ejemplo !== 'boolean') {
    fail(`${prefix} (${idStr}): es_ejemplo debe ser boolean`)
  }

  if (
    props.fecha_verificacion !== null &&
    typeof props.fecha_verificacion !== 'string'
  ) {
    fail(`${prefix} (${idStr}): fecha_verificacion debe ser string ISO o null`)
  }

  if (
    props.contacto_url !== null &&
    typeof props.contacto_url !== 'string'
  ) {
    fail(`${prefix} (${idStr}): contacto_url debe ser string URL o null`)
  }

  if (props.es_ejemplo !== true) {
    warn(
      `${idStr}: es_ejemplo no es true — confirma que los datos están verificados antes de publicar`,
    )
  }
}

console.log(
  `✅ GeoJSON válido: ${data.features.length} feature(s), ${ids.size} id(s) únicos`,
)
