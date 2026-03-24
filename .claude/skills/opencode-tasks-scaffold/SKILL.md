---
name: opencode-tasks-scaffold
description: Genera prompts de task templates a partir del template base
metadata:
  opencode:
    emoji: 📝
    tags:
      - opencode
      - taskfile
      - scaffold
---

# Task Prompt Generator

Genera scaffolds de prompts para nuevas task templates.

## Uso

```
/task-prompt <task_name>
```

## Ejemplo

```
/task-prompt Terraform
```

Genera:
- `provision/prompts/tasks/terraform/implement-v1.prompt.md`
- `provision/prompts/tasks/terraform/README.md`

## Derivaciones automáticas

| Input | Derivado |
|-------|----------|
| `task_name` | `Terraform` |
| `task_slug` | `terraform` (kebab-case) |

## Errores

- Si falta `task_name` → pide el nombre
- Si el directorio ya existe → confirma antes de sobrescribir