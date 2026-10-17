import { useI18n } from '../i18n/I18nProvider'

export function DataAttribution() {
  const { t } = useI18n()

  return (
    <footer className="data-attribution">
      <p>
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
    </footer>
  )
}
