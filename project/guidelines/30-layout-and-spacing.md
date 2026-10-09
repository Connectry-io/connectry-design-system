# Layout and spacing

Three measures build everything. The **gutter**, `max(20px, 6.9vw)`, sets the edge on the
site, the slide safe area and the social cards (6.5cqw, the nearest step). The **left rail**
is where the line lives, 5.6vw from the bottom of a film frame. The **open third** of a
photograph is where glass may sit.

Spacing is a 4px base, `space-1` through `space-30`: 4 (hairline gaps, chip dot) · 8 (inside
chips, between initials) · 12 (label to line, caption to stage) · 16 (inside a doc preview) ·
20 (between stages) · 24 (panel padding, grid gap) · 32 (between component rows) · 48 (section
head to content) · 72 (between sections, phone) · 120 (between sections, desktop). Nothing is
placed on a number that is not on the scale.

Radii on the website: one family, `radius-frame` 28 for film frames, `radius-glass` 19 for the
bar, cards and fields, `radius-inner` 11 for buttons and tiles inside them. Nothing on the site
is a pill.

Radii elsewhere: `radius-panel` 16 panels · `radius-card` 12 stages, surfaces, component cards and
inputs · `radius-tile` 10 tiles · `radius-doc` 8 doc previews · `radius-pill` 999 pills, chips
and toggles. Tightened in v1.6: glass reads as a slab, not a pebble.

Breakpoints: 1000px stage grids to one column · 900px section heads stack · 640px all grids to
one column, display size 7.5vw.

Panel widths: 16:9 frame 34 to 48 percent · 4:5 card 44 to 52 percent · 1:1 card up to 60
percent · 340px maximum on the site. Copy is shortened before a panel is widened.

Z order on a photograph: photograph, `scrim`, glass, type. The scrim is 42 percent black
rising from the bottom over 55 percent of the height. Nothing sits above type.

**Phones.** One left-aligned column on a 20px gutter; headings, text, glass cards and rows share
one left edge; only the final film chapter is centred. Circles become rows, sources a two-column
grid, glass cards full width inside or under their film. Nothing ever scrolls sideways.

Section heads are a two-column split, headline left and lead right. Lists are hairline rows,
not cards. Column counts are chosen so every row is full.
