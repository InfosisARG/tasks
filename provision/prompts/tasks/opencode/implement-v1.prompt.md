# Prompt: Agregar nueva Taskfile template

## Objetivo

Implementar soporte para: **Opencode**

Crear `src/opencode/Taskfile.yml` integrado con la arquitectura del repositorio.

---

## Contexto

Ver convenciones en: `@.opencode/context/project/task-templates.md`

---

## Placeholders

| Placeholder     | Uso                         |
| --------------- | --------------------------- |
| `{{task_name}}` | Nombre legible: "opencode" |
| `{{task_slug}}` | Slug: "opencode"           |

## Estructura Base

```yaml
version: "3"

tasks:
  check:
    desc: Exist Opencode and dependences
    run: once
    deps:
      - task: check:opencode

  check:opencode:
    desc: Exist Opencode
    run: once
    preconditions:
      - sh: command -v opencode
        msg: "Please Install Opencode"

  setup:
    desc: Setup Opencode dependences.
    run: once
    cmds:
      - curl -fsSL https://opencode.ai/install | bash
    deps:
      - task: check
```

## Salida

1. Contenido de `src/opencode/Taskfile.yml`
2. Descripcion breve de tareas incluidas
3. Variables requeridas (si las hay)

## Validacion

```bash
task opencode
task -l src/opencode/Taskfile.yml
```