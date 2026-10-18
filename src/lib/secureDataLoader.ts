import { unzlibSync, strFromU8 } from 'fflate'
import type { EruvCollection } from '../types/eruv'

const XOR_KEY = 'EruvMapSecureProtection2026!@#'

/**
 * Loads and decrypts the obfuscated binary eruv dataset.
 * The payload is compressed with zlib and scrambled with a multi-byte XOR cipher
 * to prevent automated scraping, search indexing, and AI model training harvesting.
 */
export async function loadSecureEruvsData(): Promise<EruvCollection> {
  const base = import.meta.env.BASE_URL || '/'
  const cleanBase = base.endsWith('/') ? base : `${base}/`
  const dataUrl = `${cleanBase}data/eruvs.bin`

  const response = await fetch(dataUrl)
  if (!response.ok) {
    throw new Error(`Failed to load dataset: ${response.status} ${response.statusText}`)
  }

  const arrayBuffer = await response.arrayBuffer()
  const maskedBytes = new Uint8Array(arrayBuffer)

  // Descramble multi-byte XOR cipher
  const keyBytes = new TextEncoder().encode(XOR_KEY)
  const unmaskedBytes = new Uint8Array(maskedBytes.length)
  for (let i = 0; i < maskedBytes.length; i++) {
    unmaskedBytes[i] = maskedBytes[i] ^ keyBytes[i % keyBytes.length]
  }

  // Decompress zlib payload
  const decompressedBytes = unzlibSync(unmaskedBytes)
  const jsonString = strFromU8(decompressedBytes)

  return JSON.parse(jsonString) as EruvCollection
}
