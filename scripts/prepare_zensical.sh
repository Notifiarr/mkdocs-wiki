#!/usr/bin/env bash
# Copy pinned GLightbox into a Zensical config. Pass --check after the build.
set -euo pipefail
cd "$(dirname "$0")/.."

if [ "${1:-}" = --check ]; then
  found=0
  while IFS= read -r -d '' page; do
    grep -q 'bundle\.' "$page" || continue
    found=1
    grep -q 'unpkg.com/glightbox' "$page" && echo "$page references unpkg glightbox" >&2 && exit 1
    grep -q 'glightbox.min.css' "$page" || { echo "$page missing glightbox css" >&2; exit 1; }
    grep -q 'glightbox.min.js' "$page" || { echo "$page missing glightbox script" >&2; exit 1; }
  done < <(find "${2:-site}" -name '*.html' -print0)
  [ "$found" -eq 1 ]
  exit 0
fi

src=node_modules/glightbox/dist
mkdir -p docs/javascripts
cp "$src/js/glightbox.min.js" docs/javascripts/
cp "$src/css/glightbox.min.css" docs/stylesheets/
grep -q GLightbox docs/javascripts/glightbox.min.js
marker='  - stylesheets/github-permalink-style.css'
[ "$(grep -cF "$marker" mkdocs.yml)" -eq 1 ]
awk -v m="$marker" '$0==m {print; print "  - stylesheets/glightbox.min.css\n\nextra_javascript:\n  - javascripts/glightbox.min.js"; next} {print}' mkdocs.yml > mkdocs.zensical.yml
