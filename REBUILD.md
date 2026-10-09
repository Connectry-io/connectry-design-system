# Rebuild in the Connectry organization

Run this in a Claude chat **signed in to the Connectry organization account**, with GitHub
connected and access to `Connectry-io/connectry-design-system`. Paste the prompt below as is.

---

## The prompt

```text
Rebuild our design system 1:1 from the GitHub repo Connectry-io/connectry-design-system.
This is a migration, not a redesign: every token, file, component preview, guideline and asset
must end up identical to the source. Do not edit, improve, rename, re-encode or "clean up"
anything. Follow these steps exactly and stop and tell me if any check fails.

0. Setup
   - Attach and clone Connectry-io/connectry-design-system (add the repo to this session).
   - Read README.md, REBUILD.md, asset-manifest.json and files-manifest.json first.
   - Verify the clone: every file in files-manifest.json and every repo_path in
     asset-manifest.json exists with the listed sha256. Report the counts (309 files, 206 assets).

1. Create the system
   - Artifact list scope "types". Use the "Design System" type.
   - If an artifact named "Connectry Design System" made from that type already exists in this
     org, stop and ask me before creating another.
   - Create ONE artifact from the type: title "Connectry Design System",
     auto_open "after_first_write", no files. Never pass type_url again.
   - Read the SKILL.md the type returns and follow it where it is stricter than this prompt.

2. Upload every asset to the new artifact's asset store (asset: true)
   - Upload all 206 entries of asset-manifest.json, the 150 under project/assets/ AND the
     56 under store-extra/, in manifest order, up to 25 per call (file_paths). A text file
     goes in a call of its own. Do not convert or compress anything.
   - Build new-ids.json mapping each old_blob_id to the new id from the upload result,
     matched by file path. Check: 206 entries, no duplicates, every upload's sha256 equals the
     manifest's.

3. Remap ids
   - python3 tools/remap_blobs.py new-ids.json --check, then without --check.
   - It rewrites the assetGroups blob ids in project/design-system.json and every /_blob/<id>
     reference in project/ text files. It must report 0 missing ids.
   - Grep project/ for any remaining old id from asset-manifest.json: must be zero hits.

4. Publish the files (root = the repo folder)
   - Publish every file in files-manifest.json where generated_by_page is false (305 files),
     at the same project/ path. Skip the 4 page-generated files (project/tokens.css,
     project/manifest.json, project/api/**): the page regenerates them.
   - Do NOT publish the asset binaries under project/assets/<Group>/ or store-extra/ as files;
     they live in the asset store from step 2. Text files under project/assets/ (README.md and
     notes/*.md) ARE published as files.
   - At most 256 paths per call. project/design-system.json goes LAST, alone, in the final call.
   - Before that last call, read the live index back once and keep any keys the page added.
     Change only lastChange: {"by":"Fabian","at":<now ISO-8601>,"via":"Claude",
     "note":"Migrated 1:1 from the source org (artifact version 1790233602-2fdc) via GitHub export."}.
     Keep title, source, upgraded, groups, assetGroups (remapped), libraries and every other key
     exactly as in the repo.
   - Pass no capabilities and no contract: the type supplies them.

5. Verify, then report
   - Artifact list scope "files": every published path from step 4 is present.
   - Artifact list scope "assets": 206 assets.
   - Read back a sample of 10 files (include project/tokens.json, project/README.md,
     project/design-system.json, two component previews with /_blob/ references): content equals
     the repo after remap.
   - Open the artifact. Check the cover, the Tokens section, the Logo, Imagery and Film asset
     groups (the product film plays), and the GlassPanel, WebHero, Deck and FilmLibrary previews
     render with their images and video.
   - Report: link, counts (files, assets), anything that differs from the source, and remind me
     to set it as the organization default in Claude Design settings.
```

---

## Why each rule is there

- **Assets get new ids.** The asset store issues a fresh id per upload, so the index and the 14
  files that reference `/_blob/<id>` must be rewritten. `remap_blobs.py` does that and nothing else.
- **Index last.** The type replaces the whole index on each write; writing it before the files
  can drop asset records.
- **Generated files skipped.** The page rebuilds `tokens.css`, `manifest.json` and the `api/`
  cards from the index and tokens on save.
- **store-extra included.** Nothing in the index uses them, but they are in the source store, so
  a 1:1 copy carries them.

## After the rebuild

1. Claude Design settings in the Connectry org: publish the system and set it as the default.
2. Update anything that links to the old URL (`EvxyuqoMw2sH7DBEavRvUh`): skills, the Connectry
   brain, docs.
3. Leave the old artifact in place until the new one is confirmed.
