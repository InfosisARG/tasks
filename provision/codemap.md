# provision/ Directory

## Responsibility

Contains code generators and documentation templates for the repository. This directory provides the infrastructure to generate standardized documentation and diagrams from configuration-driven templates.

## Structure

```
provision/
├── generators/          # YAML configuration for README and documentation generation
│   └── README.yaml      # Canonical config defining project metadata, badges, sections
├── templates/          # Go template files (.tpl.md) for documentation
│   └── README.tpl.md    # Main README template using gomplate syntax
├── diagrams/            # Taskfile for PlantUML/Mermaid diagram generation
│   └── Taskfile.yml     # Docker-based PlantUML renderer
├── prompts/             # AI prompt templates for code scaffolding
│   └── tasks/           # Domain-specific prompt templates
│       ├── biomejs/     # BiomeJS task generation prompts
│       └── scaffold-template.prompt.md
└── codemap.md           # This file
```

## Design

### YAML Configuration (generators/README.yaml)

Central configuration file defining all README content:

- **Project metadata**: name, email, license, GitHub repo
- **Badges**: CI, lint, test, pre-commit, conventional commits, changelog status
- **Requirements**: Environment variables and external tools (gomplate, python, task)
- **Sections**: description, requirements, usages, examples (referenced as file paths)
- **Content sources**: Points to Markdown files in `docs/` for included sections

### Go Templates (templates/README.tpl.md)

Gomplate-based template using:

- `{{ ds "config" }}`: Access to YAML datasource
- `{{ ds "includes" }}`: Include external Markdown files
- Conditional sections: badges, features, screenshots, requirements, usage, etc.
- Dynamic dates and repository URLs
- Contributor tables with avatars
- Confluence metadata support (optional)

### PlantUML Diagrams (diagrams/)

Docker-based PlantUML generation:

- Uses `infosisarg/plantuml` Docker image
- Finds all `*.plantuml` files in project (excluding `.terraform`)
- Outputs PNG files to `decks/images/diagrams/`, `static/images/diagrams/`, `docs/images/diagrams/`

## Flow

### README Generation Pipeline

```
┌─────────────────────────────────────────────────────────────────────┐
│                    README Generation Pipeline                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. provision/generators/README.yaml                                │
│     └── Contains all project metadata                               │
│         - name, badges, description, requirements                   │
│         - Section references (usages, examples)                      │
│                                                                     │
│  2. task readme                                                     │
│     └── Invokes gomplate with:                                      │
│         - --file provision/templates/README.tpl.md                  │
│         - --out README.md                                           │
│         - --datasource config=provision/generators/README.yaml       │
│         - --datasource includes=file://                             │
│                                                                     │
│  3. gomplate processes template                                      │
│     └── Reads README.yaml, applies template logic                    │
│         - Includes referenced Markdown files                         │
│         - Renders badges, sections, dynamic content                  │
│                                                                     │
│  4. task prettier                                                   │
│     └── Formats output with Prettier                                │
│                                                                     │
│  5. README.md generated                                             │
│     └── Final documentation in repository root                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Diagram Generation Pipeline

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Diagram Generation Pipeline                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. Find *.plantuml files                                            │
│     └── find ./ -type f -name '*.plantuml' | grep -v '.terraform'   │
│                                                                     │
│  2. task diagrams:build                                              │
│     └── Creates output directories                                   │
│         - decks/images/diagrams/                                     │
│         - static/images/diagrams/                                    │
│         - docs/images/diagrams/                                      │
│                                                                     │
│  3. Docker PlantUML renderer                                          │
│     └── docker run infosisarg/plantuml [files...]                   │
│                                                                     │
│  4. task diagrams:publish                                            │
│     └── rsync PNG files to target directories                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Integration

### Integration with Main Taskfile.yml

```yaml
includes:
  diagrams: ./provision/diagrams/Taskfile.yml

env:
  README_YAML: provision/generators/README.yaml
  README_TEMPLATE: provision/templates/README.tpl.md
  README_INCLUDES: file://

tasks:
  readme:
    desc: Generate Readme
    cmds:
      - gomplate --file {{.README_TEMPLATE}} --out {{.README_FILE}} --datasource config={{.README_YAML}} --datasource includes={{.README_INCLUDES}}
      - task: prettier
```

### Key Tasks

| Task                    | Description                                      |
| ----------------------- | ------------------------------------------------ |
| `task readme`           | Generate README.md from YAML config and template |
| `task prettier`         | Format files (includes Terraform fmt)            |
| `task diagrams:build`   | Build PlantUML diagrams                          |
| `task diagrams:publish` | Publish diagrams to target directories           |

## Conventions

1. **Do not edit README.md directly** - All changes go to `provision/generators/README.yaml`
2. **Run `task readme`** - After modifying YAML, regenerate the README
3. **Include files are Markdown** - Referenced in `usages:` and `examples:` as paths
4. **Template uses gomplate syntax** - Supports conditionals, loops, and datasource access
5. **Badges are optional** - Only include badges relevant to the project