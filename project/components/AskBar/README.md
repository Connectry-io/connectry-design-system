# AskBar

The brand's twist. A person in their own day, one bar of brand glass with their own words
typed into it, one line back beneath it over the picture. The whole product in a second: not
an app shown, a sentence answered.

It is a **film and marketing device**, not a product screen. There is no chat of our own; the
conversation stays in the host.

## Geometry

On a 1920 frame: 1320 by 144px, centred, centre at 56 percent of the height, `radius-ask`,
padding 0 28 0 32, gap 24. Left the mark on a 40px `blue` square at `radius-tile`, then the
name at 22px in `muted`. Middle the ask at 48px weight 500 in `ink`, tracking -0.02em, solid
caret. Right a 68px `blue` circle with a white up arrow at 2.4px stroke.

On the web it scales with the frame: width 68.75cqw, height 7.5cqw, ask 2.5cqw, answer
3.54cqw, send 3.54cqw, chip 2.08cqw, answer gap 5.625cqw, radius 1.25cqw.

## The answer

108px beneath the bar's centre on a 1920 frame, centred, 68px weight 500, white over the
picture with a soft shadow, **never in a box**. Two short sentences under twelve words: what
happened, and what that means for them. The second in `blue-light`.

## Motion

The bar fades and rises over six frames. The ask types at the film's rate and resolves by 55
percent of the shot, step clamped 0.6 to 1.25 frames per character. The send dips once when
the ask completes. The answer rises over nine frames, four frames after the send.

## Placement

It may cross the person's body below the shoulders, because it is theirs. It never crosses a
face, and the answer never sits on one.

## The pairs

"What changed while I was asleep?" / "Three things. Already handled." · "Is Dad's check-up
still Thursday?" / "Thursday, 9:30. Leo's driving him." · "Anything expiring soon?" / "The
passport. Renewal drafted." · "Move the client call to 11" / "Moved. They already know." ·
"Move the flight to Saturday" / "Checked. £38 more, same bags." · "Share the plan with the
others" / "Shared. One copy each."

Rendered frames from the film are `stills/f5-ask-crossing.jpg` and `stills/f6-ask-flat.jpg` in
the **Film** asset group.

## Never

A plus, a mode pill, a speak button, placeholder text, a tagline where the answer goes, a
second bar, a boxed answer, or the bar on a face.
