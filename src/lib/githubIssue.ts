const REPO_ISSUE_NEW =
  'https://github.com/JuanCarlosGP/eruvMap/issues/new'

const MAX_SAFE_URL = 7500
const MAX_GEOM_PARAM = 1200

export interface IssueFieldPayload {
  title: string
  name_en: string
  name_he?: string
  city: string
  country: string
  geometry_kind: string
  geometry_precision: string
  status: string
  source: string
  source_url: string
  license: string
  verified_at: string
  contact_url?: string
  note?: string
  geometria: string
  verification_photo?: string
  photo_distance_m?: string
  contribution_context?: string
}

export async function openPrefilledContributionIssue(
  fields: IssueFieldPayload,
): Promise<{ clipboardUsed: boolean }> {
  let geometria = fields.geometria
  let clipboardUsed = false

  const url = new URL(REPO_ISSUE_NEW)
  url.searchParams.set('template', 'nuevo_eruv.yml')
  url.searchParams.set('title', fields.title)

  const entries: [string, string][] = [
    ['name_en', fields.name_en],
    ['name_he', fields.name_he ?? ''],
    ['city', fields.city],
    ['country', fields.country],
    ['geometry_kind', fields.geometry_kind],
    ['geometry_precision', fields.geometry_precision],
    ['status', fields.status],
    ['source', fields.source],
    ['source_url', fields.source_url],
    ['license', fields.license],
    ['verified_at', fields.verified_at],
    ['contact_url', fields.contact_url ?? ''],
    ['note', fields.note ?? ''],
    ['verification_photo', fields.verification_photo ?? ''],
    ['photo_distance_m', fields.photo_distance_m ?? ''],
    ['contribution_context', fields.contribution_context ?? ''],
  ]

  if (geometria.length > MAX_GEOM_PARAM) {
    try {
      await navigator.clipboard.writeText(geometria)
      clipboardUsed = true
      geometria =
        '(GeoJSON copied to clipboard — paste into the Geometría field below.)'
    } catch {
      geometria = `${geometria.slice(0, MAX_GEOM_PARAM)}\n… [truncated — use Download GeoJSON]`
    }
  }
  entries.push(['geometria', geometria])

  for (const [key, value] of entries) {
    if (value) url.searchParams.set(key, value)
  }

  let href = url.toString()
  if (href.length > MAX_SAFE_URL) {
    try {
      await navigator.clipboard.writeText(fields.geometria)
      clipboardUsed = true
      url.searchParams.set(
        'geometria',
        '(GeoJSON copied to clipboard — paste into the Geometría field.)',
      )
      href = url.toString()
    } catch {
      /* open anyway */
    }
  }

  window.open(href, '_blank', 'noopener,noreferrer')
  return { clipboardUsed }
}
