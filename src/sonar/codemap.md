# src/sonar/

## Responsibility

Provides SonarQube code quality scanning via Docker container, enabling static analysis of code for bugs, vulnerabilities, and code smells.

## Design

### Key Tasks

| Task           | Description                                |
| -------------- | ------------------------------------------ |
| `check`        | Validates Docker and SonarQube credentials |
| `check:docker` | Verifies Docker installation               |
| `check:vars`   | Validates SONAR_URL and SONAR_TOKEN        |
| `show`         | Displays configured SonarQube variables    |
| `scan`         | Runs SonarScanner analysis                 |

### Variables

| Variable      | Required | Purpose              |
| ------------- | -------- | -------------------- |
| `SONAR_URL`   | Yes      | SonarQube server URL |
| `SONAR_TOKEN` | Yes      | Authentication token |

### Patterns

- Docker-based scanner (sonarsource/sonar-scanner-cli)
- Volume mount for project scanning
- Environment-based authentication

## Flow

```
check → (show | scan)
```

## Integration

### Usage in Project Taskfile

```yaml
includes:
  - task: src/sonar:scan
```

### Required Files

- `sonar-project.properties` - SonarQube project configuration

### Related Templates

- `src/docker/` - Docker tooling
