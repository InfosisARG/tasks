# src/github/

## Responsibility

Provides GitHub CLI operations including repository management, pull request automation, release creation, and git submodule handling.

## Design

### Key Tasks

| Task                        | Description                                  |
| --------------------------- | -------------------------------------------- |
| `check-gh-cli`              | Validates GitHub CLI installation            |
| `add-git-submodules`        | Adds submodules from GitHub repos by pattern |
| `remove-git-submodules`     | Removes submodules and cleans up             |
| `create-release`            | Creates GitHub release with changelog        |
| `create-release-with-notes` | Creates release with auto-generated notes    |
| `merge-pull-requests`       | Auto-merges PRs with passing checks          |
| `diff-changes`              | Shows git diff excluding patterns            |

### Variables

| Variable       | Required       | Purpose                            |
| -------------- | -------------- | ---------------------------------- |
| `ORG`          | For submodules | GitHub organization                |
| `REGEXP`       | For submodules | Repository name pattern            |
| `TARGET_DIR`   | For submodules | Local directory for submodule      |
| `NEXT_VERSION` | For releases   | Version tag for release            |
| `BASE_BRANCH`  | For diff       | Base branch for comparison         |
| `EXCLUDES`     | For diff       | Comma-separated exclusion patterns |

### Patterns

- GitHub CLI (gh) for API operations
- jq for JSON processing
- Squash merging with branch cleanup
- Selective submodule management

## Flow

```
check-gh-cli → (create-release | merge-prs | diff-changes)
```

## Integration

### Usage in Project Taskfile

```yaml
includes:
  - task: src/github:create-release
  - task: src/github:merge-pull-requests
```

### Related Templates

- `src/git/` - Git operations
- `src/changelog/` - Changelog for releases