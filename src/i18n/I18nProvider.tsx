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

function applyDocumentLocale(locale: Locale) {
  const lang = locale === 'he' ? 'he' : 'en'
  document.documentElement.lang = lang
  document.documentElement.dir = locale === 'he' ? 'rtl' : 'ltr'
  const copy = translations[locale]
  document.title = `${copy.appName} — ${copy.tagline}`
}

function readStoredLocale(): Locale {
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
