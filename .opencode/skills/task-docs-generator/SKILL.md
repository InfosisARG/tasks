---
name: task-docs-generator
description: Generate documentation for a task from its Taskfile and update README.yaml
---

# Task Docs Generator Skill

## Trigger phrases

- "genera documentacion de task"
- "genera docs para task"
- "genera documentacion de glab"
- "docs-generate"
- "task-docs"

## What I do

1. Extract `task_slug` from user input (first word)
2. Validate that `src/<task_slug>/Taskfile.yml` exists
3. Generate `docs/tasks/<task_slug>.md` with:
   - Header with task name
   - Table of tasks (task | description)
   - Detailed sections for each task with commands, deps, preconditions
4. Add to `provision/generators/README.yaml` if not exists:
   - Line: `  - docs/tasks/<task_slug>.md`
5. Run `task readme` to regenerate README.md

## Input

- `task_slug`: Name of the task (e.g., "glab", "terraform", "go")

## Output

- `docs/tasks/<task_slug>.md`: Generated documentation
- Updated `provision/generators/README.yaml`
- Regenerated `README.md`

## Implementation

Run the Python script from the skill:

```bash
python3 .claude/skills/task-docs-generator/scripts/generate_task_docs.py <task_slug>
task readme
```

## Example

- Input: `/docs-generate glab`
- Output:
  - Creates `docs/tasks/glab.md`
  - Adds `  - docs/tasks/glab.md` to `provision/generators/README.yaml`
  - Runs `task readme`