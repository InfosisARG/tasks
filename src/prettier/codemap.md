# src/prettier/

## Responsibility

Provides multi-language code formatting using Prettier with support for JavaScript, TypeScript, SCSS, Markdown, YAML, GraphQL, and MJML files.

## Design

### Key Tasks

| Task             | Description                                    |
| ---------------- | ---------------------------------------------- |
| `check`          | Validates Prettier installation                |
| `check:prettier` | Verifies prettier binary exists                |
| `all`            | Formats all supported file types               |
| `less`           | Formats only LESS files                        |
| `code`           | Formats code files (JS, TS, MD, YAML, GraphQL) |
| `sass`           | Formats only SCSS files                        |
| `execute`        | Core formatter with configurable file patterns |

### Variables

| Variable         | Required | Purpose                           |
| ---------------- | -------- | --------------------------------- |
| `FILES_PRETTIER` | Yes      | Glob patterns for files to format |

### Patterns

- Modular task organization by file type
- Prettier config: `.ci/linters/prettier.config.cjs`
- Prettier ignore: `.ci/linters/.prettierignore`
- `--list-different` for CI validation mode

## Flow

```
check → (all | less | code | sass)
```

## Integration

### Usage in Project Taskfile

```yaml
includes:
  - task: src/prettier:all
```

### Related Templates

- `src/python/` - Python formatting
- `src/go/` - Go formatting