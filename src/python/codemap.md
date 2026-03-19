# src/python/

## Responsibility

Provides reusable Python development tasks with configurable package manager support. Template defaults to `uv` but supports any Python package manager through variable substitution.

## Design

### Key Tasks

| Task                    | Description                                       |
| ----------------------- | ------------------------------------------------- |
| `check`                 | Validates Python, package manager, and pre-commit |
| `check:python`          | Verifies Python is installed                      |
| `check:package_manager` | Verifies package manager is installed             |
| `check:precommit`       | Verifies pre-commit is available                  |
| `setup`                 | Installs dependencies with dev group              |
| `fmt`                   | Formats Python code using black                   |
| `test`                  | Runs pytest                                       |
| `environment`           | Installs Python interpreter                       |
| `precommit`             | Installs Git hooks for all phases                 |

### Variables

| Variable                 | Default | Purpose                 |
| ------------------------ | ------- | ----------------------- |
| `PYTHON_PACKAGE_MANAGER` | `uv`    | Package manager command |

### Dependencies

- Python runtime
- Package manager (uv by default)
- pre-commit framework

### Patterns

- Uses `run: once` for idempotent task execution
- Hierarchical task namespacing (`check:*`, `setup:*`)
- Precondition checks for tool validation

## Flow

```
check → setup → (fmt | test | precommit)
```

## Integration

### Usage in Project Taskfile

```yaml
includes:
  - task: src/python:fmt
  - task: src/python:test
```

### Related Templates

- `src/uv/` - Alternative Python tooling with stricter linting
- `src/pre-commit/` - Git hooks infrastructure
