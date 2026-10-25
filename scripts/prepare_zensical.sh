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
mkdir -p docs/javascripts docs/stylesheets
cp "$src/js/glightbox.min.js" docs/javascripts/
cp "$src/css/glightbox.min.css" docs/stylesheets/
grep -q GLightbox docs/javascripts/glightbox.min.js

# Target the comment marker placed in mkdocs.yml
marker='# --ZENSICAL_CSS_MARKER--'
[ "$(grep -cF "$marker" mkdocs.yml)" -eq 1 ]

# The marker must end the extra_css list: the next non-blank line must start at column 0
next_line=$(awk -v m="$marker" 'f && NF {print; exit} $0==m {f=1}' mkdocs.yml)
if [[ "$next_line" =~ ^[[:space:]] ]]; then
  echo "mkdocs.yml: $marker must be the last entry of extra_css (found an indented line after it)" >&2
  exit 1
fi

# The generated config adds extra_javascript, so mkdocs.yml must not already define it
if grep -q '^extra_javascript:' mkdocs.yml; then
  echo "mkdocs.yml already defines extra_javascript; the generated config would duplicate it" >&2
  exit 1
fi

# Use awk to inject the CSS and the extra_javascript block right before the comment marker
awk -v m="$marker" '$0==m {
    print "  - stylesheets/glightbox.min.css"
    print ""
    print "extra_javascript:"
    print "  - javascripts/glightbox.min.js"
    print m
    next
} {print}' mkdocs.yml > mkdocs.zensical.yml
