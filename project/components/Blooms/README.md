# Blooms

Glass on the flat grey ground has nothing to bend. Two large radial blooms behind the layout
give it light.

`bloom-blue` at `opacity-bloom-blue` (18 percent) and `bloom-warm` at `opacity-bloom-warm` (15
percent), each around 55 to 60vmax, blurred 120px, drifting over 70 to 90s on
`ease-in-out … infinite alternate`. This is the one thing in the system that moves
continuously, and it moves slowly enough that it reads as light rather than animation.

Put them on any ground section that carries a glass panel, inside a container with
`overflow:hidden` and `isolation:isolate`, and lift the content above them with
`position:relative; z-index:1`.

Reduced motion holds them still. They are never used on a photograph, which already has light
of its own.
