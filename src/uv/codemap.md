# src/uv/

## Responsibility

Provides Python development tasks using `uv` package manager with integrated linting (ruff), type checking (mypy), and testing (pytest) with coverage reporting.

## Design

### Key Tasks

| Task              | Description                            |
| ----------------- | -------------------------------------- |
| `check`           | Validates Python, uv, pre-commit, ruff |
| `check:python`    | Verifies Python installation           |
| `check:uv`        | Verifies uv package manager            |
| `check:precommit` | Verifies pre-commit availability       |
| `check:ruff`      | Verifies ruff linter                   |
| `setup`           | Installs all dependency groups         |
| `fmt`             | Formats code with ruff                 |
| `lint`            | Runs ruff check and mypy               |
| `test`            | Runs pytest via task:pytest            |
| `pytest`          | Runs pytest with coverage              |
| `mypy`            | Runs mypy type checking                |
| `environment`     | Installs Python interpreter            |
| `precommit`       | Installs all Git hook types            |

### Variables

| Variable   | Purpose                                          |
| ---------- | ------------------------------------------------ |
| `CLI_ARGS` | Forwarded to ruff/pytest for selective execution |

### Patterns

- Comprehensive Python toolchain integration
- Coverage report and HTML generation
- Strict mypy type checking
- Pre-commit hook installation for all phases

## Flow

```
check:* → setup → (fmt | lint | test | precommit)
```

## Integration

### Usage in Project Taskfile

```yaml
includes:
  - task: src/uv:lint
  - task: src/uv:test
```

### Required Configuration (pyproject.toml)

- ruff configuration
- mypy configuration (strict mode)
- pytest configuration

### Related Templates

- `src/python/` - Simpler Python setup
- `src/pre-commit/` - Git hooks
