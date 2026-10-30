import type { Theme } from '../theme/ThemeProvider'

export function mapboxStyleForTheme(theme: Theme): string {
  return theme === 'dark'
    ? 'mapbox://styles/mapbox/dark-v11'
    : 'mapbox://styles/mapbox/light-v11'
}

export const MAP_COLORS = {
  light: {
    line: '#0e6e68',
    lineWidth: 3,
    fill: 'rgba(14, 110, 104, 0.16)',
    outline: '#0a5853',
    cluster: '#0e6e68',
    clusterText: '#f7fbfc',
    clusterStroke: '#ffffff',
    markerFill: '#ffffff',
    markerStroke: '#0e6e68',
    accent: '#c4a15a',
    approxFill: 'rgba(196, 161, 90, 0.4)',
    approxStroke: '#8d5a12',
    approxPolyFill: 'rgba(14, 110, 104, 0.22)',
    unverifiedStroke: '#9a6b1f',
    unverifiedPolyFill: 'rgba(196, 161, 90, 0.14)',
  },
  dark: {
    line: '#5ee0d4',
    lineWidth: 3,
    fill: 'rgba(94, 224, 212, 0.16)',
    outline: '#8ceee5',
    cluster: '#14756e',
    clusterText: '#f3fffd',
    clusterStroke: '#e7f7f5',
    markerFill: '#06221f',
    markerStroke: '#7eefe4',
    accent: '#e7c98a',
    approxFill: 'rgba(231, 201, 138, 0.42)',
    approxStroke: '#e7c98a',
    approxPolyFill: 'rgba(94, 224, 212, 0.2)',
    unverifiedStroke: '#e7c98a',
    unverifiedPolyFill: 'rgba(231, 201, 138, 0.14)',
  },
} as const
