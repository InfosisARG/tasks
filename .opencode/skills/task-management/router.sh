#!/usr/bin/env bash
set -euo pipefail

printf '%s\n' "task-management legacy shim is not configured in this repository." >&2
printf '%s\n' "Missing backend: .infobot/skills/task-management/" >&2
printf '%s\n' "Use local commands in .opencode/commands/ or the TaskManager subagent instead." >&2
exit 2
