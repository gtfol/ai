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
| skills/ | Reusable skills |
| mcp/ | MCP configuration templates |
| agents/ | Agent configuration templates |

Only the design standard is defined so far. Add the remaining files deliberately
as their requirements are decided. Store placeholders or environment variable
references in configuration templates, never live tokens or private keys.
