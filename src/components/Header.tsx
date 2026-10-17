import { useI18n } from '../i18n/I18nProvider'
import { IconMap } from './icons'

export function Header() {
  const { t } = useI18n()

  return (
    <header className="site-header">
      <div className="site-header__brand">
        <IconMap className="site-header__logo" />
        <div>
          <h1 className="site-header__title">{t('appName')}</h1>
          <p className="site-header__tagline">{t('tagline')}</p>
        </div>
      </div>
      <a
        className="site-header__contrib"
        href="https://github.com/JuanCarlosGP/eruvMap/issues/new?template=nuevo_eruv.yml"
        target="_blank"
        rel="noopener noreferrer"
      >
        {t('contribute')}
      </a>
    </header>
  )
}
