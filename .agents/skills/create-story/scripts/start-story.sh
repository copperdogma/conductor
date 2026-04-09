#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: start-story.sh <slug> [priority]" >&2
  exit 1
fi

SLUG="$1"
PRIORITY="${2:-Medium}"

if [[ ! "$SLUG" =~ ^[a-z0-9]([a-z0-9-]*[a-z0-9])?$ ]]; then
  echo "Invalid slug: $SLUG" >&2
  exit 1
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../../" && pwd)"
TEMPLATE="$ROOT/.agents/skills/create-story/templates/story.md"
STORIES_DIR="$ROOT/docs/stories"

mkdir -p "$STORIES_DIR"

next_num=1
if ls "$STORIES_DIR"/story-*.md >/dev/null 2>&1; then
  last="$(ls "$STORIES_DIR"/story-*.md | sed 's/.*story-\([0-9][0-9]*\).*/\1/' | sort -n | tail -1)"
  next_num=$((10#$last + 1))
fi

padded="$(printf "%03d" "$next_num")"
out="$STORIES_DIR/story-${padded}-${SLUG}.md"

sed "s/NNN/$padded/g; s/TITLE/${SLUG}/g; s/PRIORITY/${PRIORITY}/g" "$TEMPLATE" > "$out"
echo "$out"

