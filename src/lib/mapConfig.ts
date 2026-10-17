import type { Theme } from '../theme/ThemeProvider'

export function mapboxStyleForTheme(theme: Theme): string {
  return theme === 'dark'
    ? 'mapbox://styles/mapbox/dark-v11'
    : 'mapbox://styles/mapbox/light-v11'
}

export const MAP_COLORS = {
  light: {
    line: '#2d4a6f',
    lineWidth: 3,
    fill: 'rgba(45, 74, 111, 0.12)',
    outline: '#1e3a5f',
    cluster: '#3d5a80',
    clusterText: '#faf6ef',
    accent: '#b8956a',
    approxFill: 'rgba(184, 149, 106, 0.35)',
    approxStroke: '#8a6d3b',
  },
  dark: {
    line: '#8eb4d9',
    lineWidth: 3,
    fill: 'rgba(142, 180, 217, 0.15)',
    outline: '#a8c8e8',
    cluster: '#5a7fa6',
    clusterText: '#0f1419',
    accent: '#d4b483',
    approxFill: 'rgba(212, 180, 131, 0.4)',
    approxStroke: '#e8c99a',
  },
} as const
