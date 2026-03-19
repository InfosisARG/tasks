# Prompt: Agregar nueva Taskfile template

## Objetivo

Implementar soporte para: **{{task_name}}**

Crear `src/{{task_slug}}/Taskfile.yml` integrado con la arquitectura del repositorio.

---

## Contexto

Ver convenciones en: `@.opencode/context/project/task-templates.md`

---

## Placeholders

| Placeholder         | Uso                         |
| ------------------- | --------------------------- |
| `{{task_name}}`     | Nombre legible: "Terraform" |
| `{{task_slug}}`     | Slug: "terraform"           |
| `{{tool_command}}`  | Comando: "terraform"        |
| `{{setup_command}}` | Comando de setup            |
| `{{fmt_command}}`   | Comando de format           |
| `{{lint_command}}`  | Comando de lint             |
| `{{test_command}}`  | Comando de test             |

---

## Estructura Base

```yaml
version: "3"

tasks:
  check:
    desc: Exist {{task_name}} and dependences
    run: once
    deps:
      - task: check:{{task_slug}}

  check:{{task_slug}}:
    desc: Exist {{task_name}}
    run: once
    preconditions:
      - sh: command -v {{tool_command}}
        msg: "Please Install {{task_name}}"

  setup:
    desc: Setup {{task_name}} dependences.
    run: once
    cmds:
      - { { setup_command } }
    deps:
      - task: check

  fmt:
    desc: Format files {{task_name}}.
    run: once
    cmds:
      - { { fmt_command } }
    deps:
      - task: check

  lint:
    desc: Run linter {{task_name}}.
    run: once
    cmds:
      - { { lint_command } }
    deps:
      - task: check

  test:
    desc: Run tests {{task_name}}.
    run: once
    cmds:
      - { { test_command } }
    deps:
      - task: check
```

---

## Salida

1. Contenido de `src/{{task_slug}}/Taskfile.yml`
2. Descripcion breve de tareas incluidas
3. Variables requeridas (si las hay)

## Validacion

```bash
task prettier
task -l src/{{task_slug}}/Taskfile.yml
```