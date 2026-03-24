---
name: opencode-tasks-scaffold
description: Scaffold de tasks usando templates predefinidos
metadata:
  opencode:
    emoji: 📝
    tags:
      - opencode
      - scaffold
      - template
---

# Task Scaffold (Template-Based)

Genera un nuevo task utilizando templates existentes.

## Uso

```
/task-prompt <task_name> [--force]
```

## Parámetros

| Parámetro | Tipo | Requerido | Descripción |
|----------|------|----------|-------------|
| `task_name` | string | ✅ | Nombre del task (ej: Terraform) |
| `--force` | flag | ❌ | Sobrescribe archivos existentes |

---

## Resolución de template

El template base se obtiene desde:

```
provision/prompts/templates/task/
```

Archivos esperados:

```
implement.prompt.template.md
README.template.md
```

---

## Output

Se genera:

```
provision/prompts/tasks/<task_slug>/
├── implement-v1.prompt.md
└── README.md
```

---

## Variables disponibles

Las siguientes variables se inyectan en los templates:

| Variable | Valor |
|----------|------|
| `{{task_name}}` | Terraform |
| `{{task_slug}}` | terraform |
| `{{task_title}}` | Terraform Task |

---

## Transformaciones

- `task_slug`:
  - lowercase
  - kebab-case
- `task_title`:
  - `<task_name> Task`

---

## Reglas de generación

1. Crear directorio destino:
```

provision/prompts/tasks/<task_slug>/

```

2. Procesar templates:
- `implement.prompt.template.md` → `implement-v1.prompt.md`
- `README.template.md` → `README.md`

3. Reemplazar variables `{{...}}`

---

## Comportamiento ante conflictos

| Caso | Acción |
|------|--------|
| Directorio no existe | Crear |
| Existe sin `--force` | Abort |
| Existe con `--force` | Sobrescribir |

---

## Validaciones

- `task_name` requerido
- no vacío
- sin special characters inválidos

---

## Errores

- Template no encontrado → abortar
- Variables no resueltas → error
- Permisos de escritura → error