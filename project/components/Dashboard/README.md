# Dashboard

The home surface: the person's day, the applications ready to use and the connectors that feed
them, on one sheet of glass over the person's own picture.

## Structure

- **Nav glass.** 60px, `glass-nav` tint, 18px blur, hairline beneath. The ink lockup at 26px, the
  applications as tabs (active: `ink` 500 with a 2px `blue` rule), the person on the right.
- **Sheet.** One dark-plate panel, 48px from the plate's edges, 30 by 32 padding.
- **Head.** Date and time as `label`, the 44px headline with one accent word, the tag
  "One memory · 7 connected" with its live dot.
- **Today.** Hairline rows: time, line, source (`muted` 12px), state word. At most five; the one
  that needs the person carries the blue state "Needs you".
- **Ready to use.** Six wells in two columns: name and state, one line, one meta line.
- **Connected.** Connector pills (a grey square for the product's mark, the kind of thing it
  is, a blue dot when on) and, at the end, "Only what you choose to share leaves this sheet."

## Rules

One sheet, never cards floating on cards. Connectors are named by kind (Mail, Calendar, Bank),
never by vendor on anything public. Money shows what is due and drafted, never a balance.
