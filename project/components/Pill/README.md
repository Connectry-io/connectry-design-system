# Pill

The system's only button shape. 12 by 20 padding, `radius-pill`, 15px at weight 500, minimum
touch target 44 by 44.

- **Primary** — `blue` with white text, hover `blue-hover`. One primary per view, and never
  inside a glass message panel.
- **Secondary** — `ink` with white text, for the rare second action.
- **Quiet** — a hairline border and `ink` text; hover fills `surface`.
- **Glass** — the glass material with `ink` text, on photography or blooms only. See
  GlassPanel.

## States

Rest. Hover: 160ms `ease`, colour or fill only, nothing moves, grows or glows. Focus:
`2px solid blue`, offset 3px, `:focus-visible` only. Disabled: `opacity-disabled`, pointer
events off, the same colour, never a grey substitute.

## Copy

Two or three words that say what happens. No emoji. No exclamation mark.
