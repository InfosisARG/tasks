# src/version/

## Responsibility

Provides standalone semantic version bumping without changelog generation. Used as a building block for release processes.

## Design

### Key Tasks

| Task          | Description                   |
| ------------- | ----------------------------- |
| `default`     | Shows current release version |
| `major`       | Bumps major version (X.0.0)   |
| `minor`       | Bumps minor version (x.Y.0)   |
| `patch`       | Bumps patch version (x.y.Z)   |
| `pre_release` | Bumps pre-release version     |

### Variables

| Variable                 | Required | Purpose                              |
| ------------------------ | -------- | ------------------------------------ |
| `APP_TAG`                | Auto     | Current version from bump-my-version |
| `PYTHON_PACKAGE_MANAGER` | Yes      | Package manager for bump-my-version  |

### Patterns

- Semantic versioning (MAJOR.MINOR.PATCH)
- Non-committing bumps (--no-commit flag)
- Configured via pyproject.toml/bump-my-version

## Flow

```
default → (major | minor | patch | pre_release)
```

## Integration

### Usage in Project Taskfile

```yaml
includes:
  - task: src/version:patch
```

### Related Templates

- `src/release/` - Integrates versioning with changelog
- `src/changelog/` - Changelog generation
