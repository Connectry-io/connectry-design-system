# MorningWidget

The morning, as the site hero shows it: one sheet of glass on the open third of a photograph,
the day's three things and the applications ready to use.

## Structure

- **Head.** `label` with the day and time, the state word Live with its dot in `blue`.
- **Title.** 26px, one accent word, full stop: "Three things need you today."
- **Rows.** Time (13px, tabular), the line (15px `ink`), a source line in `muted` 12px, the state
  word on the right: Drafted, Done, Live. Three rows, never more.
- **Applications.** Three wells, name and one line each.
- **Foot.** "One memory · 7 connected" and "Nothing to set up" in `muted`.

## Provide

A photograph with an open third (Imagery 03, 15, 18), the date, three rows with source and state,
three applications.

## Motion

The panel arrives once (1.2s, `cubic-bezier(.2,.7,.2,1)`), rows land at 0.9, 1.25 and 1.6s,
applications at 2.0s. Nothing loops. Reduced motion shows it complete.

## Never

On a face, more than three rows, a button inside it, a vendor or assistant name.
