# src/ Directory

## Responsibility

Organizes reusable Taskfile templates by tool/language ecosystem. These templates provide standardized CI/CD, development, and operational tasks that can be included into project-specific `Taskfile.yml` files using Task's `includes` directive.

## Design

### Template Categories

#### Language Runtimes

| Category | Path          | Description                                                               |
| -------- | ------------- | ------------------------------------------------------------------------- |
| Python   | `src/python/` | Python project tooling with configurable package manager (defaults to uv) |
| Go       | `src/go/`     | Go module management, formatting, linting, testing                        |
| Node.js  | `src/node/`   | Node/npm project tasks                                                    |
| Bun      | `src/bun/`    | Bun runtime setup and installation                                        |
| Yarn     | `src/yarn/`   | Yarn package management tasks                                             |

#### Infrastructure as Code

| Category   | Path              | Description                                                       |
| ---------- | ----------------- | ----------------------------------------------------------------- |
| Terraform  | `src/terraform/`  | Terraform formatting, documentation generation, environment setup |
| Terragrunt | `src/terragrunt/` | Terragrunt wrapper tasks                                          |
| Packer     | `src/packer/`     | Packer image building                                             |
| Ansible    | `src/ansible/`    | Ansible playbook execution                                        |
| K8s        | `src/k8s/`        | Kubernetes manifests and kubectl tasks                            |

#### DevOps & Containers

| Category | Path          | Description                                  |
| -------- | ------------- | -------------------------------------------- |
| Docker   | `src/docker/` | Docker image build, login, and publish       |
| AWS      | `src/aws/`    | AWS CLI operations and credential management |

#### Development Tools

| Category   | Path              | Description                                  |
| ---------- | ----------------- | -------------------------------------------- |
| Prettier   | `src/prettier/`   | Multi-language code formatting               |
| Pre-commit | `src/pre-commit/` | Git hooks management                         |
| Docs       | `src/docs/`       | MkDocs documentation build/serve             |
| SonarQube  | `src/sonar/`      | SonarQube scanning via Docker                |
| Git        | `src/git/`        | Git configuration and ignore file generation |

#### Release & Versioning

| Category  | Path             | Description                                 |
| --------- | ---------------- | ------------------------------------------- |
| Version   | `src/version/`   | Semantic version bumping                    |
| Release   | `src/release/`   | Release orchestration (version + changelog) |
| Changelog | `src/changelog/` | git-chglog changelog generation             |

#### Collaboration

| Category   | Path              | Description                          |
| ---------- | ----------------- | ------------------------------------ |
| Confluence | `src/confluence/` | Mark-based documentation sync        |
| GitHub     | `src/github/`     | GitHub CLI operations, PR management |

#### Security & Keys

| Category | Path           | Description                           |
| -------- | -------------- | ------------------------------------- |
| SSH      | `src/ssh/`     | SSH key generation and PEM management |
| SOPS     | `src/sops/`    | SOPS secrets encryption               |
| Keybase  | `src/keybase/` | Keybase operations                    |

#### Other Tools

| Category  | Path             | Description                    |
| --------- | ---------------- | ------------------------------ |
| Maven     | `src/maven/`     | Java/Maven build tasks         |
| Gradle    | `src/gradle/`    | Gradle build tasks             |
| Flutter   | `src/flutter/`   | Flutter SDK tasks              |
| Android   | `src/android/`   | Android SDK tasks              |
| Coursier  | `src/coursier/`  | Coursier dependency manager    |
| Multipass | `src/multipass/` | Multipass VM management        |
| PlantUML  | `src/plantuml/`  | UML diagram generation         |
| OpenSSL   | `src/openssl/`   | OpenSSL certificate operations |
| Lua       | `src/lua/`       | Lua tooling                    |
| Poetry    | `src/poetry/`    | Poetry package manager         |
| Pnpm      | `src/pnpm/`      | pnpm package manager           |
| Renovate  | `src/renovate/`  | Renovate bot configuration     |
| Mark      | `src/mark/`      | Mark documentation sync        |

### Common Patterns

#### Check Pattern

Every template provides a `check` task that validates prerequisites:

```yaml
tasks:
  check:
    desc: Exist <tool> and dependences
    run: once
    deps:
      - task: check:tool
      - task: check:dependencies

  check:tool:
    desc: Exist <tool>
    run: once
    preconditions:
      - sh: command -v <tool>
        msg: "Please Install <tool>"
```

#### Environment Variables

Templates use environment variables for configuration:

| Variable                 | Purpose                             |
| ------------------------ | ----------------------------------- |
| `PYTHON_PACKAGE_MANAGER` | Package manager choice (uv, poetry) |
| `AWS_PROFILE_NAME`       | AWS CLI profile                     |
| `CI_REGISTRY_*`          | Container registry credentials      |
| `APP_TAG`                | Application version/tag             |
| `SONAR_URL`              | SonarQube server URL                |
| `CONFLUENCE_*`           | Confluence credentials              |

#### Run-once Pattern

Tasks use `run: once` to prevent redundant execution:

```yaml
tasks:
  setup:
    desc: Setup dependencies
    run: once # Prevents re-running if already done
    cmds:
      - package-manager install
```

#### Deps Dependencies

Tasks declare dependencies to enforce execution order:

```yaml
tasks:
  publish:
    desc: Publish artifact
    deps:
      - task: check # Prerequisites
      - task: build # Build first
    cmds:
      - publish command
```

## Flow

Templates follow a consistent lifecycle:

1. **Check Phase**: Validate toolchain and environment variables
2. **Setup Phase**: Install dependencies if needed
3. **Execute Phase**: Run the actual task (fmt, test, build, etc.)

## Integration

### Template Dependencies

```
src/version/
    └── src/release/ (uses version + changelog)

src/changelog/
    └── src/release/ (integrated)

src/pre-commit/
    └── Used by: src/python/, src/uv/

src/docker/
    └── Requires: CI_REGISTRY_USER, CI_REGISTRY_PASSWORD, CI_REGISTRY

src/sonar/
    └── Requires: SONAR_URL, SONAR_TOKEN

src/confluence/
    └── Requires: CONFLUENCE_BASE_URL, CONFLUENCE_ACCESS_TOKEN, CONFLUENCE_USER

src/terraform/
    └── Requires: AWS_PROFILE_NAME, ORGANIZATION
```

### Usage Example

Include a template in project `Taskfile.yml`:

```yaml
version: "3"

includes:
  - task: src/uv:fmt
  - task: src/go:lint
  - task: src/docker:build

tasks:
  ci:
    desc: Run CI pipeline
    cmds:
      - task: uv:lint
      - task: uv:test
      - task: docker:build
      - task: docker:publish
```

### Key Design Principles

1. **Composability**: Templates are self-contained and can be combined arbitrarily
2. **Validation**: Every template validates prerequisites before execution
3. **Idempotency**: Tasks use `run: once` and `status` checks to be safely re-runnable
4. **Environment-driven**: Configuration via environment variables enables CI/CD integration
5. **Documentation-first**: terraform-docs, mkdocs patterns for self-documenting infrastructure
