# src/release/

## Responsibility

Provides semantic versioning and release orchestration by combining version bumping with automatic changelog regeneration.

## Design

### Key Tasks

| Task                   | Description                           |
| ---------------------- | ------------------------------------- |
| `_version:default`     | Shows current release version         |
| `_version:major`       | Bumps major version                   |
| `_version:minor`       | Bumps minor version                   |
| `_version:patch`       | Bumps patch version                   |
| `_version:pre_release` | Bumps pre-release version             |
| `major`                | Full major release (bump + changelog) |
| `minor`                | Full minor release (bump + changelog) |
| `patch`                | Full patch release (bump + changelog) |
| `pre_release`          | Pre-release (bump + changelog)        |
| `_changelog_next`      | Internal: regenerates next changelog  |

### Variables

| Variable                 | Required | Purpose                              |
| ------------------------ | -------- | ------------------------------------ |
| `APP_TAG`                | Auto     | Current version from bump-my-version |
| `PYTHON_PACKAGE_MANAGER` | Yes      | Package manager for bump-my-version  |

### Patterns

- Semantic versioning (MAJOR.MINOR.PATCH)
- Non-committing version bumps (--no-commit flag)
- Automatic changelog regeneration
- Internal tasks for reusable version logic

## Flow

```
_version:* → _changelog_next
```

## Integration

### Usage in Project Taskfile

```yaml
includes:
  - task: src/release:major
  - task: src/release:patch
```

### Related Templates

- `src/version/` - Standalone versioning
- `src/changelog/` - Changelog generation