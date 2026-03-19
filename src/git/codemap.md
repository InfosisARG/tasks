# src/git/

## Responsibility

Provides Git repository initialization and configuration tasks including gitignore generation and code reviewer assignment.

## Design

### Key Tasks

| Task        | Description                            |
| ----------- | -------------------------------------- |
| `check`     | Validates Git installation             |
| `check:git` | Verifies git binary exists             |
| `setup`     | Runs gitignore and reviewer setup      |
| `ignore`    | Generates .gitignore from templates    |
| `gi`        | Downloads gitignore templates via curl |
| `reviews`   | Configures GitHub PR reviewers         |

### Variables

| Variable             | Required | Purpose                         |
| -------------------- | -------- | ------------------------------- |
| `GIT_IGNORES`        | Yes      | Comma-separated gitignore types |
| `GIT_IGNORES_CUSTOM` | No       | Custom entries for .gitignore   |
| `REVIEWERS`          | Yes      | GitHub usernames for PR review  |

### Patterns

- Uses gitignore API (toptal.com) for template generation
- Appends custom entries after template
- Silent mode for non-interactive operations
- Git config for reviewer assignment

## Flow

```
check:git → setup → (ignore | reviews)
```

## Integration

### Usage in Project Taskfile

```yaml
includes:
  - task: src/git:setup
```

### Example Variables

```bash
export GIT_IGNORES="python,node,macos,linux,windows"
export GIT_IGNORES_CUSTOM="dist/\n*.log"
export REVIEWERS="username1,username2"
```

### Related Templates

- `src/github/` - GitHub operations