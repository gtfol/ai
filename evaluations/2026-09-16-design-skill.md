# Design skill trial — 2026-09-16

Status: **partially complete**. Codex completed the isolated UI task and its
result passed independent browser checks. Claude Code discovered the local skill,
but provider/model access prevented inference. Cross-tool behavior remains
unverified. No global installation or Tesla project changes were made.

## Task and isolation

Skill and shared instructions came from gtfol/ai revision `957c9f6`.
Two separate local Git repositories received identical copies of the Tesla
simulator viewer and its 38-scenario results file. Each received the shared
instructions, the Claude import, and gtfol-design in its tool's project skill
directory. The AI repository-specific instruction section was excluded.

The same task asked each tool to allow loading a replacement simulation report,
preserve the current report after an invalid replacement, provide accessible
loading/error feedback, and retain playback, themes, simulation meanings, and
the existing quiet design. The scope was approved in advance. The tools could
edit only their isolated copy and add local verification artifacts. They were
not asked to change firmware, install dependencies, commit, or push.

This explicitly invoked the skill. Automatic selection without a skill request
has not been tested.

## Codex

- Ran the desktop application's bundled Codex CLI 0.153.4 in a workspace-write
  sandbox with an ephemeral session. The separately installed command was broken;
  it was not repaired or replaced.
- Loaded SKILL.md and its bundled design standard.
- Added a persistent loading action, loading/error status, same-file retry, and
  validation before replacing the current report. Kept the main car illustration,
  report meanings, playback, and theme behavior.
- Passed its local Node state checks and whitespace checks.
- Attempted browser verification, then accurately reported that the sandbox
  blocked browser launch. It did not claim screenshots or visual checks passed.

Independent review ran outside the child sandbox using Playwright with a
temporary headless Brave profile. Sixteen independent browser checks passed:
report/replacement access, 38-scenario loading, invalid JSON and invalid schema
preservation, scenario/time preservation, live error feedback, continued playback,
successful recovery, playback/reset, theme behavior, overflow at 390 px and
320 px, reduced motion, and absence of uncaught page errors.

The candidate's additional browser script initially failed its focus-ring check:
it expected :focus-visible after programmatic focus in pointer input mode. The
reviewer retained that script and made a separate corrected copy that navigated
with Tab. The corrected script passed, including pending feedback, keyboard file
selection, same-file retry, cancellation, long filenames, playback continuity,
and absence of network requests. The original proposed script is not recorded as
a passing browser test.

The reviewer inspected desktop error, narrow light, and narrow dark/error
screenshots. The loading control and recovery message fit the existing style.
The pre-existing car illustration remains small on narrow screens; this trial
did not broaden into a responsive scene redesign. Screen-reader announcements
were checked structurally through live-region markup, not with a screen reader.

## Claude Code

- Claude Code 2.1.79 listed gtfol-design among its project-local skills.
- Its isolated default selected claude-sonnet-4-5, which the configured Foundry
  provider rejected before inference.
- Retrying the user's configured claude-opus-4-6 also failed. The provider's
  suggested claude-opus-4-1 alternative failed as well.
- No skill-body use, implementation, or verification occurred. The Claude copy
  is unchanged. This is a provider-access blocker, not a skill-quality result.

## Evidence and next step

Local artifacts are under the workspace's
`outputs/ai-design-trial-20260916/`: identical task prompt, source hash manifest,
separate tool logs/copies, independent checks, and screenshots. Raw session logs
and the large simulation fixture are not committed to this configuration repo.
Source viewer and results hashes were unchanged after the trial; the only tracked
input modified in the Codex copy was viewer.html.

The skill needs no change based on this limited trial. Before broader adoption,
restore a working Claude Code account/provider, rerun the same task on its clean
copy, and independently inspect the result. Do not treat skill discovery as proof
of successful use, or this single UI trial as comprehensive validation.
