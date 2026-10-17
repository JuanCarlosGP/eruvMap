import MapboxDraw from '@mapbox/mapbox-gl-draw'
import mapboxgl from 'mapbox-gl'
import { useEffect, useRef, useState } from 'react'
import type { Geometry } from 'geojson'
import { useI18n } from '../i18n/I18nProvider'
import type { ContributeDrawTool } from '../lib/contribution'
import { perimeterFeatures, pointMapFeatures } from '../lib/eruvData'
import { featureCenterForMap } from '../lib/geometry'
import { mapboxLanguage } from '../lib/mapLocale'
import { MAP_COLORS, mapboxStyleForTheme } from '../lib/mapConfig'
import type { Theme } from '../theme/ThemeProvider'
import type { EruvFeature, EruvStatusFilter } from '../types/eruv'
import '@mapbox/mapbox-gl-draw/dist/mapbox-gl-draw.css'
import 'mapbox-gl/dist/mapbox-gl.css'

function drawModeForTool(tool: ContributeDrawTool): string {
  switch (tool) {
    case 'polygon':
      return 'draw_polygon'
    case 'line':
      return 'draw_line_string'
    case 'point':
      return 'draw_point'
  }
}

export interface FlyToRequest {
  center: [number, number]
  zoom?: number
}

interface MapViewProps {
  features: EruvFeature[]
  statusFilter: EruvStatusFilter
  theme: Theme
  token: string | undefined
  selectedId: string | null
  onSelect: (feature: EruvFeature | null) => void
  flyToRequest: FlyToRequest | null
  onFlyToComplete?: () => void
  contributeMode?: boolean
  drawTool?: ContributeDrawTool
  onDrawGeometryChange?: (geometry: Geometry | null) => void
  clearDrawNonce?: number
}

function statusFilterExpression(
  filter: EruvStatusFilter,
): mapboxgl.FilterSpecification | null {
  if (filter === 'all') return null
  return ['==', ['get', 'status'], filter]
}

function resolveFeatureId(props: GeoJSON.GeoJsonProperties): string {
  const p = props as Record<string, unknown>
  return String(p.eruv_id ?? p.id ?? '')
}

export function MapView({
  features,
  statusFilter,
  theme,
  token,
  selectedId,
  onSelect,
  flyToRequest,
  onFlyToComplete,
  contributeMode = false,
  drawTool = 'polygon',
  onDrawGeometryChange,
  clearDrawNonce = 0,
}: MapViewProps) {
  const { t, locale } = useI18n()
  const containerRef = useRef<HTMLDivElement>(null)
  const mapRef = useRef<mapboxgl.Map | null>(null)
  const featuresRef = useRef(features)
  const onSelectRef = useRef(onSelect)
  const onDrawChangeRef = useRef(onDrawGeometryChange)
  const contributeModeRef = useRef(contributeMode)
  const drawRef = useRef<MapboxDraw | null>(null)
  useEffect(() => {
    featuresRef.current = features
  }, [features])
  useEffect(() => {
    onSelectRef.current = onSelect
  }, [onSelect])
  useEffect(() => {
    onDrawChangeRef.current = onDrawGeometryChange
  }, [onDrawGeometryChange])
  useEffect(() => {
    contributeModeRef.current = contributeMode
  }, [contributeMode])

  const [mapReady, setMapReady] = useState(false)
  const [mapError, setMapError] = useState(false)

  useEffect(() => {
    if (!token || !containerRef.current) return

    setMapError(false)
    setMapReady(false)

    mapboxgl.accessToken = token
    const map = new mapboxgl.Map({
      container: containerRef.current,
      style: mapboxStyleForTheme(theme),
      center: [10, 30],
      zoom: 1.8,
      attributionControl: true,
      cooperativeGestures: true,
    })

    map.addControl(
      new mapboxgl.NavigationControl({ showCompass: false }),
      locale === 'he' ? 'bottom-left' : 'bottom-right',
    )

    const loadTimeout = window.setTimeout(() => {
      setMapError(true)
    }, 8000)

    map.on('load', () => {
      window.clearTimeout(loadTimeout)

      map.addSource('eruv-perimeters', {
        type: 'geojson',
        data: perimeterFeatures(featuresRef.current),
      })

      map.addSource('eruv-points', {
        type: 'geojson',
        data: {
          type: 'FeatureCollection',
          features: pointMapFeatures(featuresRef.current),
        },
        cluster: true,
        clusterMaxZoom: 12,
        clusterRadius: 48,
      })

      const colors = MAP_COLORS[theme]

      map.addLayer({
        id: 'eruv-fill',
        type: 'fill',
        source: 'eruv-perimeters',
        filter: [
          'all',
          ['==', ['geometry-type'], 'Polygon'],
          ['!=', ['get', 'is_partial'], true],
        ],
        paint: {
          'fill-color': colors.fill,
          'fill-outline-color': colors.outline,
        },
      })

      map.addLayer({
        id: 'eruv-line',
        type: 'line',
        source: 'eruv-perimeters',
        filter: [
          'any',
          ['==', ['geometry-type'], 'LineString'],
          ['==', ['geometry-type'], 'MultiLineString'],
        ],
        paint: {
          'line-color': colors.line,
          'line-width': [
            'case',
            ['==', ['get', 'is_partial'], true],
            4,
            colors.lineWidth,
          ],
          'line-dasharray': [
            'case',
            ['==', ['get', 'is_partial'], true],
            ['literal', [2, 1.5]],
            ['literal', [1, 0]],
          ],
        },
      })

      map.addLayer({
        id: 'eruv-clusters',
        type: 'circle',
        source: 'eruv-points',
        filter: ['has', 'point_count'],
        paint: {
          'circle-color': colors.cluster,
          'circle-radius': [
            'step',
            ['get', 'point_count'],
            18,
            5,
            22,
            15,
            28,
          ],
          'circle-stroke-width': 2,
          'circle-stroke-color': colors.accent,
        },
      })

      map.addLayer({
        id: 'eruv-cluster-count',
        type: 'symbol',
        source: 'eruv-points',
        filter: ['has', 'point_count'],
        layout: {
          'text-field': ['get', 'point_count_abbreviated'],
          'text-font': ['DIN Pro Medium', 'Arial Unicode MS Bold'],
          'text-size': 13,
        },
        paint: {
          'text-color': colors.clusterText,
        },
      })

      map.addLayer({
        id: 'eruv-point-approx',
        type: 'circle',
        source: 'eruv-points',
        filter: [
          'all',
          ['!', ['has', 'point_count']],
          ['==', ['get', 'geometry_precision'], 'approximate'],
        ],
        paint: {
          'circle-color': colors.approxFill,
          'circle-radius': 11,
          'circle-stroke-width': 3,
          'circle-stroke-color': colors.approxStroke,
          'circle-opacity': 0.92,
        },
      })

      const selectById = (id: string) => {
        const found = featuresRef.current.find(
          (f) => String(f.id) === id || String(f.properties.id) === id,
        )
        onSelectRef.current(found ?? null)
      }

      map.on('mouseenter', 'eruv-clusters', () => {
        map.getCanvas().style.cursor = 'pointer'
      })
      map.on('mouseleave', 'eruv-clusters', () => {
        map.getCanvas().style.cursor = ''
      })

      map.on('click', 'eruv-clusters', (e) => {
        const hits = map.queryRenderedFeatures(e.point, {
          layers: ['eruv-clusters'],
        })
        const cluster = hits[0]
        if (!cluster?.properties?.cluster_id) return
        const source = map.getSource('eruv-points') as mapboxgl.GeoJSONSource
        source.getClusterExpansionZoom(
          cluster.properties.cluster_id as number,
          (err, zoom) => {
            if (err || zoom == null) return
            map.easeTo({
              center: (cluster.geometry as GeoJSON.Point).coordinates as [
                number,
                number,
              ],
              zoom,
            })
          },
        )
      })

      const interactiveLayers = [
        'eruv-point-approx',
        'eruv-line',
        'eruv-fill',
      ] as const

      for (const layerId of interactiveLayers) {
        map.on('click', layerId, (e) => {
          if (contributeModeRef.current) return
          const f = e.features?.[0]
          if (!f?.properties) return
          selectById(resolveFeatureId(f.properties))
        })
        map.on('mouseenter', layerId, () => {
          map.getCanvas().style.cursor = 'pointer'
        })
        map.on('mouseleave', layerId, () => {
          map.getCanvas().style.cursor = ''
        })
      }

      try {
        map.setLanguage(mapboxLanguage(locale))
      } catch {
        /* algunos estilos no exponen setLanguage */
      }

      setMapReady(true)
    })

    mapRef.current = map
    return () => {
      window.clearTimeout(loadTimeout)
      setMapReady(false)
      map.remove()
      mapRef.current = null
    }
  }, [token, theme, locale])

  useEffect(() => {
    const map = mapRef.current
    if (!map || !mapReady) return
    try {
      map.setLanguage(mapboxLanguage(locale))
    } catch {
      /* ignore */
    }
  }, [locale, mapReady])

  useEffect(() => {
    const map = mapRef.current
    if (!map || !mapReady) return

    const perimeterSource = map.getSource('eruv-perimeters') as mapboxgl.GeoJSONSource
    const pointSource = map.getSource('eruv-points') as mapboxgl.GeoJSONSource
    if (!perimeterSource || !pointSource) return

    perimeterSource.setData(perimeterFeatures(features))
    pointSource.setData({
      type: 'FeatureCollection',
      features: pointMapFeatures(features),
    })
  }, [features, mapReady])

  useEffect(() => {
    const map = mapRef.current
    if (!map || !mapReady) return

    const expr = statusFilterExpression(statusFilter)
    const layers = [
      'eruv-fill',
      'eruv-line',
      'eruv-clusters',
      'eruv-cluster-count',
      'eruv-point-approx',
    ]
    for (const id of layers) {
      if (!map.getLayer(id)) continue
      map.setFilter(id, expr ?? undefined)
    }
  }, [statusFilter, mapReady])

  useEffect(() => {
    const map = mapRef.current
    if (!map || !flyToRequest) return
    map.flyTo({
      center: flyToRequest.center,
      zoom: flyToRequest.zoom ?? 11,
      essential: true,
    })
    map.once('moveend', () => onFlyToComplete?.())
  }, [flyToRequest, onFlyToComplete])

  useEffect(() => {
    const map = mapRef.current
    if (!map || !mapReady || !selectedId) return
    const feature = features.find(
      (f) => String(f.id) === selectedId || String(f.properties.id) === selectedId,
    )
    if (!feature) return
    const [lng, lat] = featureCenterForMap(feature)
    map.easeTo({ center: [lng, lat], zoom: Math.max(map.getZoom(), 12) })
  }, [selectedId, features, mapReady])

  useEffect(() => {
    const map = mapRef.current
    if (!map || !mapReady) return

    const syncDraw = () => {
      const draw = drawRef.current
      if (!draw) return
      const feat = draw.getAll().features[0]
      onDrawChangeRef.current?.(feat?.geometry ?? null)
    }
    const onDrawDelete = () => onDrawChangeRef.current?.(null)

    if (contributeMode) {
      if (!drawRef.current) {
        const draw = new MapboxDraw({
          displayControlsDefault: false,
          controls: {},
          defaultMode: drawModeForTool(drawTool),
        })
        map.addControl(draw as mapboxgl.IControl)
        map.on('draw.create', syncDraw)
        map.on('draw.update', syncDraw)
        map.on('draw.delete', onDrawDelete)
        drawRef.current = draw
      }
      drawRef.current.changeMode(drawModeForTool(drawTool))
    } else if (drawRef.current) {
      map.off('draw.create', syncDraw)
      map.off('draw.update', syncDraw)
      map.off('draw.delete', onDrawDelete)
      map.removeControl(drawRef.current as mapboxgl.IControl)
      drawRef.current = null
      onDrawChangeRef.current?.(null)
    }
  }, [contributeMode, mapReady, drawTool])

  useEffect(() => {
    if (!clearDrawNonce || !drawRef.current) return
    drawRef.current.deleteAll()
    onDrawChangeRef.current?.(null)
  }, [clearDrawNonce])

  if (!token || mapError) {
    return (
      <div className="state-card state-card--error map-shell map-shell--error" role="alert">
        <h3>{t('mapErrorTitle')}</h3>
        <p>{t('mapErrorToken')}</p>
      </div>
    )
  }

  return (
    <div className="map-shell">
      {!mapReady && !mapError && (
        <div className="map-shell__overlay" aria-live="polite">
          <div className="spinner" aria-hidden />
          <p>{t('loadingMap')}</p>
        </div>
      )}
      <div ref={containerRef} className="map-canvas" role="region" aria-label={t('tagline')} />
    </div>
  )
}
