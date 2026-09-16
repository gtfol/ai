# ai

Private organization reference for design standards and future agent instructions
and configuration.

Supported tools: **Codex and Claude Code**. Maintain shared guidance once, with
tool-specific configuration only where necessary. See [SETUP.md](SETUP.md) for the
setup sequence and adoption plan.

Start with [DESIGN.md](DESIGN.md), based on the Freewrite and Capsule interfaces.
This repository stores reference material; it does not automatically change any
agent's configuration.

## Planned layout

| Path | Purpose |
| --- | --- |
| DESIGN.md | Shared interface design standard |
| AGENTS.md | Shared agent instructions, to be written later |
| CLAUDE.md | Import shared AGENTS.md, add Claude-specific guidance only if needed |
| skills/gtfol-design/ | Shared interface design and review skill |
| mcp/ | MCP configuration templates |
| agents/ | Agent configuration templates |

The design standard and [gtfol-design skill](skills/gtfol-design/SKILL.md) are
written. The skill includes a portable copy of the design standard, generated
from the root file. After editing DESIGN.md, run:

```sh
python3 scripts/sync_design.py
python3 scripts/sync_design.py --check
```

Do not edit the generated copy independently. To adopt the skill, distribute its
whole directory, including references. It has not yet been installed or exercised
in a real UI task with both tools; see [SETUP.md](SETUP.md).

Add remaining configuration deliberately as requirements are decided. Store
placeholders or environment variable references, never live tokens or private keys.
