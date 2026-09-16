<!-- Generated from repository DESIGN.md by scripts/sync_design.py. Edit the source, then regenerate. -->

# Design standard

Quiet, useful interfaces in the style of Freewrite and Capsule.

This is the default direction for future design work requested by Allen. Apply
it to new interfaces and substantial redesigns. Respect explicit task requirements
and an existing product's necessary interaction patterns. This document is a
shared reference; putting it in this repository does not automatically install
instructions into any agent or project.

## References

Reviewed the live interfaces and source styles on 2026-09-15:

- [Freewrite](https://freewrite.gtfol.dev): a generous writing column, text-first
  controls, restrained bottom toolbar, and a white or black canvas.
  [Styles at the reviewed revision](https://github.com/gtfol/freewrite/blob/046e39b39f2a57b23a83cd701c8e03894bc5305c/app/globals.css).
- [Capsule](https://capsule.gtfol.dev): content without enclosing cards, compact
  labels, subtle dividers, monochrome navigation, and ample space around objects.
  [Styles at the reviewed revision](https://github.com/gtfol/capsule/blob/efee76d996967c75e2e3878dc310223312ced596/src/app/globals.css).

The rules below synthesize that direction. Sizes and accessible color adjustments
are defaults for new work, not claims that the reference apps use every value.

## Start with the task

- Identify the one thing the user came to do. Give it the most space.
- Show the content, object, or interaction before statistics about it.
- Put specialist readings and configuration behind clearly labeled disclosure.
- Make the next action visible. Keep the initial screen short.
- Use plain labels and concise explanations. Keep implementation terminology out
  of the interface unless it helps someone make a decision.

For a simulator, the primary view is the thing being simulated: a car and a moving
key. Charts, protocol events, and diagnostics support that view. State clearly
when movement is illustrative rather than measured.

## Visual language

- White canvas with near-black text; optional black canvas with off-white text.
- Monochrome by default. Use color sparingly for meaningful state or actual content.
- Let spacing, alignment, and type establish hierarchy.
- Prefer open layouts and thin separators. Add a container only when it clarifies
  grouping, selection, or an interaction boundary.
- Use text actions and simple line icons. Give every icon action an accessible name.
- Avoid decorative gradients, glows, glass effects, oversized hero headings,
  dense dashboard cards, status-pill collections, and unnecessary shadows.
- Keep meaningful states distinct even in grayscale. Labels must explain success,
  failure, uncertainty, and unavailable features.

## Starting tokens

| Role | Light | Dark |
| --- | --- | --- |
| Canvas | #ffffff | #000000 |
| Main text | #111111 | #eeeeee |
| Secondary text | #686868 | #aaaaaa |
| Divider | #e5e5e5 | #2c2c2c |
| Hover surface | #fafafa | #111111 |
| Caution | #85601b | #d4b26a |
| Error | #ac3030 | #ef9696 |

Secondary text is intentionally stronger than some reference metadata. Check
contrast in the actual context. Decorative dividers may be subtle; essential
control boundaries and focus indicators must remain easy to see.

Use semantic CSS variables rather than repeating colors throughout components.
Color must never be the only way to understand a state.

## Typography and space

- Prefer Lato, which both references use, with a system sans-serif fallback.
  Bundle a properly licensed font if needed; offline tools must not require
  a font service or network connection.
- Normal weight does most of the work. Use medium weight sparingly.
- Typical interface text: 13–16 px. Secondary labels: 12–13 px.
  Reading content: 17–20 px with generous line height.
- Headings should establish structure without becoming a separate visual event.
  Start around 16–24 px for tools and adjust to the content.
- Use tabular numbers for changing time and measurements.
- Start with 20 px mobile gutters and 30–32 px desktop gutters.
  Use consistent 4, 8, 12, 16, 24, 32, and 48 px spacing increments.
- A focused tool or reading column usually fits within 650–840 px. Collections
  can use the available width with responsive grids.
- Preserve useful whitespace while keeping the primary action within reach.

## Interaction

- Controls should look quiet and still be discoverable: visible labels, subtle
  hover feedback, and clear selected and focus states.
- Prefer text toolbars; a bottom toolbar is appropriate for persistent actions.
  Reserve space so it cannot obscure content, errors, or keyboard focus.
- Keep touch targets roughly 44 px where practical, even when the visible icon
  or label is smaller. Essential actions must work without hovering.
- Use native controls and semantic HTML where they work well.
- Light and dark themes must change the entire interface, including diagrams.
- Motion should explain a change. Avoid decorative loops and automatic playback.
  Support reduced motion, pause, reset, and direct navigation through a timeline.
- Preserve user control of zoom, keyboard navigation, and screen-reader access.

## Honest states

- Design empty, loading, error, disabled, and completed states before calling the
  interface finished. Never leave a blank page when data is missing.
- An empty view should explain what is missing and offer a concrete next step.
- A failed load should preserve a way to retry or choose another file.
- Show uncertainty explicitly. An unconfirmed command is not a successful result.
- An unsupported feature must remain labeled unsupported, even if a negative test
  passes. Simulation success is not hardware validation.
- Show sample, simulated, or illustrative content as such. Do not imply measured
  distance, battery life, capability, or real-world success without evidence.

## Review before delivery

1. Compare the result with Freewrite and Capsule: does the content lead, with
   quiet controls and a restrained palette?
2. Remove framing, labels, and repeated explanations that do not help the task.
3. Inspect the actual rendered interface on a wide and narrow viewport.
4. Exercise the primary flow, keyboard focus, theme toggle, empty state, and error
   recovery. Check that no toolbar covers the final content.
5. Verify contrast, readable text, zoom behavior, and reduced-motion behavior.
6. Verify local/offline use where promised. Missing data must produce a useful
   state rather than a blank screen.
7. Report what was tested and any remaining limitation plainly.

## Adoption

Projects can keep a copy of this file or link to a pinned revision. An agent
instruction file can later tell that project's tools to read it before design
work. AGENTS.md, CLAUDE.md, skills, MCP definitions, and agent configuration are
separate concerns and can be added when their behavior has been decided.
