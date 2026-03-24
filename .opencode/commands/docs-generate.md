---
description: Generate documentation for a task from its Taskfile
---

1. Read input from `{{args}}`
2. Extract:
   - task_slug = first word (e.g., "glab", "terraform")
3. Validate:
   - If empty → ask user for task_slug
   - Check if src/{{task_slug}}/Taskfile.yml exists
4. Execute:
   - Create docs/tasks/{{task_slug}}.md with:
     - Header with task name
     - Table of tasks (task | description)
     - Detailed sections for each task with commands, deps, preconditions
   - Add to provision/generators/README.yaml if not exists:
     - Line: `  - docs/tasks/{{task_slug}}.md`
   - Run `task readme` to regenerate README.md