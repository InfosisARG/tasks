# Prompt: Generar Taskfile Template

**Objetivo**: Crear `src/<nombre>/Taskfile.yml` para: **{{TOOL_NAME}}**

Sigue las reglas de `AGENTS.md` estrictamente.

---

## Estructura Base

```yaml
version: "3"

tasks:
  check:
    desc: Exist {{TOOL_NAME}} and dependences
    run: once
    deps:
      - task: check:{{TOOL_NAME_LOWER}}

  check:{{TOOL_NAME_LOWER}}:
    desc: Exist {{TOOL_NAME}}
    run: once
    preconditions:
      - sh: command -v {{TOOL_COMMAND}}
        msg: "Please Install {{TOOL_NAME}}"

  setup:
    desc: Setup {{TOOL_NAME}} dependences.
    run: once
    cmds:
      - { { SETUP_COMMAND } }
    deps:
      - task: check

  fmt:
    desc: Format files {{TOOL_NAME}}.
    run: once
    cmds:
      - { { FMT_COMMAND } }
    deps:
      - task: check

  lint:
    desc: Run linter {{TOOL_NAME}}.
    run: once
    cmds:
      - { { LINT_COMMAND } }
    deps:
      - task: check

  test:
    desc: Run tests {{TOOL_NAME}}.
    run: once
    cmds:
      - { { TEST_COMMAND } }
    deps:
      - task: check
```

---

## Convenciones (AGENTS.md)

| Regla            | Detalle            |
| ---------------- | ------------------ |
| `version: "3"`   | Siempre v3         |
| `desc:`          | Obligatorio        |
| `run: once`      | Idempotente        |
| `deps:`          | Precondiciones     |
| `preconditions:` | Verificar binaries |
| 2 spaces         | Indent YAML        |
| `\|\| true`      | Solo intencional   |

### Nomenclatura

- **Namespace**: `area:accion` → `python:fmt`, `docker:build`
- **Common verbs**: `check`, `setup`, `fmt`, `lint`, `test`, `build`, `publish`

---

## Patrones Comunes

### Check Pattern

```yaml
check:
  deps:
    - task: check:tool

check:tool:
  preconditions:
    - sh: command -v tool
      msg: "Please Install tool"
```

### Variable Propagation

```yaml
tasks:
  build:
    cmds:
      - docker build --tag {{.CI_REGISTRY}}/{{.PROJECT_NAME}}:{{.APP_TAG}}
```

### Deps Dependencies

```yaml
build:
  deps:
    - task: login
    - task: check
```

---

## Variables Disponibles

```yaml
PROJECT_NAME, ORGANIZATION, APP_TAG, DOCKER_PLATFORM PYTHON_VERSION, NODE_VERSION, TERRAFORM_VERSION
```

---

## Tareas por Categoria

| Categoria  | Tareas Tipicas                       |
| ---------- | ------------------------------------ |
| Runtime    | check, setup, fmt, lint, test, build |
| IaC        | check, fmt, validate, docs           |
| Containers | check, login, build, publish         |
| Docs       | check, build, serve                  |
| Release    | check, version, changelog            |

---

## Salida

1. `src/{{TOOL_SLUG}}/Taskfile.yml`
2. Descripcion breve de tareas
3. Variables requeridas (si hay)

## Validacion

```bash
task prettier
task -l src/{{TOOL_SLUG}}/Taskfile.yml
```
