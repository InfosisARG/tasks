# src/ssh/

## Responsibility

Provides SSH key generation and PEM certificate management for infrastructure deployment across multiple environments.

## Design

### Key Tasks

| Task           | Description                                           |
| -------------- | ----------------------------------------------------- |
| `check`        | Validates ssh-keygen installation                     |
| `check:keygen` | Verifies ssh-keygen binary exists                     |
| `make`         | Generates SSH key pair in PEM format                  |
| `make:pem:*`   | Convenience tasks for dev/staging/testing/prod/custom |
| `export`       | Moves keys to keybase directory structure             |
| `export:pem:*` | Convenience tasks for key export                      |
| `make:user`    | Generates user-specific SSH key                       |

### Variables

| Variable               | Required      | Purpose                                   |
| ---------------------- | ------------- | ----------------------------------------- |
| `PROJECT_NAME`         | Yes           | Project identifier for key naming         |
| `STAGE`                | Yes           | Environment (dev, staging, testing, prod) |
| `USERNAME`             | For make:user | Username for key generation               |
| `KEYBASE_PROJECT_PATH` | For export    | Base path for key storage                 |

### Patterns

- RSA 4096-bit key generation
- PEM format conversion via openssl
- Idempotent key generation with status check
- Stage-specific key organization

## Flow

```
check → (make | export | make:user)
```

## Integration

### Usage in Project Taskfile

```yaml
includes:
  - task: src/ssh:make:pem:prod
  - task: src/ssh:export:pem:prod
```

### Related Templates

- `src/keybase/` - Keybase for key management
- `src/sops/` - Secrets encryption
