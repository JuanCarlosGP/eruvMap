import type { Locale } from '../i18n/translations'

const COUNTRY_HE: Record<string, string> = {
  US: 'ארצות הברית',
  'United States': 'ארצות הברית',
  CA: 'קנדה',
  Israel: 'ישראל',
  'West Bank': 'יהודה ושומרון',
  'United Kingdom': 'הממלכה המאוחדת',
  'South Africa': 'דרום אפריקה',
  France: 'צרפת',
  Australia: 'אוסטרליה',
  Brazil: 'ברזיל',
  Hungary: 'הונגריה',
  Uruguay: 'אורוגוואי',
  Ukraine: 'אוקראינה',
  Belgium: 'בלגיה',
  Austria: 'אוסטריה',
  Mexico: 'מקסיקו',
  Argentina: 'ארגנטינה',
  Panama: 'פנמה',
  'Golan Heights': 'רמת הגולן',
  Spain: 'ספרד',
  Netherlands: 'הולנד',
  Chile: 'צ׳ילה',
  Gibraltar: 'גיברלטר',
  Portugal: 'פורטוגל',
  Switzerland: 'שווייץ',
  Italy: 'איטליה',
  Russia: 'רוסיה',
  'Hong Kong': 'הונג קונג',
  Slovakia: 'סלובקיה',
  Poland: 'פולין',
  Lithuania: 'ליטא',
  Belarus: 'בלארוס',
}

const COUNTRY_EN: Record<string, string> = {
  US: 'United States',
  'United States': 'United States',
  CA: 'Canada',
}

export function countryLabel(country: string, locale: Locale): string {
  if (locale === 'he') return COUNTRY_HE[country] ?? country
  return COUNTRY_EN[country] ?? country
}
