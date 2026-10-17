import type { Locale } from '../i18n/translations'

/** Código de idioma para Mapbox GL (etiquetas de mapa) y Geocoding API. */
export function mapboxLanguage(locale: Locale): string {
  return locale === 'he' ? 'he' : 'en'
}
