# AGENTS.md

This repo is a collection of reusable `Taskfile.yml` templates. The main entrypoint is `Taskfile.yml` (go-task v3).

## Key Tools

| Tool         | Purpose                     | Version Config            |
| ------------ | --------------------------- | ------------------------- |
| `task`       | Task runner (go-task v3)    | N/A                       |
| `uv`         | Python package manager      | N/A                       |
| `ruff`       | Python linting + formatting | `pyproject.toml`          |
| `mypy`       | Python type checking        | `pyproject.toml` (strict) |
| `pre-commit` | Git hooks                   | `.pre-commit-config.yaml` |
| `prettier`   | Multi-language formatting   | N/A                       |
| `terraform`  | IaC tooling                 | `TERRAFORM_VERSION` var   |

**IMPORTANT**: `README.md` is GENERATED from `provision/generators/README.yaml` + `provision/templates/README.tpl.md`. Run `task readme` after modifying YAML sources. **Do not hand-edit README.md**.

## Build / Lint / Test Commands

### Quick Start

```bash
task setup      # Create .env, install deps, setup hooks
task check      # Verify toolchain dependencies
task prettier   # Format all files (Prettier + Terraform fmt)
task validate   # Run pre-commit hooks (matches CI)
```

### Python (via uv)

```bash
task uv:setup       # Install Python dependencies
task uv:fmt         # Format with ruff (line length 90)
task uv:lint        # Lint with ruff + mypy type check
task uv:test        # Run pytest with coverage
```

### Run A Single Test

```bash
# Python/pytest
uv run pytest -q tests/test_file.py
uv run pytest -q tests/test_file.py::test_name
uv run pytest -q -k "pattern_match"

# Go
go test -v ./path/to/pkg
go test -v ./path/to/pkg -run '^TestName$'
```

### Documentation

```bash
task docs:build      # Build MkDocs site
task docs:serve      # Serve locally for preview
task readme          # Regenerate README.md from templates
```

### Pre-commit (Full CI Pipeline)

```bash
uv run pre-commit run --all-files --show-diff-on-failure
```

## Code Style Guidelines

### Indentation (from .editorconfig)

| Extension                             | Indent   | Notes                 |
| ------------------------------------- | -------- | --------------------- |
| `*.py`                                | 4 spaces | Python only           |
| `*.go`                                | tabs     | Go uses tabs          |
| `*.{yml,yaml,json,toml,md,sh,tf,hcl}` | 2 spaces | Most config files     |
| `Makefile`                            | tabs     | Makefiles always tabs |

**Global rules**: `end_of_line=lf`, `trim_trailing_whitespace=true`, `charset=utf-8`

### Taskfile Conventions

```yaml
version: "3" # Always use v3

tasks:
  namespace:verb: # Namespaced naming: uv:lint, docs:build
    desc: "Description" # REQUIRED: always provide desc
    run: once # Use for idempotent tasks
    deps: # Dependencies (executed first)
      - task: check:tool
    preconditions: # Prerequisites validation
      - sh: command -v tool
        msg: "Install tool first"
    cmds:
      - command {{.VARS}} # Use template variables
```

**Rules**:

- Accept `{{.CLI_ARGS}}` for single-file operations
- Keep tasks non-interactive (CI-friendly)
- Commands must fail on errors (no `|| true` unless intentional)

### Python Style (pyproject.toml)

**Key ruff rules enabled**:

- `I` - Import sorting
- `BLE` - No bare except (catches `except:`)
- `S` - Security (bandit)
- `B` - Bugbear best practices
- `N` - PEP8 naming conventions
- `PLE`, `PLR` - Pylint rules

**Type annotations**: `mypy strict = true` - no untyped public functions

**Error handling**: Raise specific exceptions; never swallow errors.

### Go Style

```bash
gofmt -s              # Format
goimports             # Format + organize imports
golangci-lint run     # Full linting
```

**Import conventions**: Local prefix `github.com/infosisarg/`

## Git / PR Requirements

### Commits

- **Format**: Conventional Commits (enforced by commitlint)
- **Types**: `feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert|release|hotfix`
- **Format**: `<type>(<scope>): <description>` or `<type>: <description>`

### PR Titles

Enforced via `.github/semantic.yml`:

```
feat: add new template
fix(docker): resolve build timeout
docs: update README generation
```

### Security

- Pre-commit runs `detect-private-key` and `gitleaks`
- **Never commit credentials, keys, or secrets**
- Use `.env.example` for template variables

## Cursor/Copilot Rules

No `.cursor/rules/`, `.cursorrules`, or `.github/copilot-instructions.md` present.

## Repository Structure

```
├── Taskfile.yml         # Main entry point
├── src/                 # 40+ Taskfile templates by tool
├── provision/           # README generation pipeline
├── .ci/linters/         # CI linting configs
└── codemap.md           # Repository codemap
```