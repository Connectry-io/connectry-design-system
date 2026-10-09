# Colour and type

## Colour

| Token | Light | Role |
|---|---|---|
| `blue` | `#4a6fa5` | primary action, one accent word, links, chart accent series |
| `blue-light` | `#7fa3d6` | accent word on film and dark photographs only |
| `ground` | `#f5f5f7` | page, slide and card background |
| `surface` | `#ffffff` | surfaces, doc previews, inputs |
| `ink` | `#1a1a1a` | headlines, text in glass, the mark |
| `body` | `#43444d` | running text |
| `muted` | `#5b5c66` | captions, small text, labels inside panels |
| `faint` | `#80818d` | 12px caps labels only |
| `hairline` | `rgba(0,0,0,.06)` | rules, borders, gridlines |
| `chart-comparison` | `#9a9ba6` | chart series only, then `chart-step-1`, `chart-step-2` |

The blue appears at most twice per surface: one primary action and one accent word. No
gradients as decoration (the photographic `scrim` is the exception), no purple, no navy fills,
no black backgrounds, no glow, no second accent.

The **Film** theme is the same brand in its dark register: `ground` becomes `#1a1a1a`, `ink`
becomes white, `blue-light` becomes usable as an accent word. It is the register of
photography, the product film and the endcard, not a dark mode for the product.

## Site dark

The website's edition, chosen in September 2026. It is a context, not a switch: the brand stays
light first on every other surface, and a light edition of the site exists as a known version.

| Token | Site dark | Role |
|---|---|---|
| `ground` | `#0e0f11` | warm graphite pages between film chapters, never pure black |
| `surface` | `#121316` | one lighter step for a section, blended in and out over 30 percent |
| `ink` | `#f3f3f5` | headlines, off-white rather than white |
| `body` | 74 percent `ink` | running text |
| `muted` | 60 percent | secondary text |
| `faint` | 45 percent | labels; the footer at 56 |
| `hairline` | 7 percent white | rules; a 40px white line at 50 percent above page headings |
| `blue-light` | `#7fa3d6` | the one blue on dark: eyebrows, accents, the menu action |

Luxury on dark comes from restraint: graphite, not black; layered surfaces instead of borders;
off-white type; one soft accent used rarely; a few thin white accents; gradients so faint they
are felt, not seen (a 2 percent blue pool at most).

## Type

Inter only, weights 400, 500, 600. Features `cv11` and `ss01` on. Nothing bold except the
wordmark.

| Style | Size | Weight | Line height | Tracking |
|---|---|---|---|---|
| film-headline | 5.6vw (107.5px at 1920) | 500 | 1.04 | -0.03em, one accent word in `blue-light`, second line at 0.42em, 400, white 78% |
| display | clamp(40px, 6.4vw, 84px) | 500 | 1.04 | -0.03em |
| headline | clamp(30px, 4vw, 48px) | 500 | 1.06 | -0.025em, breaks at 14ch |
| title | 20 to 26px | 500 | 1.2 | -0.015em |
| lead | 17 to 19px | 400 | 1.6 | 0, measure 56ch |
| body | 17px | 400 | 1.6 | 0, measure 64ch |
| small | 14px | 400 | 1.5 | 0 |
| caption | 13px | 400 | 1.45 | 0, measure 60ch |
| label | 12px | 500 | 1.2 | +0.08em, uppercase, the only uppercase in the system |

Headlines end with a full stop and carry one accent word at most. Numbers are tabular. Inter
is loaded from Google Fonts; no font binaries ship with this system.
