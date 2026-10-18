import { useI18n } from '../i18n/I18nProvider'
import { useTheme } from '../theme/ThemeProvider'
import type { EruvStatusFilter } from '../types/eruv'
import { IconLocate, IconMoon, IconSearch, IconSun } from './icons'

interface MapToolbarProps {
  searchQuery: string
  onSearchQueryChange: (q: string) => void
  onSearchSubmit: () => void
  searchBusy: boolean
  statusFilter: EruvStatusFilter
  onStatusFilterChange: (f: EruvStatusFilter) => void
  onNearMe: () => void
  nearMeBusy: boolean
}

export function MapToolbar({
  searchQuery,
  onSearchQueryChange,
  onSearchSubmit,
  searchBusy,
  statusFilter,
  onStatusFilterChange,
  onNearMe,
  nearMeBusy,
}: MapToolbarProps) {
  const { t, locale, setLocale } = useI18n()
  const { theme, toggleTheme } = useTheme()

  return (
    <div className="toolbar">
      <form
        className="search-field"
        role="search"
        onSubmit={(e) => {
          e.preventDefault()
          onSearchSubmit()
        }}
      >
        <IconSearch className="search-field__icon" />
        <input
          type="search"
          className="search-field__input"
          placeholder={t('searchPlaceholder')}
          aria-label={t('searchAria')}
          value={searchQuery}
          onChange={(e) => onSearchQueryChange(e.target.value)}
          autoComplete="off"
        />
        <button
          type="submit"
          className="btn btn--primary search-field__submit"
          disabled={searchBusy || !searchQuery.trim()}
        >
          {t('searchGo')}
        </button>
      </form>

      <div className="toolbar__row">
        <fieldset className="filter-group">
          <legend className="visually-hidden">{t('filterStatus')}</legend>
          <span className="filter-group__label" id="filter-status-label">
            {t('filterStatus')}
          </span>
          <div
            className="segmented"
            role="group"
            aria-labelledby="filter-status-label"
          >
            {(
              [
                ['all', t('filterAll')],
                ['active', t('statusActive')],
                ['unknown', t('statusUnknown')],
              ] as [EruvStatusFilter, string][]
            ).map(([value, label]) => (
              <button
                key={value}
                type="button"
                className={`segmented__btn${statusFilter === value ? ' is-active' : ''}`}
                aria-pressed={statusFilter === value}
                onClick={() => onStatusFilterChange(value)}
              >
                {label}
              </button>
            ))}
          </div>
        </fieldset>

        <div className="toolbar__actions">
          <button
            type="button"
            className="btn btn--secondary"
            onClick={onNearMe}
            disabled={nearMeBusy}
            aria-label={t('nearMeAria')}
          >
            <IconLocate />
            <span className="btn__label">{t('nearMe')}</span>
          </button>

          <div
            className="lang-switch"
            role="group"
            aria-label={t('languageGroup')}
          >
            <button
              type="button"
              className={`lang-switch__btn${locale === 'he' ? ' is-active' : ''}`}
              onClick={() => setLocale('he')}
              aria-pressed={locale === 'he'}
            >
              {t('langHe')}
            </button>
            <button
              type="button"
              className={`lang-switch__btn${locale === 'en' ? ' is-active' : ''}`}
              onClick={() => setLocale('en')}
              aria-pressed={locale === 'en'}
            >
              {t('langEn')}
            </button>
          </div>

          <button
            type="button"
            className="btn btn--ghost btn--icon"
            onClick={toggleTheme}
            aria-label={t('themeToggle')}
            title={theme === 'light' ? t('themeDark') : t('themeLight')}
          >
            {theme === 'light' ? <IconMoon /> : <IconSun />}
          </button>
        </div>
      </div>
    </div>
  )
}
