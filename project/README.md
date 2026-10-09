# Connectry

**Your brain. Wherever you work.**

This is the whole Connectry system, version 2.1: the brand, the marketing surfaces and the
product UI in one place. It replaces every earlier Connectry design system, including the
`connectry-design` skill built around Urbanist and `#0066cc`, which described a different
company and is retired.

Where this system and the published brand site disagree, the site is newer. Where a build,
a deck, a card or a product screen is checked, it is checked against this.

## What we are

One brain per person. And one for your people. One memory for the whole of a life, on every
surface the person already uses: their assistant, their messages, their mail. Text, pictures
and everything they connect. It grows with them, takes care of what it can, and outlives the
moment. It remembers why, not just what. And it arrives with the applications ready to use:
the circle, the trip, health, learning, money. Nothing to set up; the complexity is ours.

A memory and applications company, not a memory alone.

In three words: **Remembers. Takes care. Passes on.** Each one is something already
built and running.

Two doors, described, never named as products. *For you* is the individual, the whole of a
life in scope, work included. *For your people* is circles: a flat share, a five-a-side team,
grandparents on a video call, a parents' group, a couple, friends on a trip, the cafe, the
freelancer, the small team. In every circle a person shares only what they choose, and mail is
never one of those things. Never "family" alone; the circle is always wider.

The circle's wedge is host neutrality: one shared memory for people who each use a different
assistant. No first party can do that, because their memory is their lock-in. There is no app
of our own and no chat of our own; the conversation stays in the host and the brain reaches it
through one connector. The ask bar is a film device for that exchange, not a product screen.

Never on anything public: pricing or any pricing shape, tiers, compliance or certification
claims, user counts, "trusted by", revenue, a specific industry, a business door,
organisations, methodology, or any assistant or vendor name.

## Foundations

**Colour.** `blue` is the one accent: a primary action and one accent word, at most twice per
surface. `blue-light` is for film and dark photography only, never as text on `ground` or
`surface`. Everything else is the neutral ladder `ink` · `body` · `muted` · `faint`, on
`ground` with `surface` for cards and `hairline` for every rule. No gradients as decoration
(the photographic `scrim` is the exception), no purple, no navy fills, no black backgrounds
(Site dark is graphite, never black), no glow except the soft glow on an answer's last word,
no second accent. Charts take `chart-accent` for the one series that matters and
`chart-comparison`, `chart-step-1`, `chart-step-2` for the rest.

Three themes ship: **Light** is every surface a person reads on, **Film** is the dark register
of photography, the product film and the endcard, and **Site dark** is the website's graphite
edition (`ground` `#0e0f11`, off-white type, `blue-light` as the one blue). None of them is a
toggle. The brand stays light first everywhere else: choosing dark for the website never makes
another surface dark. Each edition is a known version, documented side by side.

**Type.** Inter only, weights 400, 500 and 600, with `cv11` and `ss01` on. Nothing is bold
except the wordmark. `display` and `headline` are fluid, clamped between the phone and the
desktop size in the token's usage note. Headlines end with a full stop and carry one accent
word at most. `label` is the only uppercase in the system. Numbers are tabular everywhere.

**Layout.** Three measures build everything: the gutter `max(20px, 6.9vw)` sets the edge on
the site, the slide safe area and the social cards; the left rail is where a line lives,
`5.6vw` from the bottom of a film frame; the open third of a photograph is where glass may
sit. Spacing is the 4px scale, `space-1` to `space-30`, and nothing is placed on a number
that is not on it. Radii are `radius-panel` 16, `radius-card` 12, `radius-tile` 10,
`radius-doc` 8, `radius-pill` 999 for toggles, avatars and dots only. On the site one family
holds everything: `radius-frame` 28, `radius-glass` 19, `radius-inner` 11; no pill-shaped bars,
fields or buttons. Grids break at 1000 (stage grids to one column), 900
(section heads stack) and 640 (everything to one column).

**Glass.** Connectry glass is a convex lens, not a blur. Only 2px of blur, so the photograph
behind stays sharp and slightly richer through it, with the picture bending at the rim. It
needs the `#lens` SVG filter and either a photograph or the two blooms behind it. The tint
never drops below 26%, which is what keeps `ink` above 4.5:1 inside a panel. See the
**GlassPanel** component and the Glass section. On the grey ground the lens reference is left
out: there is nothing to bend, only the blooms.

**Motion.** Things arrive once. Nothing loops; the website's hero film plays once and holds. `cubic-bezier(.2,.7,.2,1)` for anything that
arrives or comes to rest, 160ms `ease` for hover and state, `cubic-bezier(.16,.8,.24,1)` for
the brackets. Three exceptions, each in one place only: the question types inside the hero's
glass, the wordmark wipes in left to right at the logo reveal, and film dissolves into the page
at its edges. No pulses, shimmer, parallax or bounce, and no motion inside the mark. Reduced motion is honoured everywhere: the glass is simply there, the
blooms hold still, the lockup is shown complete.

**Iconography.** Almost none. The site uses a few 1.8px line icons for the sources and the
three promises, and the X, LinkedIn and Instagram glyphs in the footer; nothing decorative. Where an
icon is unavoidable, it is a 1.5px stroke in a 20px box, in `ink` or `muted`, never in `blue`.
The mark is not an icon. Status is never carried by colour alone: a state is always also a
word.

## The mark

Two brackets on a 100 unit grid, stroke 15, gap 6:
`M32 0H47V47H0V32H32ZM53 53H100V68H68V100H53Z`. It reads as a crop mark, a frame around what
matters. It carries no meaning that needs explaining and it is never explained.

The wordmark is "Connectry" in Inter SemiBold at `-0.03em`, converted to paths. In the lockup
the mark's height equals the cap height and the gap is 0.6 cap. Masters are in the **Logo**
asset group. Clear space is half the mark height on every side; minimum size is 96px or 24mm
for the lockup, 16px or 4mm for the mark. Never stretch, rotate, outline, gradient, shadow,
recolour, change the gap, add a symbol, animate the mark on its own, or place the logo inside
glass. The endcard lockup is the one animation, and it is the lockup, not the mark.

## Applications

**Web.** Chapters, dark (**WebChaptersDark**): the hero **WebHero**, one memory building over a
people-first film that plays once, the logo forming at the close; then what Connectry is,
memory, circles, where it lives, it takes care, yours, and start your circle over the last
film. Graphite pages between full-bleed film chapters that dissolve into them. The nav has no
logo until you scroll, then Contact us and a menu on desktop and only the centred lockup on
phones (**WebNav**); the footer is one line on the faded end of the last film (**WebFooter**).
The light edition (**WebChaptersLight**) is the same page on the grey ground. The earlier
six-chapter page and the split **SiteHero** stay as references for CTA pages.

**Product.** The same tokens and the same components. One idea per screen. Lists are hairline
rows. The brain speaks in a message panel; a built thing appears as a doc preview; a circle
speaks in a circle panel with the members row and never exposes a member's private memory.
The home surface is the dashboard: the person's day, the applications ready to use, and the
connectors that feed them, on one sheet of glass.

**Slides.** 16:9 at 1920 by 1080, margin 86, lockup 36px top left, section label beneath it,
page number bottom right, cool grey ground, glass only where a panel is needed, no bullet
layouts. Charts are native, one axis, hairline gridlines, the value on the mark.

**Social.** One line top left or middle left in white Inter 500, the lockup white bottom left
at 4% of the width, the slogan as the one glass chip bottom right, nothing else on the image.
Glass panels sit on the open third only.

**Collateral.** A one-page overview in A4 and Letter, an email signature built as a table with
the mark hosted as a PNG, and the slide template with editable native charts.

## Voice

Sober, warm, specific. Short sentences. One accent word per headline, and the headline ends
with a full stop. "It" is the subject more often than "we". We only say what we did once: we
run ours on it first.

Never: exclamation marks, em dashes, or the hype words (delve, unlock, seamless, empower,
journey, leverage, landscape, game-changing, supercharge, revolutionary, cutting edge, next
generation, AI-powered, intelligent, smart).

Lines that carry the voice: It takes care. · Ready to use. · Only what you choose to
share. · Mail read, calendar moved, coffee still hot. · It remembers. · It holds your people. ·
Some things are yours. Some things you share. · Your year, prepared. · It builds. · It knows
why. · Passed down, not lost. · It's already done. · Wherever you already work. · We run ours
on it first.

## Before anything ships

- One blue action and one accent word at most.
- Inter only. No literal colours outside the tokens.
- Glass has the `#lens` filter and a photograph or the blooms behind it.
- No type and no glass on a person's face. The ask bar is the one exception, below the
  shoulders.
- Circles are circles: fixed width and height, never squeezed by a row.
- A focus ring on every interactive part, `:focus-visible` only.
- Every grid row full.
- No em dash, no exclamation mark, no banned word.
- The logo untouched, and never inside glass.
- No pricing, compliance, user-count, vendor or assistant claims.

## What is in this system

Read it in layers. Each layer is built only from the one above it.

1. **Tokens.** Colour, type, spacing, radii, shadows, opacity (the Tokens section).
2. **Brand.** Logo, Endcard, Blooms, Motion, and the Logo, Glass and Icons asset groups.
3. **Glass.** **GlassPanel**, the one primitive, and every panel made from it: MorningWidget,
   CircleCard, ReplyPanel, NotificationGlass, ShareToCircle, MemoryCard, DocPreview, AskBar.
   **GlassContrast** proves each plate holds 4.5:1.
4. **UI.** Pill, TextLink, Chip, Toggle, Input, WaitlistForm, ListRow, ProofNumber, Chart, Avatar,
   Nav, SectionHead, TwoDoors, Footer.
5. **Product.** Dashboard, Board, HostChat, PhoneChat, PhoneScreens, ApplicationTile,
   ConnectorPill. These follow the product film frames exactly.
6. **Website.** **WebChaptersDark** is the site; **WebChaptersLight** its light edition;
   **WebHero**, **WebSections**, **WebNav** and **WebFooter** are its parts. The earlier
   **Website** method and its chapter cards (SiteHero, SiteRelief, SiteBelonging, SiteKnown,
   SiteLasts, SiteFilmWaitlist) and AskHero stay as references for CTA and campaign pages.
7. **Film.** **FilmLibrary** plays the 75-second product film with its seven grammar frames;
   FilmClipsPeople, FilmClipsCircles and FilmClipsCity play every clip.
8. **Marketing and social.** PhotoLine, OnePager, EmailSignature, Slide, the **Deck** (all
   eighteen layouts), **ImageryLibrary**, SocialCard, InstagramPost, InstagramStory, LinkedInPost,
   **SocialLibrary** and **SocialLibraryCircles**.

**Assets.** Logo, Glass, Imagery, Circles, Film (the clips, the stills, the product film and the
hero loop), Social, Slides, Icons.

## The logo, in one paragraph

The lockup is always one colour: `ink` on light grounds (the default), white on film,
photographs and dark, and a `blue` lockup only as a rare accent on `surface` or `ground`. The
mark and the wordmark always travel together as the lockup, in the website nav at 24px once you scroll and on every
social card; the mark alone is for the favicon, the app icon, avatars and the sender tile in a
notification, where it sits white on a `blue` tile. There is no multi-colour version.

## Sections

The brand book continues in the sections below this one: how this system works, positioning, colour and type, layout
and spacing, glass, motion, accessibility, imagery and film, the product film grammar, voice,
applications, the ask, the dashboard, and governance with the version history.
