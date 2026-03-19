# Taskfile Template Conventions

## Proposito

Este documento define las convenciones para crear y mantener Taskfile templates en `src/<tool>/Taskfile.yml`.

## Estructura Base

```yaml
version: "3"

tasks:
  check:
    desc: Exist <tool> and dependences
    run: once
    deps:
      - task: check:<tool>

  check:<tool>:
    desc: Exist <tool>
    run: once
    preconditions:
      - sh: command -v <tool>
        msg: "Please Install <tool>"

  setup:
    desc: Setup <tool> dependences.
    run: once
    cmds:
      - <setup-command>
    deps:
      - task: check

  fmt:
    desc: Format files <tool>.
    run: once
    cmds:
      - <fmt-command>
    deps:
      - task: check
```

## Convenciones Obligatorias

| Regla            | Detalle                         |
| ---------------- | ------------------------------- |
| `version: "3"`   | Siempre v3                      |
| `desc:`          | Obligatorio en todas las tareas |
| `run: once`      | Para tareas idempotentes        |
| `deps:`          | Encadenar precondiciones        |
| `preconditions:` | Verificar binaries/env vars     |
| 2 spaces         | Indent en YAML                  |
| `\|\| true`      | Solo si es intencional          |

## Tareas Comunes

| Tarea          | Proposito                         | Ejemplo          |
| -------------- | --------------------------------- | ---------------- |
| `check`        | Validar precondiciones y binaries | deps: check:tool |
| `check:<tool>` | Verificar binary existe           | preconditions    |
| `setup`        | Instalar/configurar dependencias  | npm install      |
| `fmt`          | Formatear codigo                  | prettier fmt     |
| `lint`         | Ejecutar linter                   | eslint lint      |
| `test`         | Ejecutar tests                    | pytest           |
| `build`        | Compilar/build                    | docker build     |
| `publish`      | Publicar artefactos               | docker push      |
| `clean`        | Limpiar archivos generados        | rm -rf dist      |
| `docs`         | Generar documentacion             | mkdocs build     |

## Tareas por Categoria

### Runtime (go, python, node)

```yaml
check, setup, fmt, lint, test, build
```

### IaC (terraform, ansible)

```yaml
check, fmt, validate, docs
```

### Containers (docker)

```yaml
check, login, build, publish
```

### Documentation (mkdocs, confluence)

```yaml
check, build, serve
```

### Release

```yaml
check, version, changelog
```

## Patrones Reutilizables

### Check Pattern

```yaml
check:
  deps:
    - task: check:tool
    - task: check:vars

check:tool:
  preconditions:
    - sh: command -v tool
      msg: "Please Install tool"

check:vars:
  preconditions:
    - sh: test -v REQUIRED_VAR
      msg: "Please set REQUIRED_VAR"
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

### CLI_ARGS Pattern

```yaml
fmt:
  cmds:
    - prettier --write '{{.CLI_ARGS}}'
```

## Variables Disponibles

Del Taskfile raiz (`Taskfile.yml`):

```yaml
PROJECT_NAME, ORGANIZATION, APP_TAG, DOCKER_PLATFORM USER, REVIEWERS PYTHON_VERSION, NODE_VERSION, TERRAFORM_VERSION, GOLANGCI_VERSION
```

## Configuracion

### Archivo de Configuracion

Si la herramienta usa config files, referenciarlos:

```yaml
fmt:
  cmds:
    - prettier --config=.ci/linters/prettier.config.cjs .
```

### Archivos de Linters Comunes

```
.ci/linters/
├── prettier.config.cjs
├── biome.json
├── eslint.config.js
├── .golangci.yml
└── .ruff.toml
```

## Prompts de Generacion

Los prompts en `provision/prompts/tasks/` generan templates siguiendo estas convenciones:

- `biomejs/implement-v1.prompt.md` - Template para BiomeJS
- `scaffold-template.prompt.md` - Template general

## Referencia

- `AGENTS.md`: Convenciones generales y herramientas
- `src/<tool>/codemap.md`: Documentacion de templates existentes
- `.editorconfig`: Indentacion por extension