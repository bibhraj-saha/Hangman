"""
Tests for configuration.
"""

from __future__ import annotations

from src.config import load_config


def test_config_loads():
    config = load_config()

    assert config is not None


def test_game_section_exists():
    config = load_config()

    assert "game" in config


def test_logging_section_exists():
    config = load_config()

    assert "logging" in config
