"""
Development helper.
"""

from __future__ import annotations

import subprocess

COMMANDS = [
    [
        "python",
        "-m",
        "validation.validate_project",
    ],
    [
        "pytest",
    ],
    [
        "black",
        ".",
    ],
    [
        "ruff",
        "check",
        ".",
    ],
    [
        "isort",
        ".",
    ],
]


def main():
    for command in COMMANDS:
        print()

        print("=" * 60)

        print("Running")

        print(" ".join(command))

        print("=" * 60)

        subprocess.run(
            command,
            check=True,
        )


if __name__ == "__main__":
    main()
