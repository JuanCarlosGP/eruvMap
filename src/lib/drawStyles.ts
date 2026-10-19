import type { Theme } from '../theme/ThemeProvider'
import { MAP_COLORS } from './mapConfig'

/** Mapbox Draw layers. Vertices stay visible in direct_select so a perimeter can be reshaped. */
export function drawStylesForTheme(theme: Theme) {
  const colors = MAP_COLORS[theme]
  const line = colors.line
  const vertex = theme === 'dark' ? '#e7f7f5' : '#ffffff'

  return [
    {
      id: 'gl-draw-polygon-fill',
      type: 'fill',
      filter: ['all', ['==', '$type', 'Polygon']],
      paint: {
        'fill-color': line,
        'fill-opacity': 0.16,
      },
    },
    {
      id: 'gl-draw-lines',
      type: 'line',
      filter: ['any', ['==', '$type', 'LineString'], ['==', '$type', 'Polygon']],
      layout: { 'line-cap': 'round', 'line-join': 'round' },
      paint: {
        'line-color': line,
        'line-width': 3,
      },
    },
    {
      id: 'gl-draw-point-outer',
      type: 'circle',
      filter: ['all', ['==', '$type', 'Point'], ['==', 'meta', 'feature']],
      paint: {
        'circle-radius': 7,
        'circle-color': vertex,
        'circle-stroke-width': 2,
        'circle-stroke-color': line,
      },
    },
    {
      id: 'gl-draw-point-inner',
      type: 'circle',
      filter: ['all', ['==', '$type', 'Point'], ['==', 'meta', 'feature']],
      paint: {
        'circle-radius': 3,
        'circle-color': line,
      },
    },
    {
      id: 'gl-draw-vertex-outer',
      type: 'circle',
      filter: [
        'all',
        ['==', '$type', 'Point'],
        ['==', 'meta', 'vertex'],
        ['!=', 'mode', 'simple_select'],
      ],
      paint: {
        'circle-radius': ['case', ['==', ['get', 'active'], 'true'], 8, 6],
        'circle-color': vertex,
        'circle-stroke-width': 2,
        'circle-stroke-color': line,
      },
    },
    {
      id: 'gl-draw-vertex-inner',
      type: 'circle',
      filter: [
        'all',
        ['==', '$type', 'Point'],
        ['==', 'meta', 'vertex'],
        ['!=', 'mode', 'simple_select'],
      ],
      paint: {
        'circle-radius': ['case', ['==', ['get', 'active'], 'true'], 4, 3],
        'circle-color': line,
      },
    },
    {
      id: 'gl-draw-midpoint',
      type: 'circle',
      filter: ['all', ['==', 'meta', 'midpoint']],
      paint: {
        'circle-radius': 4,
        'circle-color': line,
        'circle-opacity': 0.45,
      },
    },
  ]
}
