# src/docker/

## Responsibility

Provides Docker container image build and publish tasks with multi-platform support and secure registry authentication.

## Design

### Key Tasks

| Task           | Description                              |
| -------------- | ---------------------------------------- |
| `check`        | Validates Docker installation            |
| `check:docker` | Verifies docker binary exists            |
| `check:vars`   | Validates registry credentials           |
| `login`        | Authenticates to container registry      |
| `build`        | Builds Docker image for current platform |
| `publish`      | Builds and pushes image to registry      |

### Variables

| Variable               | Required | Purpose                                    |
| ---------------------- | -------- | ------------------------------------------ |
| `CI_REGISTRY_USER`     | Yes      | Registry username                          |
| `CI_REGISTRY_PASSWORD` | Yes      | Registry password/token                    |
| `CI_REGISTRY`          | Yes      | Registry hostname (e.g., ghcr.io)          |
| `DOCKER_PLATFORM`      | Yes      | Target platform (linux/amd64, linux/arm64) |
| `GROUP_NAME`           | Yes      | Organization/group name                    |
| `PROJECT_NAME`         | Yes      | Project name                               |
| `APP_TAG`              | Yes      | Image tag/version                          |

### Patterns

- Dependency chain: `build` → `login` → `check`
- `--password-stdin` for secure credential handling
- Multi-platform build with `--platform` flag
- Build arguments for version injection

## Flow

```
check:vars → login → (build | publish)
```

## Integration

### Usage in Project Taskfile

```yaml
includes:
  - task: src/docker:publish
```

### Required Files

- `Dockerfile` - Container image definition

### Related Templates

- `src/github/` - GitHub release management
- `src/sonar/` - Docker-based SonarQube scanning
