# src/changelog/

## Responsibility

Provides changelog generation using git-chglog, enabling conventional commit-based automatic changelog creation from Git history.

## Design

### Key Tasks

| Task           | Description                                 |
| -------------- | ------------------------------------------- |
| `check`        | Validates Go and git-chglog installation    |
| `check:chglog` | Verifies git-chglog binary exists           |
| `check:go`     | Verifies Go installation (for install task) |
| `install`      | Installs git-chglog v0.15                   |
| `generate`     | Generates full CHANGELOG.md                 |
| `tag`          | Generates changelog for specific tag        |
| `next`         | Generates preview of next release changelog |

### Variables

| Variable                 | Required     | Purpose                       |
| ------------------------ | ------------ | ----------------------------- |
| `APP_TAG`                | For tag/next | Version tag for changelog     |
| `TMP_CHANGELOG_FILENAME` | For tag      | Temporary file for tag output |

### Patterns

- Version-specific changelog generation
- Streaming output for CI integration
- Optional installation of toolchain

## Flow

```
check → (install) → (generate | tag | next)
```

## Integration

### Usage in Project Taskfile

```yaml
includes:
  - task: src/changelog:generate
```

### Required Files

- `.chglog/` directory with CHANGELOG.tpl.md configuration
- Properly formatted commit history

### Related Templates

- `src/release/` - Integrates changelog with versioning
- `src/version/` - Semantic version management
