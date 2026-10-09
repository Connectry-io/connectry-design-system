# GlassPanel

The one glass primitive every panel in the system is built from: a convex lens over a photograph
or the blooms, never a blur.

## Anatomy

- **Surface.** `glass-tint-top` 40 percent to `glass-tint-bottom` 26 percent, white, vertical. The
  dark plate (`glass-dark-top` 74 to `glass-dark-bottom` 62) whenever the picture behind sits below
  mid grey.
- **Lens.** `backdrop-filter: url(#lens) blur(2px) saturate(1.7) brightness(1.04)`, with the plain
  chain declared first. The `#lens` filter is inlined once per page (see the Glass section).
- **Rim.** 1px, white at the top, 12 percent at the sides, 28 at the bottom, drawn by a masked
  `::before`. `shadow-glass` over a photograph, `shadow-glass-ground` on the ground.
- **On the ground.** The same tint and rim over the blooms, without the `#lens` reference: on a
  flat grey there is nothing to bend and the map only shows its own edges.
- **Radius.** `radius-panel` 16. Inner wells `radius-card` 12, doc previews `radius-doc` 8.

## Inside a panel

A head row (`label` in `muted`, a state word on the right with its dot), one line in 15px `ink`
or a 24px title, then hairline rows, a well, a doc preview or the members row. Text inside glass
is 15px or larger except labels and captions.

## Do and never

Do sit it on the open third of the picture. Never on a face, never glass on glass, never a flat
frosted card, never empty, never the logo inside it, never a gradient or glow inside it.
