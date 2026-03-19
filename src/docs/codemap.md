# src/docs/

## Responsibility

Provides documentation generation and preview tasks using MkDocs for building and Grip for local GitHub-flavored Markdown preview.

## Design

### Key Tasks

| Task                           | Description                                     |
| ------------------------------ | ----------------------------------------------- |
| `check`                        | Validates Python, package manager, mkdocs, grip |
| `check:python`                 | Verifies Python installation                    |
| `check:python_package_manager` | Verifies package manager                        |
| `check:mkdocs`                 | Verifies mkdocs availability                    |
| `check:grip`                   | Verifies grip availability                      |
| `show`                         | Opens local Markdown preview with grip          |
| `build`                        | Builds static site with mkdocs                  |
| `serve`                        | Starts mkdocs dev server                        |

### Variables

| Variable                 | Default    | Purpose                 |
| ------------------------ | ---------- | ----------------------- |
| `PYTHON_PACKAGE_MANAGER` | Configured | Package manager command |

### Patterns

- Docker/environment-agnostic via package manager
- Local preview with automatic reload
- Static site generation for deployment

## Flow

```
check → (show | build | serve)
```

## Integration

### Usage in Project Taskfile

```yaml
includes:
  - task: src/docs:build
```

### Required Files

- `mkdocs.yml` - MkDocs configuration
- `docs/` - Documentation source directory

### Related Templates

- `src/confluence/` - Confluence sync
- `src/prettier/` - Markdown formatting