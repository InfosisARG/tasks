---
description: Generate a task scaffold prompt from template with provided arguments
---

1. Read input from `{{args}}`
2. Extract:
   - task_name = first word
3. Validate:
   - If empty → ask user for task_name
4. Execute:
   - Load skill: opencode-tasks-scaffold
     with:
       task_name: task_name