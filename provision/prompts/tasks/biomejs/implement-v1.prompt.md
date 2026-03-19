# Prompt: Implementar Taskfile para BiomeJS

## Objetivo

Crear `src/biomejs/Taskfile.yml` para la herramienta **BiomeJS**.

BiomeJS es un formatter y linter rapido para JavaScript/TypeScript que reemplaza Prettier y ESLint.

---

## Contexto

Ver convenciones en: `@.opencode/context/project/task-templates.md`

---

## Comandos de BiomeJS

```bash
# Formatear archivos
biome fmt .

# Lintear archivos
biome lint .

# Verificar (fmt + lint + otras validaciones)
biome check .

# Aplicar fixes automaticamente
biome check --write .

# Migrar desde prettier/eslint
biome migrate prettier
biome migrate eslint
```

### Patrones de archivos

```bash
biome fmt "**/*.js" "**/*.ts" "**/*.jsx" "**/*.tsx" "**/*.json"
biome lint "**/*.js" "**/*.ts" "**/*.jsx" "**/*.tsx"
```

---

## Estructura del Taskfile

```yaml
version: "3"

tasks:
  check:
    desc: Exist biomejs and dependences
    run: once
    deps:
      - task: check:biomejs

  check:biomejs:
    desc: Exist BiomeJS
    run: once
    preconditions:
      - sh: command -v biome
        msg: "Please Install biome"

  setup:
    desc: Setup biomejs configuration.
    run: once
    cmds:
      - biome init
    deps:
      - task: check:biomejs

  fmt:
    desc: Format files with BiomeJS.
    run: once
    cmds:
      - bunx @biomejs/biome format . --write
    deps:
      - task: check:biomejs

  lint:
    desc: Lint files with BiomeJS.
    run: once
    cmds:
      - bunx @biomejs/biome lint .
    deps:
      - task: check:biomejs

  check:
    desc: Check files with BiomeJS (fmt + lint).
    run: once
    cmds:
      - bunx @biomejs/biome check --write .
    deps:
      - task: check:biomejs

  fix:
    desc: Fix lint violations automatically.
    run: once
    cmds:
      - bunx @biomejs/biome lint . --write --max-diagnostics=none --unsafe
    deps:
      - task: check:biomejs

  migrate:
    desc: Migrate from prettier/eslint configs.
    run: once
    cmds:
      - biome migrate prettier
      - biome migrate eslint
    deps:
      - task: check:biomejs
```

---

## Configuracion (biome.json)

```json
{
  "$schema": "https://biomejs.dev/schemas/1.9.4/schema.json",
  "vcs": {
    "enabled": true,
    "clientKind": "git",
    "useIgnoreFile": true
  },
  "files": {
    "ignoreUnknown": true,
    "ignore": ["node_modules/**", "dist/**", "build/**", "*.min.js"]
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2,
    "lineWidth": 90
  },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true
    }
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "double",
      "trailingCommas": "es5",
      "semicolons": "always"
    }
  }
}
```

---

## Salida

1. `src/biomejs/Taskfile.yml`
2. `biome.json` (configuracion)
3. Breve descripcion de tareas

## Validacion

```bash
task biome
task -l src/biomejs/Taskfile.yml
```