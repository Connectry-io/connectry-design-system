# Connectry Design System (v2.1) — full export

A complete, byte-exact export of the **Connectry Design System** Claude artifact, so it can be
rebuilt 1:1 in another Claude organization.

Source: `https://claude.ai/artifact/EvxyuqoMw2sH7DBEavRvUh`, version `1790233602-2fdc`,
Design System type contract `0.2.47`. Exported 2026-10-09.

## What is in here

| Path | What | Count |
|---|---|---|
| `project/` | Every published file of the system: README brand book, 14 guideline sections, `tokens.json`, `design-system.json` (the index), 70 components (README + live preview each), notes | 309 files |
| `project/assets/<Group>/` | Every asset the index names, restored to its real filename: Logo, Imagery, Circles, Film (incl. the 75s product film and the hero film), Social, Slides, Icons, Glass | 150 files |
| `project/media/` | The published media copies the previews load by relative path (logos, icons, stills, 10 clips, slides, social cards) | included above |
| `store-extra/` | The 56 asset-store uploads the index does not name (earlier logo uploads, alternate encodes, crops). Kept for completeness, named by original id | 56 files |
| `asset-manifest.json` | All 206 store assets: old id, repo path, type, size, sha256, group, whether files reference it by URL | 206 entries |
| `files-manifest.json` | sha256 of every published `project/` file (pre-remap), and which are page-generated | 309 entries |
| `tools/remap_blobs.py` | Rewrites old asset ids to the new ones after re-upload | |
| `reference/type/` | The Design System type's own `SKILL.md` and page shell at export time (reference only; the type supplies these in the new org) | 2 files |
| `docs/connectry-brand-guidelines-2.1.pdf` | The brand guidelines as one PDF (120 pages, 16:9): brand book, every guideline section in full, all tokens, logo, imagery, film, slides, social and all 66 components as rendered | 1 file |
| `tools/render_previews.py`, `tools/build_brand_pdf.py` | Rebuild the PDF from `project/` after any change: render previews, then build | |
| `REBUILD.md` | The step-by-step rebuild and the prompt to paste into Claude | |

Every byte was checked against the artifact's sha256 on export: 206 of 206 assets, 309 of 309 files.

## Not carried (cannot be exported)

- Comment threads on the artifact.
- Rows in the artifact's shared database.
- Version history and the old URL.
- The org-default setting (set it again in the new org).

## Rebuild

See [REBUILD.md](REBUILD.md).
