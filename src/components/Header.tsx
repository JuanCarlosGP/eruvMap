import { useI18n } from '../i18n/I18nProvider'
import { IconMap } from './icons'

interface HeaderProps {
  onPropose: () => void
  contributeActive?: boolean
}

export function Header({ onPropose, contributeActive }: HeaderProps) {
  const { t } = useI18n()

  return (
    <header className="site-header">
      <div className="site-header__brand">
        <IconMap className="site-header__logo" />
        <h1 className="site-header__heading">
          <span className="site-header__title">{t('appName')}</span>
          <span className="site-header__taglines">
            <span className="site-header__tagline" lang="en">
              World map of eruvs
            </span>
            <span className="site-header__tagline" lang="he">
              מפה עולמית של עירובין
            </span>
          </span>
        </h1>
      </div>
      <button
        type="button"
        className={`site-header__contrib btn btn--secondary${contributeActive ? ' is-active' : ''}`}
        onClick={onPropose}
        aria-pressed={contributeActive}
      >
        {t('proposeEruv')}
      </button>
    </header>
  )
}
