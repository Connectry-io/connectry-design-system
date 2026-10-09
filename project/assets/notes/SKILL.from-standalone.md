---
name: connectry-design
description: Use this skill to generate well-branded interfaces and assets for Connectry (native Salesforce ISV — LWC + Apex apps for the AppExchange, plus the connectry.io marketing site), either for production or throwaway prototypes/mocks. Contains essential design guidelines, colors, type, fonts, assets, and UI kit components for prototyping both the marketing and in-product (SLDS-compatible) surfaces.
user-invocable: true
---

Read the `README.md` file within this skill, and explore the other available files (`colors_and_type.css`, `assets/`, `ui_kits/marketing/`, `ui_kits/salesforce/`, `preview/`).

Connectry has **two distinct surfaces** — always ask or confirm which you are designing for:

- **Marketing (`connectry.io`)** — primary color `#0066cc`, expressive, big Urbanist 800 headlines, generous white space, editorial.
- **In-product (Salesforce LWCs)** — primary color `#4A6FA5`, SLDS-compatible, compact, gradient header, system font stack. **Never strip SLDS borders or use transparent overrides — recolor, don't restructure.**

Always use tokens from `colors_and_type.css` — never hardcode colors or fonts. All custom classes prefix `connectry-`, all CSS vars prefix `--connectry-`.

Voice: architects, not evangelists. Direct, confident, no marketing fluff. No emoji in UI copy.

If creating visual artifacts (slides, mocks, throwaway prototypes, etc), copy assets out of `assets/` and create static HTML files for the user to view. If working on production code, you can copy assets and read the rules here to become an expert in designing with this brand.

If the user invokes this skill without any other guidance, ask them what they want to build or design, confirm which surface (marketing vs. in-product), ask some questions, and act as an expert designer who outputs HTML artifacts _or_ production code, depending on the need.
