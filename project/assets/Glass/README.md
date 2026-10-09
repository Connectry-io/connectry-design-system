# Glass

`lens-map.png` is the convex, rim-weighted displacement map that makes Connectry glass a lens
rather than a blur. It drives `feDisplacementMap` at scale 42 inside the `#lens` filter.

Inline the filter once per page that uses glass, pointing `feImage` at this asset's URL:

```html
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <filter id="lens" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
    <feImage href="/_blob/8307ef4bba30e82def04ad8320eaf6fb" x="0" y="0" width="100%" height="100%" preserveAspectRatio="none" result="map"/>
    <feDisplacementMap in="SourceGraphic" in2="map" scale="42" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
</defs></svg>
```

Then `backdrop-filter: url(#lens) blur(2px) saturate(1.7) brightness(1.04)`, with the plain
`blur(2px) saturate(1.7) brightness(1.04)` declared first for engines that ignore a filter
reference. Full rules are in the Glass section and the GlassPanel component.

In a build that inlines the map as a data URI rather than fetching it, the file is the same
bytes; keep the scale at 42 and the channel selectors at R and G.
