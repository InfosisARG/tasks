# src/terraform/

## Responsibility

Provides Terraform infrastructure automation including environment setup, formatting, and multi-environment documentation generation using terraform-docs.

## Design

### Key Tasks

| Task                                    | Description                                 |
| --------------------------------------- | ------------------------------------------- |
| `check`                                 | Validates Terraform installation            |
| `check:terraform`                       | Verifies terraform binary exists            |
| `check:tfenv`                           | Verifies tfenv version manager exists       |
| `check:vars`                            | Validates AWS_PROFILE_NAME and ORGANIZATION |
| `check:vars:docs`                       | Validates TERRAFORM_PATH                    |
| `environment`                           | Switches Terraform version via tfenv        |
| `fmt`                                   | Formats all .tf files recursively           |
| `doc`                                   | Generates documentation for base path       |
| `command`                               | Core docs generation with stage/region      |
| `docs:root`, `docs:core`                | Stage-specific documentation                |
| `docs:prod`, `docs:staging`, `docs:dev` | Environment documentation                   |
| `docs:all`                              | Generates docs for all environments         |

### Variables

| Variable            | Required        | Purpose                                     |
| ------------------- | --------------- | ------------------------------------------- |
| `AWS_PROFILE_NAME`  | Yes             | AWS CLI profile                             |
| `ORGANIZATION`      | Yes             | Organization name for validation            |
| `TERRAFORM_PATH`    | For docs        | Path to Terraform root                      |
| `TERRAFORM_VERSION` | For environment | Terraform version to use                    |
| `STAGE`             | For docs        | Deployment stage (core, prod, staging, dev) |
| `REGION`            | For docs        | AWS region                                  |

### Patterns

- Hierarchical namespace: `check:*`, `docs:*`
- Environment-specific documentation generation
- tfenv for version management
- terraform-docs for automated documentation

## Flow

```
check → environment → (fmt | doc | docs:*)
```

## Integration

### Usage in Project Taskfile

```yaml
includes:
  - task: src/terraform:fmt
  - task: src/terraform:docs:all
```

### Required Files

- `.ci/config/.terraform-docs.yml` - terraform-docs configuration

### Related Templates

- `src/aws/` - AWS credential management
- `src/terragrunt/` - Terragrunt wrapper
