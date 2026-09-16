---
name: gtfol-design
description: Build, refine, or review web interfaces in Allen's Freewrite/Capsule style, with restrained visuals, responsive interactions, and rendered UI verification. Use for interface design and frontend polish, not backend-only changes.
---

# Gtfol design

Read [the design standard](references/design-standard.md) before design work.
It defines Allen's default visual direction. Follow explicit task requirements
and preserve an existing product's necessary patterns. A narrow UI fix should
remain narrow; do not turn it into an unsolicited redesign.

## Understand the interface

Identify the main task, the content or object that deserves attention, and the
next action. Inspect the current screen and relevant components where available.
Reuse the project's framework, controls, typography, and tokens when they fit.
Ask about a missing decision only when it materially changes the result.

For a new interface, start with the primary flow and hierarchy. For an existing
one, locate the specific friction before changing visual details. For a review,
report supported findings; do not edit unless implementation is requested.

## Build the experience

- Let content lead. Place supporting statistics and advanced settings behind
  clear disclosure when they compete with the task.
- Apply the design standard's quiet palette, open spacing, and text-first
  controls. Avoid adding ornamental containers to fill empty space.
- Make state transitions explicit: loading, empty, error, pending, and success
  must match the underlying behavior. Preserve entered data during recovery.
- Give controls immediate feedback without claiming an operation has completed
  before confirmation. Repeated input should not accidentally repeat an action.
- Keep focus, keyboard operation, and touch use functional throughout changes.
  Use established accessible controls instead of rebuilding interaction behavior
  for visual convenience.
- Use motion only when it explains a change or makes an interaction easier to
  follow. If motion is part of the task, read [motion guidance](references/motion.md).
  A static interface can be the right finished result.

## Inspect the result

Use available browser or application tools to inspect the rendered result at a
wide and narrow viewport. Exercise the changed flow, including relevant empty or
failure states, keyboard focus, long content, and supported themes. Check reduced
motion when animation changes. Choose checks proportional to the change; avoid
an unrelated audit.

Look for lost hierarchy, clipping, covered controls, shifting layouts, ambiguous
states, and awkward repeated interactions. Correct observed issues, then repeat
the affected checks. A successful build or screenshot alone does not establish
that the interaction works.

If rendering or interaction tools are unavailable, perform the useful checks
that remain and say exactly what was not verified. Do not claim visual review
from source inspection alone.

Report the result, relevant verification, and remaining limitations briefly.
Use a comparison table only when it helps explain multiple changes.

Design engineering inspiration and license: [attribution](references/attribution.md).
