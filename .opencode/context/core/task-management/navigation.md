# Task Management

This repo does not currently ship an active local task-management CLI backend.

Current state:

- `.opencode/skills/task-management/router.sh` is a legacy placeholder that exits with a clear error.
- Any remaining `.infobot/...` references in agent prompts or commands are repo drift and should be corrected.
- Prefer the `TaskManager` subagent for planning work and repo-local task artifacts only when a real workflow defines them.

Guidance:

- Do not assume `.infobot/.tmp/tasks/` exists in this repository.
- If a real task backend is introduced later, document its canonical paths and schema here.
