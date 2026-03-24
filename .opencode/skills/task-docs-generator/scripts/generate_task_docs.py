#!/usr/bin/env python3
"""Generate documentation from a Taskfile."""

import sys
import yaml
from pathlib import Path


def generate_task_docs(task_slug: str) -> None:
    """Generate documentation for a task."""
    taskfile_path = Path(f"src/{task_slug}/Taskfile.yml")
    output_path = Path(f"docs/tasks/{task_slug}.md")
    readme_yaml_path = Path("provision/generators/README.yaml")

    if not taskfile_path.exists():
        print(f"Error: Taskfile not found: {taskfile_path}")
        sys.exit(1)

    # Load Taskfile
    with open(taskfile_path) as f:
        taskfile = yaml.safe_load(f)

    tasks = taskfile.get("tasks", {})

    # Generate markdown
    lines = [
        f"# {task_slug}",
        "",
        f"Generated from: `src/{task_slug}/Taskfile.yml`",
        "---",
        "",
        "## Tasks",
        "",
        "| Task | Description |",
        "| ---- | ----------- |",
    ]

    # Add task table
    for task_name, task_data in tasks.items():
        desc = task_data.get("desc", "")
        if desc:
            lines.append(f"| `{task_name}` | {desc} |")

    lines.append("")
    lines.append("## Task Details")
    lines.append("")

    # Add detailed sections
    for task_name, task_data in tasks.items():
        desc = task_data.get("desc", "")
        if not desc:
            continue

        lines.append(f"### {task_name}")
        lines.append("")
        lines.append(desc)
        lines.append("")

        # Add commands
        cmds = task_data.get("cmds", [])
        if cmds:
            lines.append("**Commands:**")
            lines.append("```bash")
            for cmd in cmds:
                if isinstance(cmd, str):
                    lines.append(cmd)
                elif isinstance(cmd, dict) and "task" in cmd:
                    lines.append(f"- task: {cmd['task']}")
            lines.append("```")
            lines.append("")

        # Add dependencies
        deps = task_data.get("deps", [])
        if deps:
            lines.append("**Dependencies:**")
            for dep in deps:
                if isinstance(dep, str):
                    lines.append(f"- {dep}")
                elif isinstance(dep, dict) and "task" in dep:
                    lines.append(f"- task: {dep['task']}")
            lines.append("")

        # Add preconditions
        preconditions = task_data.get("preconditions", [])
        if preconditions:
            lines.append("**Preconditions:**")
            for precond in preconditions:
                if isinstance(precond, dict) and "msg" in precond:
                    lines.append(f"- {precond['msg']}")
            lines.append("")

    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    print(f"Documentation generated: {output_path}")

    # Update README.yaml
    module_line = f"  - docs/tasks/{task_slug}.md"
    with open(readme_yaml_path) as f:
        content = f.read()

    if module_line not in content:
        # Add module line before examples
        if "examples:" in content:
            content = content.replace("examples:", f"{module_line}\nexamples:")
        else:
            content += f"\n{module_line}\n"

        with open(readme_yaml_path, "w") as f:
            f.write(content)

        print(f"Added {module_line} to provision/generators/README.yaml")
    else:
        print(f"Module already exists in README.yaml")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_task_docs.py <task_slug>")
        sys.exit(1)

    generate_task_docs(sys.argv[1])
