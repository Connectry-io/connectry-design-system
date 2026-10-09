# GlassContrast

The accessibility proof for glass: `ink` against each plate at its thinnest tint, over pictures
from white to black.

## Reading the table

Each cell mixes the plate's floor tint with the picture value behind it and reports the WCAG
ratio against `ink`. The light plate passes from mid grey up; below that the dark plate is used,
and it passes over everything down to black.

## Rules

- Light plate only where the picture behind the panel is mid grey or brighter; the dark plate
  on anything darker or busy.
- Text in glass is 15px or larger; labels are 12px caps in `muted`, never `faint`.
- Focus: 2px solid `blue`, offset 3px, `:focus-visible` only.
- Every state is also a word.
