import react from '@vitejs/plugin-react'
import { copyFileSync, existsSync, readFileSync } from 'node:fs'
import { join } from 'node:path'
import { defineConfig, type Plugin } from 'vite'

import { cloudflare } from "@cloudflare/vite-plugin";

function normalizeBase(raw: string | undefined): string {
  const value = raw?.trim()
  if (!value || value === '/') return '/'
  return value.endsWith('/') ? value : `${value}/`
}

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

/** GitHub Pages sirve 404.html en rutas desconocidas; duplicar index para SPA. */
function githubPages404Plugin(outDir: string): Plugin {
  return {
    name: 'github-pages-404',
    apply: 'build',
    closeBundle() {
      const indexPath = join(outDir, 'index.html')
      if (!existsSync(indexPath)) return
      copyFileSync(indexPath, join(outDir, '404.html'))
    },
  }
}

const base = normalizeBase(process.env.VITE_BASE_PATH ?? '/')
const githubPages = process.env.GITHUB_PAGES === 'true'

// https://vite.dev/config/
export default defineConfig({
  base,
  plugins: [
    react(),
    geojsonPlugin(),
    githubPages404Plugin('dist'),
    ...(githubPages ? [] : [cloudflare()]),
  ],
})
