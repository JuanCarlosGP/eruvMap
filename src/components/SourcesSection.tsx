import { useMemo } from 'react'
import { useI18n } from '../i18n/I18nProvider'
import { eruvDisplayName } from '../lib/eruvData'
import { groupEruvsByPlace } from '../lib/sourcesGroups'
import type { EruvFeature } from '../types/eruv'

interface SourcesSectionProps {
  features: EruvFeature[]
  selectedId: string | null
  onEruvActivate: (feature: EruvFeature) => void
}

export function SourcesSection({
  features,
  selectedId,
  onEruvActivate,
}: SourcesSectionProps) {
  const { t, locale } = useI18n()

  const groups = useMemo(
    () => groupEruvsByPlace(features, locale),
    [features, locale],
  )

  return (
    <section className="sources-panel" aria-labelledby="sources-panel-title">
      <details className="sources-panel__details">
        <summary className="sources-panel__summary" id="sources-panel-title">
          {t('sourcesSectionTitle')}
        </summary>
        <div className="sources-panel__body">
          <ul className="sources-panel__tree" role="list">
            {groups.map(({ country, cities }) => (
              <li key={country} className="sources-panel__country">
                <h3 className="sources-panel__country-name">{country}</h3>
                <ul className="sources-panel__cities" role="list">
                  {cities.map(({ city, features: cityFeatures }) => (
                    <li key={`${country}-${city}`} className="sources-panel__city">
                      <h4 className="sources-panel__city-name">{city}</h4>
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
                              <button
                                type="button"
                                className="sources-panel__activate"
                                onClick={() => onEruvActivate(feature)}
                                aria-current={selected ? 'true' : undefined}
                                aria-label={t('sourcesActivate', { name })}
                              >
                                {name}
                              </button>
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
                    </li>
                  ))}
                </ul>
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
