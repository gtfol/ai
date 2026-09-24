# Shared agent instructions

These are Allen's established preferences for Codex and Claude Code. Maintain
shared instructions here; CLAUDE.md imports this file. Installing these
instructions into other projects or global settings is a separate step.

## Planning and implementation

Before implementing substantial changes, present the proposed approach, scope,
and verification to Allen and wait for agreement. Read-only investigation may
continue to make the plan concrete. Once the plan is approved, carry it through
without repeatedly asking; check back if the scope or approach materially changes.
Keep routine, contained edits proportional rather than introducing a planning
gate for every small change. Approval of a plan does not override the explicit
permission requirement for ignored files below.

## Communication

Give brief progress updates and concise results. Focus updates on meaningful
progress, decisions, or blockers. Lead final responses with the outcome and
include relevant verification or limitations. Expand when Allen asks for detail
or needs it to make a decision.

## Service dashboards

For authorized work, manage Supabase, Apple Developer, and App Store Connect
directly using available computer-use tools and signed-in sessions. Confirm the
correct account, project, and app before making changes. Carry out routine
dashboard steps within the agreed scope instead of handing them back to Allen.
Ask Allen when login, MFA, a required approval, or a change outside that scope
prevents progress. Verify that changes were saved and report any remaining block.
Never expose credentials or store them in instructions, source, or logs. These
instructions do not bypass tool permissions or the ignored-file rule below.

## Verification

Run relevant tests for code changes and inspect the rendered result for UI
changes. Exercise the affected behavior, with checks proportional to the change.
Clearly state what was verified and anything that remains unverified. Do not
present a passing build or source inspection as proof of working UI behavior.

## Commits

- Never include "Generated with Codex" or similar agent attribution in commit
  messages. Never include Co-Authored-By lines.
- Keep commit messages extremely concise: a comma-separated list of major
  changes, such as "add X, update Y, remove Z".

## Persistent preferences

When Allen says to do something or not do something "ever again," or otherwise
expresses a persistent preference, ask whether to add it to AGENTS.md and whether
it belongs in the master instructions or the current project's instructions.
If Allen already specifies that scope, use it without asking again.

## Ignored files

Before editing a gitignored file, always ask for explicit permission, including
for .env files, secrets, and credentials. An allowed filesystem path alone is
not permission to edit an ignored file.

## Sound notification

After finishing a response to Allen's request or running a command, notify Allen
with this command on macOS:

```sh
afplay /System/Library/Sounds/Funk.aiff
```

On a system without that command or sound file, report that the notification
could not play; do not install an audio utility as a side effect.

## Working in this repository

- This is the private gtfol/ai source repository for Codex and Claude Code
  guidance. Adding configuration here does not authorize installing it globally.
- For interface design work, read DESIGN.md. The shared gtfol-design skill is
  under skills/gtfol-design/; keep its workflow usable by both tools.
- DESIGN.md is the canonical design standard. After editing it, run
  `python3 scripts/sync_design.py`; before distributing the skill, run
  `python3 scripts/sync_design.py --check`. Do not independently edit the bundled
  copy under the skill's references directory.
- Keep credentials out of configuration templates. Preserve attribution and
  required license notices for adapted third-party material.
