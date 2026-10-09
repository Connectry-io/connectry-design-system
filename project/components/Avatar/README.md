# Avatar

A `blue` circle with white initials at weight 500. Sizes 24, 32 and 40.

**Always a circle.** Fixed width and height, `flex: 0 0 auto`, `aspect-ratio: 1 / 1`, never
squeezed into an ellipse by its row. This was the single most common break in earlier versions
and it is on the ship checklist.

## Members row

Initials overlap by 6px with a 2px white ring, then "n people" in `muted`, all on one line.
It appears in the circle panel and nowhere else without a reason. A circle panel never exposes
a member's private memory: the row says who is in the circle, not what they know.

## Photographs

Founder and member photographs are not used in place of initials until they are shot in the
system grade. Initials are the default, not a fallback.
