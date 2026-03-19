# AGENTS.md

This repo is a collection of reusable `Taskfile.yml` templates. The main entrypoint is `Taskfile.yml` (go-task v3).

## Key Tools

- Task runner: `task`
- Python tooling: `uv` (config in `pyproject.toml`)
- Formatting: `prettier` (via `task prettier`)
- Lint gates: `pre-commit` (CI runs `pre-commit run --all-files`)

Generated files:

- `README.md` is generated from `provision/generators/README.yaml` + `provision/templates/README.tpl.md` (run `task readme`). Do not hand-edit `README.md`.

Cursor/Copilot rules:

- No `.cursor/rules/`, `.cursorrules`, or `.github/copilot-instructions.md` present.

## Build / Lint / Test Commands

List available tasks:

```bash
task -l
```

Local setup (creates `.env` from `.env.example`, installs deps, installs hooks):

```bash
task setup
```

Preflight checks (toolchain present):

```bash
task check
```

Format (Prettier + Terraform fmt):

```bash
task prettier
```

Python lint/format/typecheck (via `src/uv/Taskfile.yml`):

```bash
task uv:setup
task uv:fmt
task uv:lint
```

Run all pre-commit hooks (matches CI):

```bash
uv run pre-commit run --all-files --show-diff-on-failure
```

Docs build/serve:

```bash
task docs:build
task docs:serve
```

Tests:

```bash
task test
```

### Run A Single Test

Python (pytest examples):

```bash
uv run pytest -q tests/test_file.py
uv run pytest -q tests/test_file.py::test_name
uv run pytest -q -k "expr"
```

Go (go test examples):

```bash
go test -v ./path/to/pkg
go test -v ./path/to/pkg -run '^TestName$'
```

## Code Style Guidelines

### Formatting & whitespace

Follow `.editorconfig`:

- 2 spaces: `*.{md,yml,yaml,json,toml,js,ts,tsx,sh,tf,hcl}`
- 4 spaces: `*.py`
- tabs: `*.go`, `Makefile`
- `end_of_line=lf`, trim trailing whitespace

### Taskfile conventions (most edits in this repo)

- Use `version: "3"` and keep file name `Taskfile.yml`.
- Prefer namespaced tasks: `area:verb` (examples: `uv:lint`, `docs:build`).
- Always set `desc:`; use `deps:` for prerequisites; use `preconditions:` for binaries/required env vars.
- If a task should support “single file/single test”, accept and forward `{{.CLI_ARGS}}`.
- Keep tasks non-interactive; ensure commands fail on errors.

### Python style (configured in `pyproject.toml`)

- Format: `ruff format` (line length 90).
- Lint: `ruff check` (includes import sorting).
- Types: `mypy` is `strict = true`; avoid untyped public functions.
- Error handling: raise specific exceptions; avoid `except:` / swallowing errors (ruff enables blind-except checks).

### Go style (lint config present)

- Format: `gofmt -s`.
- Imports: `goimports` with local prefix `github.com/infosisarg/` (see `.ci/linters/.golangci.yml`).
- Lint: `golangci-lint run --config .ci/linters/.golangci.yml`.

### JS/TS style (for config/scripts)

- Prefer Prettier formatting (see `task prettier`).
- ESLint rules live in `.ci/linters/.eslintrc.js`.

### Documentation

- Keep docs command examples aligned with actual tasks.
- If updating the README content, change its sources and run `task readme`.

## Git / PR Requirements

- Commits: Conventional Commits are expected (commit-msg hook uses commitlint).
- PR titles: semantic types enforced via `.github/semantic.yml`: `feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert|release|hotfix: ...`
- Secret scanning: pre-commit runs `detect-private-key` and `gitleaks`; never commit credentials.
