# WaitlistForm

The site's one action, "Join the waitlist", and every state it can be in.

## Structure

- **Field and action as one shape.** A 52px pill field (`surface` at 72 percent, hairline inset)
  holding the email input and the blue **Pill** "Join the waitlist".
- **Head.** `label` Waitlist, the state word right.
- **Title.** "Be there when it opens." 20px.
- **Note.** "One email when it is ready. Nothing else." in `muted` 13px.

## States

Empty · Focus (2px `blue` ring, `:focus-visible`) · Error (a plain sentence in `muted` beneath the
field that says how to fix it, never red, never an icon alone) · Done (the field is replaced by
"You are on the list." and what happens next). On a photograph it takes the dark plate.

## Never

More than one field, a checkbox wall, a count of people waiting, urgency, a red error.
