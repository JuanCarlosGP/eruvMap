import { useCallback, useMemo, useState } from 'react'
import type { Geometry } from 'geojson'
import { useI18n } from '../i18n/I18nProvider'
import {
  buildContributionFeature,
  downloadProposalGeoJson,
  featureGeometryJson,
  type ContributeDrawTool,
} from '../lib/contribution'
import {
  haversineMeters,
  PHOTO_DISTANCE_THRESHOLD_M,
} from '../lib/distance'
import { openPrefilledContributionIssue } from '../lib/githubIssue'
import { geometryCenter } from '../lib/geometry'
import {
  readBrowserLocation,
  readPhotoGps,
  type PhotoLocationResult,
} from '../lib/photoLocation'
import type { ContributeFormValues } from '../types/contribute'
import { IconClose } from './icons'

interface ContributePanelProps {
  open: boolean
  onClose: () => void
  drawTool: ContributeDrawTool
  onDrawToolChange: (tool: ContributeDrawTool) => void
  geometry: Geometry | null
  onClearDraw: () => void
}

const EMPTY_FORM: ContributeFormValues = {
  name_en: '',
  name_he: '',
  city: '',
  country: '',
  source_url: '',
  contact_url: '',
  permission: false,
}

export function ContributePanel({
  open,
  onClose,
  drawTool,
  onDrawToolChange,
  geometry,
  onClearDraw,
}: ContributePanelProps) {
  const { t } = useI18n()
  const [form, setForm] = useState<ContributeFormValues>(EMPTY_FORM)
  const [photoLoc, setPhotoLoc] = useState<PhotoLocationResult | null>(null)
  const [photoBusy, setPhotoBusy] = useState(false)
  const [photoError, setPhotoError] = useState<string | null>(null)
  const [submitMsg, setSubmitMsg] = useState<string | null>(null)
  const [submitBusy, setSubmitBusy] = useState(false)

  const eruvCenter = useMemo(
    () => (geometry ? geometryCenter({ type: 'Feature', properties: {}, geometry }) : null),
    [geometry],
  )

  const photoDistanceM = useMemo(() => {
    if (!photoLoc || !eruvCenter) return null
    return haversineMeters(
      [photoLoc.lng, photoLoc.lat],
      eruvCenter,
    )
  }, [photoLoc, eruvCenter])

  const distanceWarning =
    photoDistanceM != null && photoDistanceM > PHOTO_DISTANCE_THRESHOLD_M

  const formValid =
    form.name_en.trim() &&
    form.city.trim() &&
    form.country.trim() &&
    form.source_url.trim() &&
    form.permission &&
    geometry

  const handlePhoto = useCallback(
    async (file: File | null) => {
      setPhotoError(null)
      setPhotoLoc(null)
      if (!file) return
      setPhotoBusy(true)
      try {
        const exif = await readPhotoGps(file)
        if (exif) {
          setPhotoLoc({ ...exif, source: 'exif' })
          return
        }
        const browser = await readBrowserLocation()
        setPhotoLoc(browser)
      } catch {
        setPhotoError(t('contributePhotoError'))
      } finally {
        setPhotoBusy(false)
      }
    },
    [t],
  )

  const handleSubmit = useCallback(async () => {
    if (!geometry || !formValid) return
    setSubmitBusy(true)
    setSubmitMsg(null)
    const feature = buildContributionFeature(form, geometry)
    const geometria = featureGeometryJson(geometry)
    const title = `[Eruv] ${form.name_en.trim()}`
    const verificationPhoto = photoLoc
      ? `${photoLoc.lat.toFixed(6)}, ${photoLoc.lng.toFixed(6)} (${photoLoc.source})`
      : ''
    const distanceStr =
      photoDistanceM != null ? String(Math.round(photoDistanceM)) : ''

    const { clipboardUsed } = await openPrefilledContributionIssue({
      title,
      name_en: form.name_en.trim(),
      name_he: form.name_he.trim(),
      city: form.city.trim(),
      country: form.country.trim(),
      geometry_kind: feature.properties.geometry_kind,
      geometry_precision: feature.properties.geometry_precision,
      status: 'unknown',
      source: form.source_url.trim(),
      source_url: form.source_url.trim(),
      license: feature.properties.license,
      verified_at: feature.properties.verified_at,
      contact_url: form.contact_url.trim(),
      note: feature.properties.note ?? '',
      geometria,
      verification_photo: verificationPhoto,
      photo_distance_m: distanceStr,
      contribution_context: t('contributeIssuePhotoReminder'),
    })

    setSubmitMsg(
      clipboardUsed ? t('contributeIssueClipboard') : t('contributeIssueOpened'),
    )
    setSubmitBusy(false)
  }, [form, formValid, geometry, photoLoc, photoDistanceM, t])

  const handleDownload = useCallback(() => {
    if (!geometry) return
    const feature = buildContributionFeature(form, geometry)
    downloadProposalGeoJson(feature)
  }, [form, geometry])

  const handleClose = () => {
    setForm(EMPTY_FORM)
    setPhotoLoc(null)
    setPhotoError(null)
    setSubmitMsg(null)
    onClearDraw()
    onClose()
  }

  if (!open) return null

  return (
    <aside
      className="detail-panel contribute-panel"
      role="dialog"
      aria-labelledby="contribute-title"
      aria-modal="false"
    >
      <header className="detail-panel__header">
        <h2 id="contribute-title" className="detail-panel__title">
          {t('contributeTitle')}
        </h2>
        <button
          type="button"
          className="btn btn--ghost btn--icon"
          onClick={handleClose}
          aria-label={t('closePanel')}
        >
          <IconClose />
        </button>
      </header>

      <p className="contribute-panel__intro">{t('contributeIntro')}</p>

      <fieldset className="contribute-fieldset">
        <legend>{t('contributeDrawLegend')}</legend>
        <div className="segmented" role="group" aria-label={t('contributeDrawLegend')}>
          {(
            [
              ['polygon', t('contributeDrawPolygon')],
              ['line', t('contributeDrawLine')],
              ['point', t('contributeDrawPoint')],
            ] as [ContributeDrawTool, string][]
          ).map(([tool, label]) => (
            <button
              key={tool}
              type="button"
              className={`segmented__btn${drawTool === tool ? ' is-active' : ''}`}
              aria-pressed={drawTool === tool}
              onClick={() => onDrawToolChange(tool)}
            >
              {label}
            </button>
          ))}
        </div>
        <button
          type="button"
          className="btn btn--secondary contribute-panel__clear"
          onClick={onClearDraw}
          disabled={!geometry}
        >
          {t('contributeClearDraw')}
        </button>
        <p className="contribute-panel__hint" role="status">
          {geometry ? t('contributeDrawReady') : t('contributeDrawHint')}
        </p>
      </fieldset>

      <form
        className="contribute-form"
        onSubmit={(e) => {
          e.preventDefault()
          handleSubmit()
        }}
      >
        <label className="contribute-label">
          {t('contributeNameEn')}
          <input
            required
            type="text"
            autoComplete="off"
            value={form.name_en}
            onChange={(e) => setForm((f) => ({ ...f, name_en: e.target.value }))}
          />
        </label>
        <label className="contribute-label">
          {t('contributeNameHe')}
          <input
            type="text"
            autoComplete="off"
            value={form.name_he}
            onChange={(e) => setForm((f) => ({ ...f, name_he: e.target.value }))}
          />
        </label>
        <label className="contribute-label">
          {t('city')}
          <input
            required
            type="text"
            value={form.city}
            onChange={(e) => setForm((f) => ({ ...f, city: e.target.value }))}
          />
        </label>
        <label className="contribute-label">
          {t('country')}
          <input
            required
            type="text"
            value={form.country}
            onChange={(e) => setForm((f) => ({ ...f, country: e.target.value }))}
          />
        </label>
        <label className="contribute-label">
          {t('contributeSourceUrl')}
          <input
            required
            type="url"
            inputMode="url"
            placeholder="https://"
            value={form.source_url}
            onChange={(e) =>
              setForm((f) => ({ ...f, source_url: e.target.value }))
            }
          />
        </label>
        <label className="contribute-label">
          {t('contact')} ({t('contributeOptional')})
          <input
            type="url"
            inputMode="url"
            placeholder="https://"
            value={form.contact_url}
            onChange={(e) =>
              setForm((f) => ({ ...f, contact_url: e.target.value }))
            }
          />
        </label>

        <div className="contribute-photo">
          <label className="contribute-label" htmlFor="contribute-photo-input">
            {t('contributePhotoLabel')}
          </label>
          <input
            id="contribute-photo-input"
            type="file"
            accept="image/*"
            capture="environment"
            onChange={(e) => handlePhoto(e.target.files?.[0] ?? null)}
            aria-describedby="contribute-photo-privacy"
          />
          <p id="contribute-photo-privacy" className="contribute-panel__privacy">
            {t('contributePhotoPrivacy')}
          </p>
          {photoBusy && (
            <p className="contribute-panel__hint" role="status">
              {t('contributePhotoReading')}
            </p>
          )}
          {photoError && (
            <p className="inline-message contribute-panel__warn" role="alert">
              {photoError}
            </p>
          )}
          {photoLoc && (
            <p className="contribute-panel__hint" role="status">
              {t('contributePhotoCoords', {
                lat: photoLoc.lat.toFixed(5),
                lng: photoLoc.lng.toFixed(5),
                source:
                  photoLoc.source === 'exif'
                    ? t('contributePhotoExif')
                    : t('contributePhotoBrowser'),
              })}
            </p>
          )}
          {photoDistanceM != null && eruvCenter && (
            <p
              className={
                distanceWarning
                  ? 'inline-message contribute-panel__warn'
                  : 'contribute-panel__hint'
              }
              role="status"
            >
              {t('contributePhotoDistance', {
                meters: Math.round(photoDistanceM),
              })}
              {distanceWarning && ` ${t('contributePhotoDistanceWarn')}`}
            </p>
          )}
        </div>

        <label className="contribute-check">
          <input
            type="checkbox"
            checked={form.permission}
            onChange={(e) =>
              setForm((f) => ({ ...f, permission: e.target.checked }))
            }
            required
          />
          <span>{t('contributePermission')}</span>
        </label>

        <div className="contribute-actions">
          <button
            type="submit"
            className="btn btn--primary"
            disabled={!formValid || submitBusy}
          >
            {t('contributeSubmit')}
          </button>
          <button
            type="button"
            className="btn btn--secondary"
            disabled={!geometry}
            onClick={handleDownload}
          >
            {t('contributeDownload')}
          </button>
        </div>
        {submitMsg && (
          <p className="contribute-panel__hint" role="status">{submitMsg}</p>
        )}
      </form>
    </aside>
  )
}
