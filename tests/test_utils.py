"""
Tests for utilities.
"""

from __future__ import annotations

from src.utils import current_timestamp


def test_timestamp():
    timestamp = current_timestamp()

    assert isinstance(
        timestamp,
        str,
    )

    assert len(timestamp) > 10
