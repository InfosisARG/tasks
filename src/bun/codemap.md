# src/bun/

## Responsibility

Provides Bun JavaScript runtime setup and installation tasks with conditional installation if not present.

## Design

### Key Tasks

| Task         | Description                         |
| ------------ | ----------------------------------- |
| `check`      | Validates Bun and curl installation |
| `check:bun`  | Verifies bun binary exists          |
| `check:curl` | Verifies curl is available          |
| `setup`      | Installs Bun if not already present |

### Patterns

- Conditional installation via shell check
- Silent installation for CI
- Uses official Bun installation script

## Flow

```
check → setup
```

## Integration

### Usage in Project Taskfile

```yaml
includes:
  - task: src/bun:setup
```

### Related Templates

- `src/node/` - Node.js tooling
- `src/pnpm/` - pnpm package manager
- `src/yarn/` - Yarn package manager