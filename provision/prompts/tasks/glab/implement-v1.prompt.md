# Prompt: Agregar nueva Taskfile template

## Objetivo

Implementar soporte para: **glab**

Crear `src/glab/Taskfile.yml` integrado con la arquitectura del repositorio.

---

## Contexto

Ver convenciones en: `@.opencode/context/project/task-templates.md`

---

## Placeholders

| Placeholder     | Uso                         |
| --------------- | --------------------------- |
| `{{task_name}}` | Nombre legible: "glab" |
| `{{task_slug}}` | Slug: "glab"           |

## Estructura Base

```yaml
version: "3"

tasks:
  check:
    desc: Exist glab and dependences
    run: once
    deps:
      - task: check:glab

  check:glab:
    desc: Exist glab
    run: once
    preconditions:
      - sh: command -v glab
        msg: "Please Install glab"

  setup:
    desc: Setup glab dependences.
    run: once
    cmds:
      - <setup_command>
    deps:
      - task: check

  fmt:
    desc: Format files glab.
    run: once
    cmds:
      - <fmt_command>
    deps:
      - task: check

  lint:
    desc: Run linter glab.
    run: once
    cmds:
      - <lint_command>
    deps:
      - task: check

  test:
    desc: Run tests glab.
    run: once
    cmds:
      - <test_command>
    deps:
      - task: check
```

## Salida

1. Contenido de `src/glab/Taskfile.yml`
2. Descripcion breve de tareas incluidas
3. Variables requeridas (si las hay)

## Validacion

```bash
task glab
task -l src/glab/Taskfile.yml
```