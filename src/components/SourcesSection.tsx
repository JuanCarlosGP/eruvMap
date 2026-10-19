import { useMemo, useState } from 'react'
import { useI18n } from '../i18n/I18nProvider'
import { eruvDisplayName } from '../lib/eruvData'
import { countryLabel } from '../lib/placeNames'
import {
  groupEruvsByPlace,
  type SourcesCityGroup,
} from '../lib/sourcesGroups'
import type { EruvFeature } from '../types/eruv'

interface SourcesSectionProps {
  features: EruvFeature[]
  selectedId: string | null
  onEruvActivate: (feature: EruvFeature) => void
}

function EruvSourceList({
  cityFeatures,
  selectedId,
  onEruvActivate,
}: {
  cityFeatures: EruvFeature[]
  selectedId: string | null
  onEruvActivate: (feature: EruvFeature) => void
}) {
  const { t, locale } = useI18n()

  return (
    <ul className="sources-panel__eruvs" role="list">
      {cityFeatures.map((feature) => {
        const id = String(feature.id)
        const name = eruvDisplayName(feature.properties, locale)
        const p = feature.properties
        const selected = selectedId === id

        return (
          <li
            key={id}
            className={`sources-panel__item${selected ? ' sources-panel__item--selected' : ''}`}
          >
            <a
              href={`#${id}`}
              className="sources-panel__activate"
              onClick={(event) => {
                event.preventDefault()
                onEruvActivate(feature)
              }}
              aria-current={selected ? 'true' : undefined}
              aria-label={t('sourcesActivate', { name })}
            >
              {name}
            </a>
            <dl className="sources-panel__meta">
              <div>
                <dt>{t('source')}</dt>
                <dd>
                  <a
                    href={p.source_url}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {p.source}
                  </a>
                </dd>
              </div>
              <div>
                <dt>{t('license')}</dt>
                <dd>{p.license}</dd>
              </div>
              <div>
                <dt>{t('verified')}</dt>
                <dd>{p.verified_at || t('noDate')}</dd>
              </div>
            </dl>
          </li>
        )
      })}
    </ul>
  )
}

function CityGroups({
  cities,
  country,
  selectedId,
  onEruvActivate,
}: {
  cities: SourcesCityGroup[]
  country: string
  selectedId: string | null
  onEruvActivate: (feature: EruvFeature) => void
}) {
  return (
    <ul className="sources-panel__cities" role="list">
      {cities.map(({ city, features: cityFeatures }) => (
        <li key={`${country}-${city}`} className="sources-panel__city">
          <h4 className="sources-panel__city-name">{city}</h4>
          <EruvSourceList
            cityFeatures={cityFeatures}
            selectedId={selectedId}
            onEruvActivate={onEruvActivate}
          />
        </li>
      ))}
    </ul>
  )
}

function featureMatches(feature: EruvFeature, query: string, locale: 'he' | 'en') {
  const p = feature.properties
  const haystack = [
    eruvDisplayName(p, locale),
    p.name_en,
    p.name_he,
    p.city,
    p.country,
    countryLabel(p.country, locale),
    p.state,
    p.source,
  ]
    .filter(Boolean)
    .join(' ')
    .toLowerCase()
  return haystack.includes(query)
}

export function SourcesSection({
  features,
  selectedId,
  onEruvActivate,
}: SourcesSectionProps) {
  const { t, locale } = useI18n()
  const [query, setQuery] = useState('')

  const groups = useMemo(
    () => groupEruvsByPlace(features, locale),
    [features, locale],
  )

  const lastChecked = useMemo(() => {
    const dates = features
      .map((feature) => feature.properties.verified_at)
      .filter((date): date is string => Boolean(date))
      .sort()
    return dates.at(-1) ?? ''
  }, [features])

  const visibleGroups = useMemo(() => {
    const q = query.trim().toLowerCase()
    if (!q) return groups
    return groups.flatMap((group) => {
      if (group.states) {
        const states = group.states.flatMap((state) => {
          const cities = state.cities
            .map((city) => ({
              ...city,
              features: city.features.filter((feature) =>
                featureMatches(feature, q, locale),
              ),
            }))
            .filter((city) => city.features.length > 0)
          return cities.length > 0 ? [{ ...state, cities }] : []
        })
        return states.length > 0 ? [{ ...group, states }] : []
      }
      const cities = group.cities
        .map((city) => ({
          ...city,
          features: city.features.filter((feature) =>
            featureMatches(feature, q, locale),
          ),
        }))
        .filter((city) => city.features.length > 0)
      return cities.length > 0 ? [{ ...group, cities }] : []
    })
  }, [groups, query, locale])

  return (
    <section className="sources-panel" aria-labelledby="sources-panel-title">
      <details className="sources-panel__details" open>
        <summary className="sources-panel__summary" id="sources-panel-title">
          {t('sourcesSectionTitle')}
        </summary>
        <label className="sources-panel__search">
          <span className="visually-hidden">{t('sourcesSearchAria')}</span>
          <input
            type="search"
            className="sources-panel__search-input"
            value={query}
            placeholder={t('sourcesSearchPlaceholder')}
            onChange={(event) => setQuery(event.target.value)}
          />
        </label>
        <div className="sources-panel__body">
          <figure className="sources-panel__figure">
            <picture>
              <source srcSet={`${import.meta.env.BASE_URL}og.webp`} type="image/webp" />
              <img
                src={`${import.meta.env.BASE_URL}og.png`}
                width={1200}
                height={630}
                alt={t('sourcesImageAlt')}
                loading="lazy"
                decoding="async"
              />
            </picture>
          </figure>
          <p className="sources-panel__intro">{t('sourcesIntro')}</p>
          <h2 className="sources-panel__list-heading">{t('sourcesMethodTitle')}</h2>
          <p className="sources-panel__intro">{t('sourcesMethod')}</p>
          {lastChecked ? (
            <p className="sources-panel__updated">
              <time dateTime={lastChecked}>{t('sourcesUpdated', { date: lastChecked })}</time>
            </p>
          ) : null}
          <h2 className="sources-panel__list-heading">{t('sourcesListHeading')}</h2>
          {visibleGroups.length === 0 ? (
            <p className="sources-panel__empty">{t('sourcesNoMatches')}</p>
          ) : null}
          <ul className="sources-panel__tree" role="list">
            {visibleGroups.map(({ country, states, cities }) => (
              <li key={country} className="sources-panel__country">
                <h3 className="sources-panel__country-name">
                  {countryLabel(country, locale)}
                </h3>
                {states ? (
                  <ul className="sources-panel__states" role="list">
                    {states.map(({ state, cities: stateCities }) => (
                      <li
                        key={`${country}-${state}`}
                        className="sources-panel__state"
                      >
                        <h4 className="sources-panel__state-name">
                          {t('usState')}: {state}
                        </h4>
                        <CityGroups
                          cities={stateCities}
                          country={`${country}-${state}`}
                          selectedId={selectedId}
                          onEruvActivate={onEruvActivate}
                        />
                      </li>
                    ))}
                  </ul>
                ) : (
                  <CityGroups
                    cities={cities}
                    country={country}
                    selectedId={selectedId}
                    onEruvActivate={onEruvActivate}
                  />
                )}
              </li>
            ))}
          </ul>
          <p className="sources-panel__osm">
            {t('osmContains')}{' '}
            <a
              href="https://www.openstreetmap.org/copyright"
              target="_blank"
              rel="noopener noreferrer"
            >
              OpenStreetMap
            </a>{' '}
            {t('osmOdb')}
          </p>
        </div>
      </details>
    </section>
  )
}
