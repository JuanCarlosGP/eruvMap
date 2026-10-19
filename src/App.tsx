import { useCallback, useEffect, useMemo, useState } from 'react'
import type { Geometry } from 'geojson'
import { ContributePanel } from './components/ContributePanel'
import { DetailPanel } from './components/DetailPanel'
import { SourcesSection } from './components/SourcesSection'
import { Header } from './components/Header'
import { MapToolbar } from './components/MapToolbar'
import { MapView, type FlyToRequest } from './components/MapView'
import { useI18n } from './i18n/I18nProvider'
import type { ContributeDrawTool } from './lib/contribution'
import { normalizeFeatures } from './lib/eruvData'
import {
  featureCenterForMap,
  flyZoomForFeature,
} from './lib/geometry'
import { mapboxLanguage } from './lib/mapLocale'
import { loadSecureEruvsData } from './lib/secureDataLoader'
import { useTheme } from './theme/ThemeProvider'
import type { EruvFeature } from './types/eruv'

const MAPBOX_TOKEN = import.meta.env.VITE_MAPBOX_TOKEN

function App() {
  const { t, locale } = useI18n()
  const { theme } = useTheme()

  const [allFeatures, setAllFeatures] = useState<EruvFeature[]>([])
  const [dataLoading, setDataLoading] = useState(true)

  useEffect(() => {
    const chrome = document.querySelector('.map-chrome')
    if (!chrome) return
    const apply = () => {
      const bottom = chrome.getBoundingClientRect().bottom
      document.documentElement.style.setProperty('--map-chrome-bottom', `${bottom}px`)
    }
    apply()
    const observer = new ResizeObserver(apply)
    observer.observe(chrome)
    window.addEventListener('resize', apply)
    return () => {
      observer.disconnect()
      window.removeEventListener('resize', apply)
    }
  }, [])

  useEffect(() => {
    loadSecureEruvsData()
      .then((data) => {
        setAllFeatures(normalizeFeatures(data))
        setDataLoading(false)
      })
      .catch((err) => {
        console.error('Failed to load secure eruvs dataset:', err)
        setDataLoading(false)
      })
  }, [])

  const [selected, setSelected] = useState<EruvFeature | null>(null)
  const [searchQuery, setSearchQuery] = useState('')
  const [searchBusy, setSearchBusy] = useState(false)
  const [nearMeBusy, setNearMeBusy] = useState(false)
  const [flyToRequest, setFlyToRequest] = useState<FlyToRequest | null>(null)
  const [geoMessage, setGeoMessage] = useState<string | null>(null)

  const [contributeOpen, setContributeOpen] = useState(false)
  const [drawTool, setDrawTool] = useState<ContributeDrawTool>('polygon')
  const [drawGeometry, setDrawGeometry] = useState<Geometry | null>(null)
  const [clearDrawNonce, setClearDrawNonce] = useState(0)

  const handleSearch = useCallback(async () => {
    const q = searchQuery.trim()
    if (!q || !MAPBOX_TOKEN) return
    setSearchBusy(true)
    setGeoMessage(null)
    try {
      const url = new URL(
        `https://api.mapbox.com/geocoding/v5/mapbox.places/${encodeURIComponent(q)}.json`,
      )
      url.searchParams.set('access_token', MAPBOX_TOKEN)
      url.searchParams.set('limit', '1')
      url.searchParams.set('language', mapboxLanguage(locale))
      const res = await fetch(url)
      if (!res.ok) throw new Error('geocode failed')
      const data = await res.json()
      const place = data.features?.[0]
      if (!place?.center) {
        setGeoMessage(t('searchNoResults'))
        return
      }
      setFlyToRequest({
        center: place.center as [number, number],
        zoom: 10,
      })
    } catch {
      setGeoMessage(t('searchNoResults'))
    } finally {
      setSearchBusy(false)
    }
  }, [searchQuery, t, locale])

  const handleNearMe = useCallback(() => {
    setGeoMessage(null)
    if (!navigator.geolocation) {
      setGeoMessage(t('geoUnsupported'))
      return
    }
    setNearMeBusy(true)
    navigator.geolocation.getCurrentPosition(
      (pos) => {
        setFlyToRequest({
          center: [pos.coords.longitude, pos.coords.latitude],
          zoom: 12,
        })
        setNearMeBusy(false)
      },
      () => {
        setGeoMessage(t('geoDenied'))
        setNearMeBusy(false)
      },
      { enableHighAccuracy: true, timeout: 12000 },
    )
  }, [t])

  const clearFlyTo = useCallback(() => setFlyToRequest(null), [])

  const [editing, setEditing] = useState<EruvFeature | null>(null)

  const openContribute = useCallback(() => {
    setEditing(null)
    setSelected(null)
    setDrawGeometry(null)
    setDrawTool('polygon')
    setClearDrawNonce((n) => n + 1)
    setContributeOpen(true)
  }, [])

  const proposeEdit = useCallback((feature: EruvFeature) => {
    setEditing(feature)
    setSelected(null)
    setDrawGeometry(feature.geometry)
    setDrawTool(feature.geometry.type === 'Point' ? 'point' : 'polygon')
    setContributeOpen(true)
  }, [])

  const closeContribute = useCallback(() => {
    setContributeOpen(false)
    setEditing(null)
    setDrawGeometry(null)
  }, [])

  const clearDraw = useCallback(() => {
    setDrawGeometry(null)
    setClearDrawNonce((n) => n + 1)
  }, [])

  const activateEruvFromSources = useCallback(
    (feature: EruvFeature) => {
      setContributeOpen(false)
      setEditing(null)
      setDrawGeometry(null)
      setSelected(feature)
      setFlyToRequest({
        center: featureCenterForMap(feature),
        zoom: flyZoomForFeature(feature),
      })
    },
    [],
  )

  const mapFeatures = useMemo(() => {
    if (!editing) return allFeatures
    const id = String(editing.id)
    const propId = editing.properties.id
    return allFeatures.filter(
      (feature) => String(feature.id) !== id && feature.properties.id !== propId,
    )
  }, [allFeatures, editing])

  const sidePanelOpen = Boolean(selected) || contributeOpen

  return (
    <div className={`app-layout${sidePanelOpen ? ' app-layout--panel' : ''}`}>
      <main
        className={`map-layout${sidePanelOpen ? ' map-layout--with-panel' : ''}`}
      >
        <MapView
          features={mapFeatures}
          theme={theme}
          token={MAPBOX_TOKEN}
          selectedId={selected ? String(selected.id) : null}
          onSelect={setSelected}
          flyToRequest={flyToRequest}
          onFlyToComplete={clearFlyTo}
          contributeMode={contributeOpen}
          drawTool={drawTool}
          onDrawGeometryChange={setDrawGeometry}
          clearDrawNonce={clearDrawNonce}
          seedGeometry={editing?.geometry ?? null}
        />
        {dataLoading && (
          <div className="state-card state-card--empty map-layout__empty" role="status">
            <p>{t('loadingData')}</p>
          </div>
        )}
        {!dataLoading && allFeatures.length === 0 && !contributeOpen && (
          <div className="state-card state-card--empty map-layout__empty">
            <p>{t('noResults')}</p>
          </div>
        )}
        {contributeOpen ? (
          <ContributePanel
            open={contributeOpen}
            onClose={closeContribute}
            drawTool={drawTool}
            onDrawToolChange={setDrawTool}
            geometry={drawGeometry}
            onClearDraw={clearDraw}
            initialForm={
              editing
                ? {
                    name_en: editing.properties.name_en,
                    name_he: editing.properties.name_he ?? '',
                    city: editing.properties.city,
                    country: editing.properties.country,
                    source_url: editing.properties.source_url,
                    contact_url: editing.properties.contact_url ?? '',
                    permission: false,
                  }
                : undefined
            }
            editing={editing}
          />
        ) : (
          <DetailPanel
            feature={selected}
            onClose={() => setSelected(null)}
            onProposeEdit={proposeEdit}
          />
        )}
      </main>
      <div className="map-chrome">
        <Header onPropose={openContribute} contributeActive={contributeOpen} />
        <MapToolbar
          searchQuery={searchQuery}
          onSearchQueryChange={setSearchQuery}
          onSearchSubmit={handleSearch}
          searchBusy={searchBusy}
          onNearMe={handleNearMe}
          nearMeBusy={nearMeBusy}
        />
        {geoMessage && (
          <p className="inline-message" role="status">
            {geoMessage}
          </p>
        )}
      </div>
      <SourcesSection
        features={allFeatures}
        selectedId={selected ? String(selected.id) : null}
        onEruvActivate={activateEruvFromSources}
      />
    </div>
  )
}

export default App
