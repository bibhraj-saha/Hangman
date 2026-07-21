"""
Virtual keyboard for Hangman.
"""

from __future__ import annotations

from typing import Callable

import streamlit as st

KEYBOARD_ROWS = [
    list("QWERTYUIOP"),
    list("ASDFGHJKL"),
    list("ZXCVBNM"),
]


def render_keyboard(
    guessed_letters: set[str],
    on_guess: Callable[[str], None],
) -> None:
    """
    Render clickable A-Z keyboard.
    """

    st.markdown("### ⌨️ Keyboard")

    for row in KEYBOARD_ROWS:

        cols = st.columns(len(row))

        for column, letter in zip(cols, row):

            disabled = (
                letter.lower() in guessed_letters
                or st.session_state.engine.is_won()
                or st.session_state.engine.is_lost()
            )

            with column:

                if st.button(
                    letter,
                    key=f"key_{letter}",
                    disabled=disabled,
                    use_container_width=True,
                ):
                    on_guess(letter.lower())
