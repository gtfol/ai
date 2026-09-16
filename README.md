# ai

Private organization reference for design standards and future agent instructions
and configuration.

Supported tools: **Codex and Claude Code**. Maintain shared guidance once, with
tool-specific configuration only where necessary. See [SETUP.md](SETUP.md) for the
setup sequence and adoption plan.

Start with [DESIGN.md](DESIGN.md), based on the Freewrite and Capsule interfaces.
AGENTS.md and CLAUDE.md apply when an agent works in this repository. They do not
automatically change global settings or instructions in other projects.

## Contents and planned additions

| Path | Purpose |
| --- | --- |
| DESIGN.md | Shared interface design standard |
| AGENTS.md | Established shared preferences and AI repository instructions |
| CLAUDE.md | Import shared AGENTS.md, add Claude-specific guidance only if needed |
| skills/gtfol-design/ | Shared interface design and review skill |
| mcp/ | MCP configuration templates |
| agents/ | Agent configuration templates |

The shared instructions, design standard, and
[gtfol-design skill](skills/gtfol-design/SKILL.md) are written. The skill includes
a portable copy of the design standard, generated
from the root file. After editing DESIGN.md, run:

```sh
python3 scripts/sync_design.py
python3 scripts/sync_design.py --check
```

Do not edit the generated copy independently. To adopt the skill, distribute its
whole directory, including references. An [isolated UI trial](evaluations/2026-09-16-design-skill.md)
passed with Codex plus independent browser review. Claude Code discovered the
skill but could not run because of provider/model access. Broader installation
remains pending; see [SETUP.md](SETUP.md).

Add remaining configuration deliberately as requirements are decided. Store
placeholders or environment variable references, never live tokens or private keys.
