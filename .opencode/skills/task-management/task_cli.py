#!/usr/bin/env python3

"""Legacy task-management placeholder for this repository.

This repo does not include the historical `.infobot/skills/task-management/`
backend referenced by some bundled agent templates.
"""

import sys


def main() -> int:
    sys.stderr.write(
        "task-management legacy shim is not configured in this repository.\n"
    )
    sys.stderr.write("Missing backend: .infobot/skills/task-management/task_cli.py\n")
    sys.stderr.write(
        "Use local commands in .opencode/commands/ or the TaskManager subagent instead.\n"
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
