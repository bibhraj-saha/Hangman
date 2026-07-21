"""
Session state initialization.
"""

import streamlit as st


DEFAULTS = {
    "game_started": False,
    "player_name": "",
    "category": None,
    "difficulty": None,
    "engine": None,
}


def initialize_session() -> None:
    """Initialize Streamlit session state."""

    for key, value in DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = value