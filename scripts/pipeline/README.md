# scripts/pipeline

The scripts actually used (copied from the working directory, only light path clean-up) to derive the perimeters in `data/eruvs.geojson`. Method and rules: [`docs/METHODOLOGY.md`](../../docs/METHODOLOGY.md). Source URLs + hashes: [`data/sources-raw/MANIFEST.md`](../../data/sources-raw/MANIFEST.md).

## Layout
| dir | content |
|---|---|
| `global/build.py` | global dataset (OSM/Overpass + official pages), points |
| `nyc/build_nyc.py` | Manhattan (raster colour segmentation) / Brooklyn (KML rings) |
| `us-points/build_us.py` | US representative points (no geometry copied) |
| `batch1`..`batch3` | Google My Maps KML / embedded GeoJSON -> ring closing -> simplification (`load.py`, `build1.py`, `mk*.py`) |
| `batch4`..`batch7` | rasters/PDFs without coordinates: SVG extraction (`svgx.py`, `fills.py`), road correlation (`reg.py`, `refine*.py`, `tilereg.py`), control points (`gcp.py`), per-eruv `*_reg*.py`/`*_poly.py`, final `integrate*.py` / `add6.py` |

Files named `*_reg*.py`, `*reg2/3/4`, `mon*`, `nh*` are per-eruv iterations; the last numbered/`*fin*`/`*poly*` script of an eruv is the one that produced the committed geometry.

## Use
```bash
python -m venv .venv && . .venv/bin/activate
pip install -r scripts/pipeline/requirements.txt
# Scripts expect a working directory that holds the downloaded sources (raw1/, raw2/, ...) and
# intermediate files (.pkl, OSM .json). They are NOT in the repo: re-download from the URLs in
# data/sources-raw/MANIFEST.md (check sha256), keep the original file names, then run from that dir.
python batch7/dl.py <s> <w> <n> <e> prefix 0.05   # OSM road tiles via Overpass (be polite: small bboxes, retries)
```
Paths such as `./` and `../eruvmap-repo` were `/workspace/...` originally; adjust to your checkout.

## Reproducibility limits
- **Raw inputs not shipped** (rights reserved by publishers): every script needs its sources downloaded first. Pages/maps may have changed since 2026-10-17.
- **Live OSM data**: Overpass results change over time, so georeferenced geometry will differ by metres.
- **Hand-picked control points / pixel coordinates** are hard-coded in several scripts (`slp.py`, `irv_poly.py`, `lj_poly.py`, `*_poly.py`); they depend on the exact raster downloaded (and on image scale when read from a viewer).
- **Intermediate pickles** (`*.pkl`) are produced by earlier scripts of the same eruv, in order; some were produced by interactive one-off commands that are not saved as scripts (batch 7 New Haven polygonization, St. Louis / Denver conversion, Princeton attempt).
- **Not reproducible as committed**: batch 6/7 `norj.py`/`noreg*.py` (Norfolk, discarded), `prinreg.py` (Princeton, discarded), `merreg.py` (Mercer Island, discarded) are kept as evidence of attempts that did not produce geometry.
- No credentials are used or stored. HTTP uses a descriptive User-Agent and respects robots.txt.
