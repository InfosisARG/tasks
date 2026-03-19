# src/confluence/

## Responsibility

Provides documentation synchronization to Atlassian Confluence using the Mark tool. Syncs Markdown files with embedded Space metadata to Confluence pages.

## Design

### Key Tasks

| Task               | Description                                    |
| ------------------ | ---------------------------------------------- |
| `check`            | Validates Docker and Confluence credentials    |
| `check:docker`     | Verifies Docker installation                   |
| `check:vars`       | Validates all Confluence environment variables |
| `make:credentials` | Creates Mark config file                       |
| `sync`             | Syncs specified Markdown files to Confluence   |
| `sync:all`         | Syncs all docs with Space metadata             |
| `sync:develop`     | Syncs files changed since develop branch       |
| `sync:main`        | Syncs files changed since main branch          |
| `sync:master`      | Syncs files changed since master branch        |

### Variables

| Variable                  | Required | Purpose                              |
| ------------------------- | -------- | ------------------------------------ |
| `CONFLUENCE_BASE_URL`     | Yes      | Confluence instance URL              |
| `CONFLUENCE_ACCESS_TOKEN` | Yes      | API access token                     |
| `CONFLUENCE_USER`         | Yes      | Username/email                       |
| `FILES_CONFLUENCE`        | For sync | Space-separated file list            |
| `PWD`                     | Auto     | Working directory (for volume mount) |

### Patterns

- Docker-based tool execution (kovetskiy/mark)
- Credential generation to TOML config file
- Git diff-based selective sync
- Space metadata via HTML comments in Markdown

## Flow

```
check → make:credentials → sync
```

## Integration

### Usage in Project Taskfile

```yaml
includes:
  - task: src/confluence:sync:all
```

### Markdown File Metadata

```markdown
<!-- Space: DOCSPACE -->
<!-- Parent: ParentPage -->

Title: Page Title

# Actual Content
```

### Related Templates

- `src/docs/` - Documentation building
- `src/mark/` - Standalone Mark tool
