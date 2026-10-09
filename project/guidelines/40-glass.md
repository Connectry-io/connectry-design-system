# Glass

Connectry glass is a convex lens, not a blur. The picture behind a panel bends, strongest at
the rim and almost flat in the middle. Only 2px of blur, so the photograph stays sharp and
slightly richer through it.

**Refraction.** The SVG filter `#lens`, an `feImage` displacement map (convex, rim weighted)
driving `feDisplacementMap` at scale 42. Inline it once per page that uses glass. The map is
`lens-map.png` in the **Glass** asset group; reference it by its asset URL:

```html
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <filter id="lens" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
    <feImage href="/_blob/8307ef4bba30e82def04ad8320eaf6fb" x="0" y="0" width="100%" height="100%" preserveAspectRatio="none" result="map"/>
    <feDisplacementMap in="SourceGraphic" in2="map" scale="42" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
</defs></svg>
```

Filter chain: `backdrop-filter: url(#lens) blur(2px) saturate(1.7) brightness(1.04)`, with a
plain `blur(2px) saturate(1.7) brightness(1.04)` declared first for engines that do not take
a filter reference. On the grey ground (`glass--ground`) the lens reference is left out: there
is nothing to bend, and the map would only draw its own edges on flat grey.

**Which plate.** The light plate over pictures at mid grey or brighter where the panel sits; the
dark plate over anything darker or busy, and always for notifications. **GlassContrast** has the
computed ratios.

**Tint.** White, vertical, `glass-tint-top` 40 percent to `glass-tint-bottom` 26. Dark plates
74 to 62. Never below 26: that floor is what keeps `ink` above 4.5:1 inside a panel.

**Rim.** 1px lit from above, white at the top fading to 12 percent at the sides and 28 at the
bottom, drawn with a masked pseudo element; an inset highlight along the top and a faint inset
shadow along the bottom. `shadow-glass` over a photograph, `shadow-glass-ground` on the
ground.

**Arrival.** 1.2s: rises 14px and resolves from 10px of blur, then one diagonal highlight
sweeps across in 1.1s. Nothing loops, nothing shimmers.

**Blooms.** On the grey ground, two large radial blooms, `bloom-blue` at 18 percent and
`bloom-warm` at 15, sit behind the layout and drift over 70 to 90s so the glass has light to
bend.

**Inside a panel.** A head row (`label` in `muted` 12px caps, a state word with its dot on the
right: Live, Done, Shared, Kept, Drafted, Needs you), then one of: a line in 15px `ink`, a title
at 20 to 26px, hairline rows (time, line, source, state), a well (white 55 percent, radius 12)
for the reason or an application, a doc preview, the members row, tags for sources. Foot: text
links only, never a button inside a message panel.

**The panels.** **MorningWidget** (the day) · **CircleCard** (a circle speaking) ·
**ReplyPanel** (the answer beneath the ask, with its reason and sources) ·
**NotificationGlass** (lock screen and desktop) · **ShareToCircle** (the choice to share and its
after-state) · **MemoryCard** (one kept fact, why, from where, seen by whom) · **WaitlistForm** ·
the Dashboard sheet. Earlier names: message panel (a time as the label, one line, no button; where something was
built, a doc preview) · circle panel (circle name and time, one line, the members row) ·
legacy panel (the circle and its year, one line, a doc preview of what was kept) · content
panel on the ground · dark plate for legibility over dark photographs · the nav variant
(square, 18px blur, 62 percent tint, hairline beneath).

**On the website.** The hero bar and answer card use `radius-glass` 19 through every state, 74
percent white with the lens; the band of light passes once after each change. Glass over film
sits inside its frame, near the bottom, with a soft shadow beneath; it never hangs over an edge.
The menu and the contact dialog are real frosted glass: 62 percent light with a 30px blur and a
top highlight on the light edition, `glass-dark-panel` (58 percent graphite) with off-white type
on the dark edition. The scrolled nav is `nav-glass-dark` or 74 percent `ground`.

**Never.** Flat frosted cards, glass on glass, glass as a background, gradients or glow inside
the glass, glass in the logo, a button inside a message panel, a panel on a person, or empty
glass with nothing in it.
