import { useI18n } from '../i18n/I18nProvider'
import { eruvDisplayName, isPartialPerimeter } from '../lib/eruvData'
import { countryLabel } from '../lib/placeNames'
import type { EruvFeature } from '../types/eruv'
import { IconClose } from './icons'

interface DetailPanelProps {
  feature: EruvFeature | null
  onClose: () => void
  onProposeEdit: (feature: EruvFeature) => void
}

export function DetailPanel({ feature, onClose, onProposeEdit }: DetailPanelProps) {
  const { t, locale } = useI18n()

  if (!feature) return null

  const p = feature.properties
  const title = eruvDisplayName(p, locale)
  const partial = p.is_partial ?? isPartialPerimeter(p.note)
  const approximate = p.geometry_precision === 'approximate'

  return (
    <aside
      className="detail-panel"
      role="dialog"
      aria-labelledby="detail-title"
      aria-modal="false"
    >
      <header className="detail-panel__header">
        <h2 id="detail-title" className="detail-panel__title">
          {title}
        </h2>
        <button
          type="button"
          className="btn btn--ghost btn--icon"
          onClick={onClose}
          aria-label={t('closePanel')}
        >
          <IconClose />
        </button>
      </header>

      <button
        type="button"
        className="btn btn--secondary detail-panel__edit"
        onClick={() => onProposeEdit(feature)}
      >
        {t('proposeEdit')}
      </button>

      <div className="detail-panel__badges">
        {p.geometry_kind === 'point' && (
          <p className="badge badge--approx" role="status">
            {t('representativePointDisclaimer')}
          </p>
        )}
        {approximate && p.geometry_kind !== 'point' && (
          <p className="badge badge--approx" role="status">
            {t('approximatePerimeter')}
          </p>
        )}
        {partial && p.geometry_kind === 'perimeter' && (
          <p className="badge badge--partial" role="status">
            {t('partialPerimeter')}
          </p>
        )}
      </div>

      <dl className="detail-panel__meta">
        <div>
          <dt>{t('city')}</dt>
          <dd>{p.city}</dd>
        </div>
        <div>
          <dt>{t('country')}</dt>
          <dd>{countryLabel(p.country, locale)}</dd>
        </div>
        {p.state && (
          <div>
            <dt>{t('usState')}</dt>
            <dd>{p.state}</dd>
          </div>
        )}
        <div>
          <dt>{t('geometryType')}</dt>
          <dd>
            {p.geometry_kind === 'point'
              ? t('geometryPoint')
              : partial
                ? t('geometryPartialLine')
                : t('geometryPerimeter')}
          </dd>
        </div>
        <div>
          <dt>{t('status')}</dt>
          <dd>
            <span
              className={`status-dot status-dot--${p.status}`}
              aria-hidden
            />
            {p.status === 'active' ? t('statusActive') : t('statusUnknown')}
          </dd>
        </div>
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
        {p.status_as_of && (
          <div>
            <dt>{t('statusAsOf')}</dt>
            <dd>{p.status_as_of}</dd>
          </div>
        )}
        {p.hotline_or_contact && (
          <div>
            <dt>{t('hotlineOrContact')}</dt>
            <dd>{p.hotline_or_contact}</dd>
          </div>
        )}
      </dl>

      {p.boundary_map_url && (
        <a
          className="btn btn--secondary detail-panel__link"
          href={p.boundary_map_url}
          target="_blank"
          rel="noopener noreferrer"
        >
          {t('officialBoundaryMap')}
        </a>
      )}

      {p.contact_url && (
        <a
          className="btn btn--secondary detail-panel__link"
          href={p.contact_url}
          target="_blank"
          rel="noopener noreferrer"
        >
          {t('contact')}
        </a>
      )}

      {p.note && (
        <p className="detail-panel__notes" role="note">
          {p.note}
        </p>
      )}

      {p.extra_note && (
        <p className="detail-panel__notes" role="note">
          {p.extra_note}
        </p>
      )}
    </aside>
  )
}
