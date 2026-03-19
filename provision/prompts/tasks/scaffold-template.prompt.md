# Prompt: Agregar nueva Taskfile template a tasks

## Objetivo

Implementar soporte para: **{{task_name}}**

Crear `src/{{task_slug}}/Taskfile.yml` integrado con la arquitectura del repositorio.

---

## Reglas Obligatorias (AGENTS.md)

| Regla            | Detalle                         |
| ---------------- | ------------------------------- |
| `version: "3"`   | Siempre v3                      |
| `desc:`          | Obligatorio en todas las tareas |
| `run: once`      | Para tareas idempotentes        |
| `deps:`          | Encadenar precondiciones        |
| `preconditions:` | Verificar binaries/env vars     |
| 2 spaces         | Indent en YAML                  |
| `\|\| true`      | Solo si es intencional          |

### Nomenclatura

```yaml
tasks:
  namespace:verb: # area:accion
  check: # Verificar precondiciones
  setup: # Instalar dependencias
  fmt: # Formatear codigo
  lint: # Ejecutar linter
  test: # Ejecutar tests
  build: # Compilar/Build
  publish: # Publicar artefactos
```

---

## Estructura Requerida

```yaml
version: "3"

tasks:
  check:
    desc: Exist {{task_name}} and dependences
    run: once
    deps:
      - task: check:{{task_name_slug}}

  check:{{task_name_slug}}:
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

## Patrones Comunes

### Check Pattern

```yaml
check:
  deps:
    - task: check:tool
    - task: check:dependencies

check:tool:
  preconditions:
    - sh: command -v tool
      msg: "Please Install tool"
```

### Deps Dependencies

```yaml
build:
  deps:
    - task: login
    - task: check
```

### Variable Propagation

```yaml
build:
  cmds:
    - docker build --tag {{.CI_REGISTRY}}/{{.PROJECT_NAME}}:{{.APP_TAG}}
```

---

## Variables Disponibles

```yaml
PROJECT_NAME, ORGANIZATION, APP_TAG, DOCKER_PLATFORM USER, REVIEWERS PYTHON_VERSION, NODE_VERSION, TERRAFORM_VERSION, GOLANGCI_VERSION
```

---

## Tareas por Categoria

| Categoria                | Tareas Tipicas                       |
| ------------------------ | ------------------------------------ |
| Runtime (go, python)     | check, setup, fmt, lint, test, build |
| IaC (terraform, ansible) | check, fmt, validate, docs           |
| Containers (docker)      | check, login, build, publish         |
| Docs (mkdocs)            | check, build, serve                  |
| Release                  | check, version, changelog            |

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
