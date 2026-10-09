#!/usr/bin/env python3
"""Remap asset-store ids after re-uploading the assets into a new Design System artifact.

Usage:
  python3 tools/remap_blobs.py new-ids.json [--check]

new-ids.json maps every OLD blob id (see asset-manifest.json) to the NEW id the
upload returned in the target artifact:  {"<old 32-hex>": "<new 32-hex>", ...}

What it rewrites, in place:
  * project/design-system.json  -> assetGroups.<Group>.files.<key>.blob
  * every text file under project/ (.html .md .json .css .js .txt)
    -> each "/_blob/<old>" becomes "/_blob/<new>" (also bare ids in "read <id>" lines)

--check only reports what would change and exits non-zero if any referenced
old id has no new id.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEXT = {".html", ".md", ".json", ".css", ".js", ".txt"}


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    check = "--check" in sys.argv
    mapping = json.loads(pathlib.Path(sys.argv[1]).read_text())
    manifest = json.loads((ROOT / "asset-manifest.json").read_text())
    required = {a["old_blob_id"] for a in manifest["assets"]
                if a["index_group"] or a["referenced_by_url_in_files"]}
    missing = sorted(required - mapping.keys())
    if missing:
        print(f"MISSING new ids for {len(missing)} required assets:")
        for m in missing:
            print("  ", m)
        if check:
            sys.exit(1)

    pat = re.compile(r"\b(" + "|".join(map(re.escape, mapping)) + r")\b") if mapping else None
    changed = 0
    for p in sorted((ROOT / "project").rglob("*")):
        if not p.is_file() or p.suffix.lower() not in TEXT or pat is None:
            continue
        s = p.read_text(encoding="utf-8", errors="surrogateescape")
        n = pat.sub(lambda m: mapping[m.group(1)], s)
        if n != s:
            changed += 1
            hits = len(pat.findall(s))
            print(f"{'would update' if check else 'updated'} {p.relative_to(ROOT)} ({hits} ids)")
            if not check:
                p.write_text(n, encoding="utf-8", errors="surrogateescape")
    print(f"{changed} files {'to change' if check else 'changed'}; "
          f"{len(mapping)} ids mapped; {len(missing)} required ids missing")
    if missing:
        sys.exit(1)


if __name__ == "__main__":
    main()
