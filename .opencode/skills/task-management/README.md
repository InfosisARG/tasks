# Task Management Skill (Local)

This directory currently provides legacy compatibility placeholders referenced by some bundled agents.

Current state:

- This repo does not contain the old `.infobot/skills/task-management/` implementation.
- `router.sh` and `task_cli.py` are kept only to fail fast with a clear error instead of silently pointing to a missing path.
- Treat any `.infobot/...` reference in `.opencode/agent/` or `.opencode/commands/` as repo drift to be corrected.

Repo guidance:

- Prefer direct task execution, local commands in `.opencode/commands/`, or the `TaskManager` subagent when planning work.
- If a real local task-management backend is added later, document its canonical paths here and update all references together.