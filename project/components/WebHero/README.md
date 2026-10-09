# WebHero

The website hero, "One memory, building": one glass element over a people-first film that plays once, three moments that build on each other, and the logo forming at the close. Press Play again.

## The film

22 seconds, 1920 wide, plays once and holds its last frame. Every shot opens on people: one person in her kitchen, four friends on a platform with their bags, five-a-side at dusk, a flat share in the evening, grandparents on the Sunday call with a slow push to stillness. 1s dissolves between shots, a fade in from black, no still behind the video. The file is `hero.mp4` in the **Film** asset group; phones get a 1280 wide copy.

## The sequence

1. **0.9s** Nav fades in. No logo in the nav yet.
2. **1.4s** "One memory. For all of it." over the kitchen, with a soft dark halo behind it. `all` in `blue-light`.
3. **1.8 to 3.9s** A thin line of light draws out from the centre over 1.5s, then swells up and down around its own centre into the glass bar. Blur, tint and shadow fade in together; the tile and placeholder arrive only once the bar has settled.
4. **Three moments, each building on the last.** The question types inside the glass, the bar opens down into the answer card, and the last word glows.
   - The trip, on the platform: "What did we decide about the third night?" gives "Porto, not Sintra. All four of you said **yes.**"
   - The pitch: "Can Leo still play on Thursday?" gives "Yes. He flies to Porto on Friday, so he is **in.**"
   - The grandparents: "When are we calling Nan and Grandad?" gives "Sunday at 11, once Leo is back. They already **know.**"
5. After each answer the card folds into a small glass layer that rises above the bar; the memory visibly grows to three layers. The opening line steps aside while they build.
6. **17.4s** The layers sink back into the bar, which glows once and becomes the waitlist field.
7. **18.9s** The logo forms above the field: the two brackets fade in from a soft blur and drift sideways into the mark, one a beat after the other; at 20.3s the name appears left to right behind a soft-edged wipe.
8. **20.7s** "One memory. For all of it." settles under the field as the sign-off. Everything holds.

## Rules

- One radius through every state: the bar, the card and the field keep `radius-glass`; nothing is a pill. The tile and send button use `radius-inner`, concentric with the bar.
- The answer card grows to fit its text; a long question steps its size down a little, then glides left like a real field. On phones a question may take two lines in a 64px bar.
- The cursor sits at the left edge whenever the bar is empty and disappears while words clear.
- The last word glows (`blue` with a soft blue text glow that breathes slowly), never underlined.
- The logo is about half the field's width, clear of it, and shifted 3.5 percent left so it reads optically centred.
- Morphs run 1.4s on `cubic-bezier(.65,0,.25,1)`; arrivals settle on `cubic-bezier(.22,1,.36,1)`; a band of light passes over the glass after each change.
- Reduced motion or no autoplay: the last frame and the end state, at once.

## The other hero

**SiteHero**, the split hero on the grey ground with the form above the fold, stays as a reference for CTA pages.
