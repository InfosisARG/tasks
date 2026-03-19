# Prompt: Extraer documentación de Taskfile

## Objetivo

Refactorizar el archivo `./docs/usage.md`, extrayendo toda la documentación detallada hacia `./docs/`, manteniendo el usage solo con lo necesario y legible.

---

## Input

* Archivos fuente: `src/**/Taskfile.yml`

---

## Instrucciones

1. Analizar todos los tasks definidos en el Taskfile.
2. Mantener cada `desc`, pero reducirlo a una sola línea clara y concisa.
3. Extraer toda la información detallada (comandos, dependencias, precondiciones) a un archivo de documentación.
4. No modificar la lógica ni la estructura de los tasks.
5. No duplicar lógica, solo documentarla.
6. colocar la documentacion de los task en `./docs`, generar cada archivo
7. ver la manera de como usar modules para colocarlo en `provision/generator/README.yml` ya que este tiene un template `provision/templates/README.tpl.md`

---

## Output

### 1. Taskfile actualizado

* Ruta: `src/{{task_slug}}/Taskfile.yml`
* Requisitos:
  * Estructura limpia
  * `desc` cortos (1 línea)
  * Sin documentación extensa inline

---

### 2. Archivo de documentación

* Ruta: `docs/tasks/{{task_slug}}.md`

### 3. Actualizacion de archivo README.yml

* Ruta: `provision/generator/README.yml`

---

## Reglas de transformación

* `desc` → resumir a una sola línea
* `cmds` → documentar en `internals`
* `deps` → describir relaciones
* `preconditions` → documentar validaciones

---

## Validación

```bash
task {{task_slug}}
task -l src/{{task_slug}}/Taskfile.yml
task validate
task readme
```

---

## Resultado esperado

* Documentación completa en `./docs/tasks/`
* Estructura escalable para múltiples tasks