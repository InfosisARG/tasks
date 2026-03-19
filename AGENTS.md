# AGENTS.md

This repo is a collection of reusable `Taskfile.yml` templates. The main entrypoint is `Taskfile.yml` (go-task v3).

## Key Tools

| Tool         | Purpose                     | Version Config            |
| ------------ | --------------------------- | ------------------------- |
| `task`       | Task runner (go-task v3)    | N/A                       |
| `uv`         | Python package manager      | N/A                       |
| `ruff`       | Python linting + formatting | `pyproject.toml`          |
| `mypy`       | Python type checking        | `pyproject.toml` (strict) |
| `pre-commit` | Git hooks                   | `.pre-commit-config.yaml` |
| `prettier`   | Multi-language formatting   | N/A                       |
| `terraform`  | IaC tooling                 | `TERRAFORM_VERSION` var   |

**IMPORTANT**: `README.md` is GENERATED from `provision/generators/README.yaml` + `provision/templates/README.tpl.md`. Run `task readme` after modifying YAML sources. **Do not hand-edit README.md**.

## Build / Lint / Test Commands

### Quick Start

```bash
task setup      # Create .env, install deps, setup hooks
task check      # Verify toolchain dependencies
task prettier   # Format all files (Prettier + Terraform fmt)
task validate   # Run pre-commit hooks (matches CI)
```

### Python (via uv)

```bash
task uv:setup       # Install Python dependencies
task uv:fmt         # Format with ruff (line length 90)
task uv:lint        # Lint with ruff + mypy type check
task uv:test        # Run pytest with coverage
```

### Run A Single Test

```bash
# Python/pytest
uv run pytest -q tests/test_file.py
uv run pytest -q tests/test_file.py::test_name
uv run pytest -q -k "pattern_match"

# Go
go test -v ./path/to/pkg
go test -v ./path/to/pkg -run '^TestName$'
```

### Documentation

```bash
task docs:build      # Build MkDocs site
task docs:serve      # Serve locally for preview
task readme          # Regenerate README.md from templates
```

### Pre-commit (Full CI Pipeline)

```bash
uv run pre-commit run --all-files --show-diff-on-failure
```

## Code Style Guidelines

### Indentation (from .editorconfig)

| Extension                             | Indent   | Notes                 |
| ------------------------------------- | -------- | --------------------- |
| `*.py`                                | 4 spaces | Python only           |
| `*.go`                                | tabs     | Go uses tabs          |
| `*.{yml,yaml,json,toml,md,sh,tf,hcl}` | 2 spaces | Most config files     |
| `Makefile`                            | tabs     | Makefiles always tabs |

**Global rules**: `end_of_line=lf`, `trim_trailing_whitespace=true`, `charset=utf-8`

### Taskfile Conventions

```yaml
version: "3" # Always use v3

tasks:
  namespace:verb: # Namespaced naming: uv:lint, docs:build
    desc: "Description" # REQUIRED: always provide desc
    run: once # Use for idempotent tasks
    deps: # Dependencies (executed first)
      - task: check:tool
    preconditions: # Prerequisites validation
      - sh: command -v tool
        msg: "Install tool first"
    cmds:
      - command {{.VARS}} # Use template variables
```

**Rules**:

- Accept `{{.CLI_ARGS}}` for single-file operations
- Keep tasks non-interactive (CI-friendly)
- Commands must fail on errors (no `|| true` unless intentional)

### Python Style (pyproject.toml)

**Key ruff rules enabled**:

- `I` - Import sorting
- `BLE` - No bare except (catches `except:`)
- `S` - Security (bandit)
- `B` - Bugbear best practices
- `N` - PEP8 naming conventions
- `PLE`, `PLR` - Pylint rules

**Type annotations**: `mypy strict = true` - no untyped public functions

**Error handling**: Raise specific exceptions; never swallow errors.

### Go Style

```bash
gofmt -s              # Format
goimports             # Format + organize imports
golangci-lint run     # Full linting
```

**Import conventions**: Local prefix `github.com/infosisarg/`

## Git / PR Requirements

### Commits

- **Format**: Conventional Commits (enforced by commitlint)
- **Types**: `feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert|release|hotfix`
- **Format**: `<type>(<scope>): <description>` or `<type>: <description>`

### PR Titles

Enforced via `.github/semantic.yml`:

```
feat: add new template
fix(docker): resolve build timeout
docs: update README generation
```

### Security

- Pre-commit runs `detect-private-key` and `gitleaks`
- **Never commit credentials, keys, or secrets**
- Use `.env.example` for template variables

## Cursor/Copilot Rules

No `.cursor/rules/`, `.cursorrules`, or `.github/copilot-instructions.md` present.

## Repository Structure

```
├── Taskfile.yml         # Main entry point
├── src/                 # 40+ Taskfile templates by tool
├── provision/           # README generation pipeline
├── .ci/linters/         # CI linting configs
└── codemap.md           # Repository codemap
```

<skills_system priority="1">

## Available Skills

<!-- SKILLS_TABLE_START -->
<usage>
When users ask you to perform tasks, check if any of the available skills below can help complete the task more effectively. Skills provide specialized capabilities and domain knowledge.

How to use skills:
- Invoke: `npx openskills read <skill-name>` (run in your shell)
  - For multiple: `npx openskills read skill-one,skill-two`
- The skill content will load with detailed instructions on how to complete the task
- Base directory provided in output for resolving bundled resources (references/, scripts/, assets/)

Usage notes:
- Only use skills listed in <available_skills> below
- Do not invoke a skill that is already loaded in your context
- Each skill invocation is stateless
</usage>

<available_skills>

<skill>
<name>atlassian</name>
<description>|</description>
<location>project</location>
</skill>

<skill>
<name>azure-devops</name>
<description>|</description>
<location>project</location>
</skill>

<skill>
<name>deep-research</name>
<description>"Execute autonomous multi-step research using Google Gemini Deep Research Agent. Use for: market analysis, competitive landscaping, literature reviews, technical research, due diligence. Takes 2-10 minutes but produces detailed, cited reports. Costs $2-5 per task."</description>
<location>project</location>
</skill>

<skill>
<name>elevenlabs</name>
<description>|</description>
<location>project</location>
</skill>

<skill>
<name>git-release</name>
<description>Create consistent releases and changelogs</description>
<location>project</location>
</skill>

<skill>
<name>gitlab-create-mr</name>
<description>Validate, push the current branch, and create a GitLab merge request from the current diff</description>
<location>project</location>
</skill>

<skill>
<name>gmail</name>
<description>|</description>
<location>project</location>
</skill>

<skill>
<name>goji-commit-smart</name>
<description>Create git commits using goji rules from .goji.json (type/scope/emoji/signoff) with path-based heuristics.</description>
<location>project</location>
</skill>

<skill>
<name>google-calendar</name>
<description>|</description>
<location>project</location>
</skill>

<skill>
<name>google-chat</name>
<description>|</description>
<location>project</location>
</skill>

<skill>
<name>google-docs</name>
<description>|</description>
<location>project</location>
</skill>

<skill>
<name>google-drive</name>
<description>|</description>
<location>project</location>
</skill>

<skill>
<name>google-sheets</name>
<description>|</description>
<location>project</location>
</skill>

<skill>
<name>google-slides</name>
<description>|</description>
<location>project</location>
</skill>

<skill>
<name>google-tts</name>
<description>|</description>
<location>project</location>
</skill>

<skill>
<name>image-compression</name>
<description>Reduce image file size using the MCP image-compression tool. If no path is provided, ask the user for the file.</description>
<location>project</location>
</skill>

<skill>
<name>imagen</name>
<description>|</description>
<location>project</location>
</skill>

<skill>
<name>jira-add-worklog</name>
<description>Skill para registrar worklogs en Jira usando el issue key derivado del branch actual y una descripcion basada en los commits del branch.</description>
<location>project</location>
</skill>

<skill>
<name>jira-cloud-frequent-tasks-csv</name>
<description>Skill para consultar Jira Cloud mediante MCP y generar un archivo CSV con las tareas más frecuentes de un proyecto dado, sin filtrar por estado.</description>
<location>project</location>
</skill>

<skill>
<name>jira-cloud-incident-manager</name>
<description>Skill para gestionar incidentes en Jira Cloud usando el MCP de Atlassian (crear, buscar y actualizar issues).</description>
<location>project</location>
</skill>

<skill>
<name>jira-start-task</name>
<description>Skill para listar issues no terminadas asignadas al usuario en Jira usando `infobot.toml`, elegir una y crear un branch `feature/<ISSUE-KEY>`.</description>
<location>project</location>
</skill>

<skill>
<name>jira-work-report</name>
<description>Skill para generar un reporte de implementacion para el issue de Jira derivado del branch actual usando un template y un resumen basado en commits, y publicarlo como comentario.</description>
<location>project</location>
</skill>

<skill>
<name>jules</name>
<description>"Delegate coding tasks to Google Jules AI agent for asynchronous execution. Use when user says: 'have Jules fix', 'delegate to Jules', 'send to Jules', 'ask Jules to', 'check Jules sessions', 'pull Jules results', 'jules add tests', 'jules add docs', 'jules review pr'. Handles: bug fixes, documentation, features, tests, refactoring, code reviews. Works with GitHub repos, creates PRs."</description>
<location>project</location>
</skill>

<skill>
<name>manus</name>
<description>Delegate complex, long-running tasks to Manus AI agent for autonomous execution. Use when user says 'use manus', 'delegate to manus', 'send to manus', 'have manus do', 'ask manus', 'check manus sessions', or when tasks require deep web research, market analysis, product comparisons, stock analysis, competitive research, document generation, data analysis, or multi-step workflows that benefit from autonomous agent execution with parallel processing.</description>
<location>project</location>
</skill>

<skill>
<name>markdown-to-jira</name>
<description>Skill para crear issues de tipo epic y/o task en Jira Cloud a partir de un archivo Markdown y luego completar componentes, labels y issue keys.</description>
<location>project</location>
</skill>

<skill>
<name>mssql</name>
<description>"Execute read-only SQL queries against multiple Microsoft SQL Server databases. Use when: (1) querying MSSQL/SQL Server databases, (2) exploring database schemas/tables, (3) running SELECT queries for data analysis, (4) checking database contents. Supports multiple database connections with descriptions for intelligent auto-selection. Blocks all write operations (INSERT, UPDATE, DELETE, DROP, etc.) for safety."</description>
<location>project</location>
</skill>

<skill>
<name>mysql</name>
<description>"Execute read-only SQL queries against multiple MySQL databases. Use when: (1) querying MySQL databases, (2) exploring database schemas/tables, (3) running SELECT queries for data analysis, (4) checking database contents. Supports multiple database connections with descriptions for intelligent auto-selection. Blocks all write operations (INSERT, UPDATE, DELETE, DROP, etc.) for safety."</description>
<location>project</location>
</skill>

<skill>
<name>notebooklm</name>
<description>"Query and manage Google NotebookLM notebooks with persistent profile auth, source sync, batch/multi queries, and structured exports. Use when user asks to query NotebookLM, 'ask my notebook', shares NotebookLM notebook URLs, wants to list/create notebooks, manage sources, do bulk folder sync, dedupe, or audit exports."</description>
<location>project</location>
</skill>

<skill>
<name>opencode-tasks-scaffold</name>
<description>Genera prompts de task templates a partir del template base</description>
<location>project</location>
</skill>

<skill>
<name>outline</name>
<description>"Search, read, and manage Outline wiki documents. Use when: (1) searching wiki for documentation, (2) reading wiki pages or articles, (3) listing wiki collections or documents, (4) creating or updating wiki content, (5) exporting documents as markdown. Works with any Outline wiki instance (self-hosted or cloud)."</description>
<location>project</location>
</skill>

<skill>
<name>postgres</name>
<description>"Execute read-only SQL queries against multiple PostgreSQL databases. Use when: (1) querying PostgreSQL databases, (2) exploring database schemas/tables, (3) running SELECT queries for data analysis, (4) checking database contents. Supports multiple database connections with descriptions for intelligent auto-selection. Blocks all write operations (INSERT, UPDATE, DELETE, DROP, etc.) for safety."</description>
<location>project</location>
</skill>

<skill>
<name>release</name>
<description>Run a release bump (major/minor/patch) and generate next changelog from the updated pyproject.toml version.</description>
<location>project</location>
</skill>

<skill>
<name>update-pr</name>
<description>Push branch commits and update the existing MR body safely (prefer REST API)</description>
<location>project</location>
</skill>

<skill>
<name>validate-pr</name>
<description>Find vulnerabilities or errors in a merge request (checks, scans, merge blockers) and propose fixes.</description>
<location>project</location>
</skill>

</available_skills>
<!-- SKILLS_TABLE_END -->

</skills_system>