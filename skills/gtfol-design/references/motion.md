# Motion and feedback

Use these as starting decisions, not mandatory effects or timing limits. The
project's established motion system and the actual interaction take precedence.

## Choose what earns motion

Motion can explain where a panel came from, show an object changing position, or
acknowledge input. Reduce or omit it when repeated use makes it feel like waiting.
Typing, selection, and frequent navigation should respond immediately. Do not
delay an action or focus change solely to complete an animation.

## Tune the transition

- Begin with short transitions, roughly 120–200 ms for small controls and
  180–250 ms for a panel. Judge them in context, including rapid repeated use.
- For an entering panel, try easing that shows movement promptly and settles
  gently. For movement between positions, consider easing at both ends. Keep
  timing consistent with the rest of the interface.
- Animate from the trigger's location when that explains the relationship. Use
  small movement or scaling; large travel and bounce need a clear purpose.
- Name the properties being animated. Prefer opacity and transforms when they
  express the intended effect; inspect actual performance when it is a concern.
- Reversing or cancelling an interaction should settle into the latest requested
  state. Test open-close-open quickly; avoid queued transitions and stuck states.
- Use the existing animation library when appropriate. A simple transition does
  not justify adding a dependency. Reserve springs or gesture systems for tasks
  that benefit from their behavior.

## Preserve control

Respect reduced-motion preferences with an immediate change or a restrained
alternative that preserves the same information. Essential controls and state
must remain available. Do not make correctness depend solely on an animation's
completion event.

Hover feedback must have a touch and keyboard equivalent where needed. Pressed
feedback may be a subtle surface or border change; every button need not shrink.
After a failed operation, offer a useful recovery action instead of replaying
success-like feedback. Keep explanatory timelines pausable and directly navigable.

Adapted in spirit from [Emil Kowalski's design engineering skill](attribution.md),
with quieter defaults and context-dependent choices for Gtfol interfaces.
