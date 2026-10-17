import { useCallback, useMemo, useState } from 'react'
import eruvsData from '../data/eruvs.geojson'
import { DetailPanel } from './components/DetailPanel'
import { Header } from './components/Header'
import { MapToolbar } from './components/MapToolbar'
import { MapView, type FlyToRequest } from './components/MapView'
import { useI18n } from './i18n/I18nProvider'
import { mapboxLanguage } from './lib/mapLocale'
import { useTheme } from './theme/ThemeProvider'
import type { EruvCollection, EruvEstadoFilter, EruvFeature } from './types/eruv'

const MAPBOX_TOKEN = import.meta.env.VITE_MAPBOX_TOKEN

function normalizeFeatures(collection: EruvCollection): EruvFeature[] {
  return collection.features.map((f, index) => ({
    ...f,
    id: String(f.id ?? `feature-${index}`),
  })) as EruvFeature[]
}

function App() {
  const { t, locale } = useI18n()
  const { theme } = useTheme()

  const allFeatures = useMemo(() => normalizeFeatures(eruvsData as EruvCollection), [])

  const [statusFilter, setStatusFilter] = useState<EruvEstadoFilter>('all')
  const [selected, setSelected] = useState<EruvFeature | null>(null)
  const [searchQuery, setSearchQuery] = useState('')
  const [searchBusy, setSearchBusy] = useState(false)
  const [nearMeBusy, setNearMeBusy] = useState(false)
  const [flyToRequest, setFlyToRequest] = useState<FlyToRequest | null>(null)
  const [geoMessage, setGeoMessage] = useState<string | null>(null)

  const filteredFeatures = useMemo(() => {
    if (statusFilter === 'all') return allFeatures
    return allFeatures.filter((f) => f.properties.estado === statusFilter)
  }, [allFeatures, statusFilter])

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

  return (
    <div className="app-layout">
      <Header />
      <MapToolbar
        searchQuery={searchQuery}
        onSearchQueryChange={setSearchQuery}
        onSearchSubmit={handleSearch}
        searchBusy={searchBusy}
        statusFilter={statusFilter}
        onStatusFilterChange={(f) => {
          setStatusFilter(f)
          if (selected && f !== 'all' && selected.properties.estado !== f) {
            setSelected(null)
          }
        }}
        onNearMe={handleNearMe}
        nearMeBusy={nearMeBusy}
      />
      {geoMessage && (
        <p className="inline-message" role="status">
          {geoMessage}
        </p>
      )}
      <main
        className={`map-layout${selected ? ' map-layout--with-panel' : ''}`}
      >
        <MapView
          features={filteredFeatures}
          statusFilter={statusFilter}
          theme={theme}
          token={MAPBOX_TOKEN}
          selectedId={selected ? String(selected.id) : null}
          onSelect={setSelected}
          flyToRequest={flyToRequest}
          onFlyToComplete={clearFlyTo}
        />
        {filteredFeatures.length === 0 && (
          <div className="state-card state-card--empty map-layout__empty">
            <p>{t('noResults')}</p>
          </div>
        )}
        <DetailPanel feature={selected} onClose={() => setSelected(null)} />
      </main>
    </div>
  )
}

export default App
