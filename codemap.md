# Repository Atlas: tasks

## Project Responsibility

A collection of reusable `Taskfile.yml` templates for standardizing common DevOps and development tasks across projects. This repository provides drop-in task definitions for various tools and languages that can be included via Go Task's `includes` mechanism.

## System Entry Points

| Entry Point      | Purpose                                                                           |
| ---------------- | --------------------------------------------------------------------------------- |
| `Taskfile.yml`   | Main orchestrator - includes all `src/` templates and defines project-level tasks |
| `pyproject.toml` | Python project configuration with uv-based tooling (lint, test, docs, dev deps)   |
| `AGENTS.md`      | Claude/OpenCode agent instructions and coding conventions                         |
| `.goji.json`     | Commit message conventions (emoji prefixes, scopes, signoff rules)                |
| `opencode.json`  | OpenCode AI agent configuration (plugins, models, MCP servers, permissions)       |
| `infobot.toml`   | Infobot configuration for Jira integration and commit derivation                  |

## Directory Map (Aggregated)

| Directory | Responsibility | Key Tasks |
| --- | --- | --- |
| `src/changelog/` | Git changelog generation with git-chglog | `generate`, `tag`, `next` |
| `src/confluence/` | Sync markdown docs to Atlassian Confluence via Mark | `sync`, `sync:all`, `sync:develop`, `sync:main` |
| `src/uv/` | Python tooling via uv package manager | `setup`, `fmt`, `lint`, `test`, `precommit` |
| `src/python/` | Python project setup and testing | `setup`, `fmt`, `test`, `precommit` |
| `src/git/` | Git configuration and .gitignore generation | `setup`, `ignore`, `reviews` |
| `src/docs/` | MkDocs documentation build and serve | `build`, `serve`, `show` |
| `src/docker/` | Docker image build and publish to registries | `login`, `build`, `publish` |
| `src/version/` | Semantic versioning with bump-my-version | `major`, `minor`, `patch`, `pre_release` |
| `src/release/` | Release workflow combining version + changelog | `major`, `minor`, `patch`, `pre_release` |
| `src/plantuml/` | PlantUML diagram generation via Docker | `make` |
| `src/prettier/` | Code formatting via Prettier (JS/TS/MD/YAML/etc.) | `all`, `code`, `sass`, `less` |
| `src/sonar/` | SonarQube code quality scanning | `scan`, `show` |
| `src/terraform/` | Terraform formatting, docs, and environment setup | `fmt`, `doc`, `docs:all`, `environment` |
| `src/bun/` | Bun JavaScript runtime installation | `setup` |
| `src/go/` | Go module setup, formatting, linting, testing | `setup`, `fmt`, `lint`, `test`, `build` |
| `src/aws/` | AWS resource management (KMS cleanup, EFS deletion) | `cleanup-kms`, `cleanup-efs` |
| `src/k8s/` | Kubernetes namespace management utilities | `destroy-stuck-ns` |
| `src/ansible/` | Ansible playbook execution | _(see Taskfile)_ |
| `src/coursier/` | Coursier (Scala) dependency management | _(see Taskfile)_ |
| `src/flutter/` | Flutter SDK setup and commands | _(see Taskfile)_ |
| `src/gradle/` | Gradle build tool tasks | _(see Taskfile)_ |
| `src/java/` | Java/Maven project tasks | _(see Taskfile)_ |
| `src/lua/` | Lua scripting tasks | _(see Taskfile)_ |
| `src/mark/` | Mark Markdown-to-Confluence sync | _(see Taskfile)_ |
| `src/maven/` | Maven build tasks | _(see Taskfile)_ |
| `src/molecule/` | Molecule for Ansible testing | _(see Taskfile)_ |
| `src/multipass/` | Multipass VM management | _(see Taskfile)_ |
| `src/node/` | Node.js tooling | _(see Taskfile)_ |
| `src/openssl/` | SSL certificate utilities | _(see Taskfile)_ |
| `src/packer/` | Packer image builder | _(see Taskfile)_ |
| `src/pnpm/` | pnpm package manager | _(see Taskfile)_ |
| `src/pre-commit/` | Pre-commit hook management | _(see Taskfile)_ |
| `src/renovate/` | Renovate dependency updates | _(see Taskfile)_ |
| `src/sops/` | Mozilla SOPS secrets management | _(see Taskfile)_ |
| `src/ssh/` | SSH key management | _(see Taskfile)_ |
| `src/keybase/` | Keybase integration | _(see Taskfile)_ |
| `src/github/` | GitHub CLI workflows | _(see Taskfile)_ |
| `src/terragrunt/` | Terragrunt Infrastructure-as-Code | _(see Taskfile)_ |
| `src/yarn/` | Yarn package manager | _(see Taskfile)_ |
| `provision/diagrams/` | PlantUML diagram generation pipeline | `build`, `publish`, `make` |
| `provision/generators/` | README.md generation from YAML templates | _(template sources)_ |

## Template Organization

### By Language/Runtime

```
Language Runtimes:
├── go/          → Go modules, formatting, linting, testing
├── python/      → Python project setup, testing
├── uv/          → uv-based Python tooling (preferred)
├── node/        → Node.js tooling
├── bun/         → Bun runtime installation
├── pnpm/        → pnpm package manager
├── yarn/        → Yarn package manager
├── java/        → Java projects
├── maven/       → Maven builds
├── gradle/      → Gradle builds
├── coursier/    → Scala/Coursier
├── lua/         → Lua scripting
├── flutter/     → Flutter SDK
└── android/     → Android SDK
```

### By Tool Category

```
IaC & Infrastructure:
├── terraform/   → Terraform formatting, docs, environment
├── terragrunt/   → Terragrunt orchestration
├── ansible/      → Ansible playbook execution
├── molecule/     → Ansible testing framework
├── packer/       → Image building
└── multipass/    → VM management

Containers & Cloud:
├── docker/       → Docker build/publish
├── k8s/          → Kubernetes utilities
├── aws/          → AWS resource management
└── sonar/        → SonarQube scanning

Documentation & Sync:
├── docs/         → MkDocs build/serve
├── confluence/   → Confluence sync via Mark
├── changelog/    → Git changelog generation
├── prettier/     → Code formatting
├── plantuml/     → Diagram generation
└── provision/diagrams/ → PlantUML pipeline

Development Workflow:
├── git/          → Git setup, .gitignore
├── version/      → Semantic versioning
├── release/      → Release workflow
├── pre-commit/   → Pre-commit hooks
├── renovate/     → Dependency updates
├── prettier/     → Code formatting
└── sops/         → Secrets management
```

## Entry Points and Build Process

### Main Taskfile.yml Structure

```yaml
includes: # All src/ templates are included here
  changelog: ./src/changelog/
  confluence: ./src/confluence/
  uv: ./src/uv/
  python: ./src/python/
  git: ./src/git/
  docs: ./src/docs/
  docker: ./src/docker/
  version: ./src/version/
  release: ./src/release/
  plantuml: ./src/plantuml/
  prettier: ./src/prettier/
  sonar: ./src/sonar/
  terraform: ./src/terraform/
  bun: ./src/bun/
  diagrams: ./provision/diagrams/

vars: # Shared variables across all includes
  PROJECT_NAME, ORGANIZATION, etc.

tasks: default      → show summary + task list check        → validate all toolchain dependencies setup        → install dependencies, pre-commit hooks prettier     → format all files validate     → run pre-commit hooks test         → execute test suite readme       → generate README from templates
```

### README Generation Pipeline

```
provision/generators/README.yaml  →  provision/templates/README.tpl.md
                                        ↓ (gomplate)
                                      README.md
```

Run with: `task readme`

## Integration Patterns

### 1. Task Includes Pattern

Projects include templates via Go Task's `includes`:

```yaml
includes:
  terraform: path/to/src/terraform/Taskfile.yml
  docker: path/to/src/docker/Taskfile.yml
```

Tasks are namespaced by include path: `terraform:fmt`, `docker:build`

### 2. Dependency Chaining

Templates use `deps:` to chain tasks:

```yaml
tasks:
  check:
    deps:
      - task: check:docker
      - task: check:vars
  build:
    deps:
      - task: login # Ensures registry auth before build
```

### 3. Variable Propagation

Parent Taskfiles pass variables to includes via `vars:`:

```yaml
tasks:
  docs:prod:
    cmds:
      - task: terraform:command
        vars:
          STAGE: prod
          REGION: us-east-1
```

### 4. Precondition Guards

Templates validate prerequisites before execution:

```yaml
preconditions:
  - sh: command -v terraform
    msg: "Please Install terraform"
  - sh: test -v AWS_PROFILE_NAME
    msg: "Please add var environment AWS_PROFILE_NAME"
```

### 5. Environment Detection

Root Taskfile detects available tools:

```yaml
env:
  DOCKER:
    sh: docker --version 2> /dev/null || echo "not exist"
  PYTHON:
    sh: python --version 2> /dev/null || echo "not exist"
```

## Tool Versions (Default)

| Tool      | Version Variable    | Default  |
| --------- | ------------------- | -------- |
| Python    | `PYTHON_VERSION`    | 3.11.5   |
| Node      | `NODE_VERSION`      | v24.11.1 |
| Terraform | `TERRAFORM_VERSION` | 1.11.4   |
| GolangCI  | `GOLANGCI_VERSION`  | 1.42.0   |

## Detailed Maps

For comprehensive documentation of each directory, see:

| Directory    | Detailed Map                                                               |
| ------------ | -------------------------------------------------------------------------- |
| `src/`       | [View Map](src/codemap.md) - All task templates organized by category      |
| `provision/` | [View Map](provision/codemap.md) - README generation and diagram pipelines |

## Key Tools Reference

| Tool              | Purpose                 | Package Manager |
| ----------------- | ----------------------- | --------------- |
| `task`            | Task runner (go-task)   | Binary          |
| `uv`              | Python package manager  | Binary          |
| `ruff`            | Python linter/formatter | pip             |
| `pre-commit`      | Git hooks               | pip             |
| `mypy`            | Python type checker     | pip             |
| `prettier`        | Code formatter          | npm             |
| `terraform`       | IaC                     | tfenv           |
| `docker`          | Containers              | Binary          |
| `golangci-lint`   | Go linter               | Binary          |
| `git-chglog`      | Changelog generator     | go install      |
| `bump-my-version` | Version bumping         | pip             |
| `mkdocs`          | Documentation           | pip             |