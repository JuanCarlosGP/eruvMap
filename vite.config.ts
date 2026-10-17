import react from '@vitejs/plugin-react'
import { readFileSync } from 'node:fs'
import { defineConfig, type Plugin } from 'vite'

function geojsonPlugin(): Plugin {
  return {
    name: 'geojson-loader',
    load(id) {
      if (id.endsWith('.geojson')) {
        const json = readFileSync(id, 'utf-8')
        return `export default ${json}`
      }
    },
  }
}

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), geojsonPlugin()],
})
