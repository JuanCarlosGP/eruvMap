import { useI18n } from '../i18n/I18nProvider'
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
  const dateLabel =
    p.fecha_verificacion ??
    (locale === 'es' ? 'Sin fecha' : 'No date')

  return (
    <aside
      className="detail-panel"
      role="dialog"
      aria-labelledby="detail-title"
      aria-modal="false"
    >
      <header className="detail-panel__header">
        <h2 id="detail-title" className="detail-panel__title">
          {p.nombre}
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

      {p.es_ejemplo && (
        <p className="badge badge--example" role="status">
          {t('exampleBadge')}
        </p>
      )}

      <dl className="detail-panel__meta">
        <div>
          <dt>{t('city')}</dt>
          <dd>{p.ciudad}</dd>
        </div>
        <div>
          <dt>{t('country')}</dt>
          <dd>{p.pais_nombre}</dd>
        </div>
        <div>
          <dt>{t('geometryType')}</dt>
          <dd>
            {p.tipo_geometria === 'linea'
              ? t('geometryLine')
              : t('geometryPolygon')}
          </dd>
        </div>
        <div>
          <dt>{t('status')}</dt>
          <dd>
            <span
              className={`status-dot status-dot--${p.estado}`}
              aria-hidden
            />
            {p.estado === 'activo' ? t('statusActive') : t('statusUnknown')}
          </dd>
        </div>
        <div>
          <dt>{t('source')}</dt>
          <dd>{p.fuente}</dd>
        </div>
        <div>
          <dt>{t('verified')}</dt>
          <dd>{dateLabel}</dd>
        </div>
      </dl>

      {p.contacto_url && (
        <a
          className="btn btn--secondary detail-panel__link"
          href={p.contacto_url}
          target="_blank"
          rel="noopener noreferrer"
        >
          {t('contact')}
        </a>
      )}

      {p.notas && <p className="detail-panel__notes">{p.notas}</p>}
    </aside>
  )
}
