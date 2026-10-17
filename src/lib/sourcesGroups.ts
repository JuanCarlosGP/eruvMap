import type { Locale } from '../i18n/translations'
import { eruvDisplayName } from './eruvData'
import type { EruvFeature } from '../types/eruv'

export interface SourcesCityGroup {
  city: string
  features: EruvFeature[]
}

export interface SourcesStateGroup {
  state: string
  cities: SourcesCityGroup[]
}

export interface SourcesCountryGroup {
  country: string
  /** US: grouped by state; otherwise flat cities under country */
  states: SourcesStateGroup[] | null
  cities: SourcesCityGroup[]
}

function sortCityGroups(
  citiesMap: Map<string, EruvFeature[]>,
  collator: Intl.Collator,
  locale: Locale,
): SourcesCityGroup[] {
  const cityNames = [...citiesMap.keys()].sort((a, b) =>
    collator.compare(a, b),
  )
  return cityNames.map((city) => {
    const cityFeatures = [...citiesMap.get(city)!].sort((a, b) =>
      collator.compare(
        eruvDisplayName(a.properties, locale),
        eruvDisplayName(b.properties, locale),
      ),
    )
    return { city, features: cityFeatures }
  })
}

export function groupEruvsByPlace(
  features: EruvFeature[],
  locale: Locale,
): SourcesCountryGroup[] {
  const collator = new Intl.Collator(locale === 'he' ? 'he' : 'en', {
    sensitivity: 'base',
  })

  const byCountry = new Map<string, EruvFeature[]>()

  for (const feature of features) {
    const { country } = feature.properties
    const list = byCountry.get(country) ?? []
    list.push(feature)
    byCountry.set(country, list)
  }

  const countries = [...byCountry.keys()].sort((a, b) => collator.compare(a, b))

  return countries.map((country) => {
    const countryFeatures = byCountry.get(country)!

    if (country === 'US') {
      const byState = new Map<string, Map<string, EruvFeature[]>>()
      for (const feature of countryFeatures) {
        const state = feature.properties.state?.trim() || '—'
        let cities = byState.get(state)
        if (!cities) {
          cities = new Map()
          byState.set(state, cities)
        }
        const { city } = feature.properties
        const list = cities.get(city) ?? []
        list.push(feature)
        cities.set(city, list)
      }

      const stateCodes = [...byState.keys()].sort((a, b) =>
        collator.compare(a, b),
      )
      const states: SourcesStateGroup[] = stateCodes.map((state) => ({
        state,
        cities: sortCityGroups(byState.get(state)!, collator, locale),
      }))

      return { country, states, cities: [] }
    }

    const citiesMap = new Map<string, EruvFeature[]>()
    for (const feature of countryFeatures) {
      const { city } = feature.properties
      const list = citiesMap.get(city) ?? []
      list.push(feature)
      citiesMap.set(city, list)
    }

    return {
      country,
      states: null,
      cities: sortCityGroups(citiesMap, collator, locale),
    }
  })
}
