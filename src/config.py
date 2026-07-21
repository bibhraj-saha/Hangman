"""
Configuration loader.
"""

from pathlib import Path

import yaml

CONFIG_PATH = Path("config/settings.yaml")


def load_config() -> dict:
    """Load application configuration."""

    with CONFIG_PATH.open(
        "r",
        encoding="utf-8",
    ) as file:
        return yaml.safe_load(file)
