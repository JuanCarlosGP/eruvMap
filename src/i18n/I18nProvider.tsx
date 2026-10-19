import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from 'react'
import {
  translations,
  type Locale,
  type TranslationKey,
} from './translations'

const STORAGE_KEY = 'eruvmap-locale'

function localeFromUrl(): Locale | null {
  const value = new URLSearchParams(window.location.search).get('lang')
  if (value === 'he' || value === 'en') return value
  return null
}

function applyDocumentLocale(locale: Locale) {
  const lang = locale === 'he' ? 'he' : 'en'
  document.documentElement.lang = lang
  document.documentElement.dir = locale === 'he' ? 'rtl' : 'ltr'
  document.title = 'World map of eruvs, boundaries and sources | Eruvpedia'
  const canonical =
    locale === 'en' ? 'https://eruvpedia.com/?lang=en' : 'https://eruvpedia.com/'
  document
    .querySelector('link[rel="canonical"]')
    ?.setAttribute('href', canonical)
  const url = new URL(window.location.href)
  if (locale === 'en') url.searchParams.set('lang', 'en')
  else url.searchParams.delete('lang')
  const next = `${url.pathname}${url.search}${url.hash}`
  const current = `${window.location.pathname}${window.location.search}${window.location.hash}`
  if (next !== current) history.replaceState(null, '', next)
}

function readStoredLocale(): Locale {
  const fromUrl = localeFromUrl()
  if (fromUrl) return fromUrl
  try {
    const v = localStorage.getItem(STORAGE_KEY)
    if (v === 'he' || v === 'en') return v
    if (v === 'es') return 'he'
  } catch {
    /* ignore */
  }
  return 'he'
}

interface I18nContextValue {
  locale: Locale
  setLocale: (locale: Locale) => void
  t: (key: TranslationKey, vars?: Record<string, string | number>) => string
}

const I18nContext = createContext<I18nContextValue | null>(null)

export function I18nProvider({ children }: { children: ReactNode }) {
  const [locale, setLocaleState] = useState<Locale>(readStoredLocale)

  useEffect(() => {
    applyDocumentLocale(locale)
  }, [locale])

  const setLocale = useCallback((next: Locale) => {
    setLocaleState(next)
    try {
      localStorage.setItem(STORAGE_KEY, next)
    } catch {
      /* ignore */
    }
    applyDocumentLocale(next)
  }, [])

  const t = useCallback(
    (key: TranslationKey, vars?: Record<string, string | number>) => {
      let text: string = translations[locale][key] ?? translations.he[key]
      if (vars) {
        for (const [k, v] of Object.entries(vars)) {
          text = text.replace(`{{${k}}}`, String(v))
        }
      }
      return text
    },
    [locale],
  )

  const value = useMemo(
    () => ({ locale, setLocale, t }),
    [locale, setLocale, t],
  )

  return <I18nContext.Provider value={value}>{children}</I18nContext.Provider>
}

export function useI18n() {
  const ctx = useContext(I18nContext)
  if (!ctx) throw new Error('useI18n must be used within I18nProvider')
  return ctx
}
