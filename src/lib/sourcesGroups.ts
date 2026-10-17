import type { Locale } from '../i18n/translations'
import { eruvDisplayName } from './eruvData'
import type { EruvFeature } from '../types/eruv'

export interface SourcesCityGroup {
  city: string
  features: EruvFeature[]
}

export interface SourcesCountryGroup {
  country: string
  cities: SourcesCityGroup[]
}

export function groupEruvsByPlace(
  features: EruvFeature[],
  locale: Locale,
): SourcesCountryGroup[] {
  const collator = new Intl.Collator(locale === 'he' ? 'he' : 'en', {
    sensitivity: 'base',
  })

  const byCountry = new Map<string, Map<string, EruvFeature[]>>()

  for (const feature of features) {
    const { country, city } = feature.properties
    let cities = byCountry.get(country)
    if (!cities) {
      cities = new Map()
      byCountry.set(country, cities)
    }
    const list = cities.get(city) ?? []
    list.push(feature)
    cities.set(city, list)
  }

  const countries = [...byCountry.keys()].sort((a, b) => collator.compare(a, b))

  return countries.map((country) => {
    const citiesMap = byCountry.get(country)!
    const cityNames = [...citiesMap.keys()].sort((a, b) =>
      collator.compare(a, b),
    )
    const cities: SourcesCityGroup[] = cityNames.map((city) => {
      const cityFeatures = [...citiesMap.get(city)!].sort((a, b) =>
        collator.compare(
          eruvDisplayName(a.properties, locale),
          eruvDisplayName(b.properties, locale),
        ),
      )
      return { city, features: cityFeatures }
    })
    return { country, cities }
  })
}
