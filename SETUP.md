# Codex and Claude Code setup

This private repository is the maintained source for Allen's reusable agent
guidance. Supported tools are Codex and Claude Code. Storing files here does not
activate them in other projects or change either tool's local configuration.

## Shared content, separate configuration

| File or directory | Responsibility | Status |
| --- | --- | --- |
| DESIGN.md | Freewrite/Capsule visual standard | Written |
| AGENTS.md | Established shared preferences and AI repository instructions | Written; initial working preferences agreed |
| CLAUDE.md | Import AGENTS.md; add only necessary Claude-specific instructions | Written |
| skills/gtfol-design/ | Shared design implementation and review workflow | Written; adoption pending |
| codex/ | Codex-specific configuration templates | Add when needed |
| claude/ | Claude Code configuration templates | Add when needed |
| mcp/ | Tool connection templates with environment references | Add when needed |

Keep planned directories absent until they contain something useful. No global
instruction files, settings, skills, or connections have been installed as part
of this setup.

Claude's entry point contains:

```markdown
@AGENTS.md
```

Claude Code documents this import specifically for sharing instructions with
other agents. Avoid maintaining two copies of the same working preferences.

AGENTS.md also applies to work in this repository. It contains the existing
master preferences on commits, persistent preferences, ignored files, and sound
notifications, followed by a clearly scoped AI repository section. Global
adoption must separate those repository-specific instructions from the shared
preferences rather than copying the entire file blindly.

Allen's chosen working style: check the plan before implementing substantial
changes, then carry out the approved plan without repeated confirmation.

Communication preference: brief progress updates and concise results.

Verification preference: relevant tests for code changes, rendered checks for UI
changes, and a clear statement of anything unverified. These working preferences
are recorded in AGENTS.md. Existing tool-level and project-level requirements
continue to apply.

## Build it in this order

1. **Design skill.** Keep DESIGN.md as the source of visual taste. Write a focused
   implementation/review workflow inspired by Emil Kowalski's design engineering
   skill: purposeful motion, responsive feedback, interruptible transitions,
   reduced motion, and inspection of the rendered result. Adapt those techniques
   to the quiet Freewrite/Capsule direction. Credit source material and retain any
   required license notices when adapting content.
2. **Shared instructions.** Agree on initiative, communication, verification,
   commits, and permission boundaries. Keep these independent of design tasks.
   Then add the small Claude import file.
3. **Try one project.** Make the skill available to both tools in a chosen
   project, exercise a real UI task in each, and check behavior before broader
   adoption. A valid file format alone does not prove equivalent agent behavior.
4. **Configurations and MCPs.** Add only settings and connections Allen actually
   uses. Maintain each tool's native format. Keep credentials out of this repo.
5. **Repeatable installation.** Once the layout has been exercised, add an
   installer with a preview, explicit target scope, collision handling, and a
   way to restore the prior state. Preserve unrelated existing configuration.

## Skill installation targets

Author one portable skill directory under skills/. Use the shared SKILL.md
format and keep tool-specific extensions out of the common entry point.

| Scope | Codex | Claude Code |
| --- | --- | --- |
| One project | .agents/skills/<name>/ | .claude/skills/<name>/ |
| This user's machine | ~/.agents/skills/<name>/ | ~/.claude/skills/<name>/ |

Installation must include the skill's referenced resources, including the design
standard when required. The gtfol-design skill bundles a generated copy of the
root DESIGN.md under references/. Run `python3 scripts/sync_design.py` after
editing the root standard and `python3 scripts/sync_design.py --check` before
distribution. Copy the entire skill directory. It does not require access to the
source checkout or the private GitHub repository at runtime.

Start with project scope. User-wide installation is a separate adoption step;
it can affect other projects and needs a review of existing settings first.

## References

Documentation checked on 2026-09-16:

- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code AGENTS.md imports](https://code.claude.com/docs/en/memory#agentsmd)
- [Emil Kowalski's design engineering skills](https://emilkowal.ski/skill)

Installation and discovery paths above describe documented support. Neither
tool's skill loading has been tested against this repository yet.
