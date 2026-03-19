# src/biomejs/

## Responsibility

Taskfile template for BiomeJS - fast JavaScript/TypeScript formatter and linter that replaces Prettier and ESLint.

## Design

Template follows go-task v3 conventions:
- `check:`, `check:biomejs` - Precondition validation
- `setup` - Initialize biome configuration
- `fmt` - Format code
- `lint` - Lint code
- `check:all` - Full check (fmt + lint)
- `fix` - Auto-fix lint violations
- `migrate` - Migrate from prettier/eslint configs

Uses `bunx @biomejs/biome` for execution (via bun runtime).

## Integration

- Consumed by: Root `Taskfile.yml` (via `includes: biome`)
- Depends on: `bunx` binary
- Config: `biome.json` at project root
