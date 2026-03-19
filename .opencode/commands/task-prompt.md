---
description: Generate a task scaffold prompt from template with provided arguments
agent: OpenAgent
---

1. Read the task name from `$1` (e.g., "Terraform").
   If `$1` is missing, ask the user for the task name.

2. Derive `task_slug` from task name:
   - Convert to kebab-case: "Terraform" → "terraform"
   - Use lowercase with hyphens

3. Read the base template from `provision/prompts/tasks/scaffold-template.prompt.md`.

4. Replace placeholders:
   - `{{task_name}}` → task name (capitalized)
   - `{{task_slug}}` → kebab-case slug

5. Create directory: `provision/prompts/tasks/{{task_slug}}/`

6. Write the generated prompt to: `provision/prompts/tasks/{{task_slug}}/implement-v1.prompt.md`

7. Create `provision/prompts/tasks/{{task_slug}}/README.md`:
   ```markdown
   # {{task_name}}

   Task template for {{task_name}}.

   ## Files

   - `implement-v1.prompt.md` - Implementation prompt
   ```

8. Report files created.