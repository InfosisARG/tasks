# src/go/

## Responsibility

Provides comprehensive Go development tasks including module management, code generation, formatting, linting, testing, and release building.

## Design

### Key Tasks

| Task                 | Description                                     |
| -------------------- | ----------------------------------------------- |
| `check`              | Validates Go, gofmt, golangci-lint, goreleaser  |
| `check:go`           | Verifies Go installation                        |
| `check:gofmt`        | Verifies gofmt exists                           |
| `check:golangcilint` | Verifies golangci-lint exists                   |
| `check:goreleaser`   | Verifies goreleaser exists                      |
| `setup`              | Downloads deps, tidies, vendors, generates code |
| `fmt`                | Formats Go files using gofmt                    |
| `prettier`           | Alias for fmt                                   |
| `lint`               | Runs golangci-lint                              |
| `fix`                | Auto-fixes lint violations                      |
| `vet`                | Runs go vet                                     |
| `test`               | Runs tests with race detection                  |
| `build`              | Builds release using goreleaser                 |
| `mockery`            | Regenerates mocks via mockery                   |
| `generate`           | Runs Wire DI code generation                    |

### Variables

| Variable   | Purpose                                       |
| ---------- | --------------------------------------------- |
| `GO_FILES` | Auto-computed: all .go files excluding vendor |

### Dependencies

- Go toolchain
- gofmt (part of Go)
- golangci-lint
- goreleaser
- mockery (optional)
- wire (optional)

### Patterns

- Race detection in tests (`-race`)
- Coverage report generation
- Vendor directory management
- Config-driven linting (`.ci/linters/.golangci.yml`)

## Flow

```
check:* → setup → (fmt | lint | fix | vet | test | build)
```

## Integration

### Usage in Project Taskfile

```yaml
includes:
  - task: src/go:lint
  - task: src/go:test
```

### Required Files

- `.ci/linters/.golangci.yml` - Linter configuration
- `.ci/config/mockery.yaml` - Mockery configuration

### Related Templates

- `src/release/` - Release orchestration
- `src/changelog/` - Changelog generation
