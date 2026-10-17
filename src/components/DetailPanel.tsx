import { useI18n } from '../i18n/I18nProvider'
import { eruvDisplayName, isPartialPerimeter } from '../lib/eruvData'
import type { EruvFeature } from '../types/eruv'
import { IconClose } from './icons'

interface DetailPanelProps {
  feature: EruvFeature | null
  onClose: () => void
}

export function DetailPanel({ feature, onClose }: DetailPanelProps) {
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

      <div className="detail-panel__badges">
        {approximate && (
          <p className="badge badge--approx" role="status">
            {t('approximateLocation')}
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
          <dd>{p.country}</dd>
        </div>
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
      </dl>

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
    </aside>
  )
}
