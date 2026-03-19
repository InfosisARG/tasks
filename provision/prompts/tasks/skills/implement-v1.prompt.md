# Prompt: Agregar nueva Taskfile template

## Objetivo

Implementar soporte para: **Skills**

Crear `src/skills/Taskfile.yml` integrado con la arquitectura del repositorio.

---

## Contexto

Ver convenciones en: `@.opencode/context/project/task-templates.md`

---

## Placeholders

| Placeholder     | Uso                         |
| --------------- | --------------------------- |
| `{{task_name}}` | Nombre legible: "skills" |
| `{{task_slug}}` | Slug: "skills"           |

## Estructura Base

```yaml
version: "3"

tasks:
  check:
    desc: Exist skills and dependencies
    run: once
    deps:
      - task: check:skills

  check:skills:
    desc: Exist skills
    run: once
    preconditions:
      - sh: command -v skills
        msg: "Please Install skills"

  setup:
    desc: setup package skills.
    run: once
    cmds:
      - echo "TODO: Implement skill setup logic"
    deps:
      - task: check:skills

  sync:
    desc: Sync skills with AGENTS.md and context.
    run: once
    cmds:
      - echo "TODO: Implement skill sync logic"
    deps:
      - task: check:skills
```

## Salida

1. `src/skills/Taskfile.yml`
2. Breve descripcion de tareas incluidas
3. Variables requeridas (si las hay)

## Validacion

```bash
task skills
task -l src/skills/Taskfile.yml
```