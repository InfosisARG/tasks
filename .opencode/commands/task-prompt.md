---
description: Generate a task scaffold prompt from template with provided arguments
agent: OpenAgent
---

1. Read the task_name from `$1` (e.g., "Terraform").
   If `$1` is missing, ask the user for the task_name.

2. Load skill: opencode-tasks-scaffold `task_name`