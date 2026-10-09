# Chart

Charts are native: drawn in the surface they sit on, never an image, never a screenshot.

- **Colour.** `chart-accent` is the one series that matters. `chart-comparison`, then
  `chart-step-1` and `chart-step-2` for anything further from the point. `chart-comparison` on
  white is 2.8:1, so it is never used for text.
- **Gridlines.** `chart-grid`, hairline, and only where a reader has to compare. One axis, the
  baseline in `ink`.
- **Labels.** The value sits on the mark, in 13px weight 500, tabular. Axis labels in `faint`
  at 12px. A source line at the foot in `faint`.
- **No** legend where two series can be labelled directly, no 3D, no gradients, no drop
  shadows, no doughnut with a number in the hole.

## The nine chart layouts on slides

Column, line, bar before and after, part to whole, timeline, comparison, and the three in the
proof family. All native and editable in the deck: a chart that cannot be corrected in the
room is not shipped.

## Colour never alone

Where two series must be told apart in print or by a colour-blind reader, they differ in
lightness, not hue, and the series is labelled directly.
