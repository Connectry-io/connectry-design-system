# Accessibility

**Contrast**, as WCAG ratios:

| Pair | Ratio | Use |
|---|---|---|
| ink on ground | 15.9 | anything |
| body on ground | 8.9 | running text |
| muted on ground | 6.1 | captions, small text |
| faint on ground | 3.5 | 12px caps labels only, never body |
| blue on white | 5.1 | accent words and links at 15px and up |
| blue on ground | 4.7 | the same |
| white on blue | 5.1 | the primary pill |
| blue-light on ink | 6.7 | film and dark photographs only |
| blue-light on white | 2.6 | never text |
| chart-comparison on white | 2.8 | never text |
| blue on the Film ground | 3.4 | a fill there, never text |
| body on the Film ground | 10.7 | running text in the dark register |
| muted on the Film ground | 7.4 | captions in the dark register |
| faint on the Film ground | 5.4 | caps labels in the dark register |

**Glass.** Computed at the tint floor (see **GlassContrast**): the light plate holds `ink` at
17.4 over white, 12.0 over light grey and 6.7 over mid grey, and fails below that (3.6 over dark,
1.7 over black). The dark plate holds 6.5 or better over everything down to black. So: the light
plate only where the picture behind the panel is mid grey or brighter, the dark plate everywhere
else and always for notifications. Text inside glass is 15px or larger; labels inside glass are
`muted`, never `faint`.

**Type on film.** White on the 42 percent scrim clears 4.5:1 over every plate in the set.

**Sizes.** Body 17, small 14, captions 13, labels 12 caps. Nothing smaller.

**Keyboard.** A focus ring on every interactive part: `2px solid blue`, offset 3px, through
`:focus-visible` only. Minimum touch target 44 by 44.

**Screen readers.** Film is `aria-hidden` with the line as real text beside it. Photographs
carry a plain alt: who, where, what they are doing. Decorative glass has none.

**Colour never carries meaning alone.** A state is always also a word: Done, Live, Selected.
An input error is a plain sentence in `muted` beneath the field, never red.

Reduced motion is honoured everywhere.
