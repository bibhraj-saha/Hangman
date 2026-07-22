"""
Reusable Streamlit UI components.
"""

from __future__ import annotations

import streamlit as st


def render_title():
    st.title("🎯 Hangman")


def render_subtitle():
    st.caption("Modern Python • Streamlit • Portfolio Project")


def render_game_information(
    player,
    category,
    difficulty,
):
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Player",
        player,
    )

    col2.metric(
        "Category",
        category,
    )

    col3.metric(
        "Difficulty",
        difficulty,
    )


def render_word(word: str):
    st.markdown(
        f"""
<h1 style="text-align:center;
letter-spacing:12px;
margin-top:25px;
margin-bottom:25px;">
{word}
</h1>
""",
        unsafe_allow_html=True,
    )


def render_hearts(
    remaining_attempts,
):
    hearts = "❤️" * remaining_attempts

    hearts += "🤍" * (6 - remaining_attempts)

    st.markdown(f"### Lives: {hearts}")


def render_progress(
    guessed,
    total,
):
    progress = guessed / total

    st.progress(progress)


def render_guess_history(
    title: str,
    letters: set[str],
    color: str,
) -> None:
    """
    Render guessed letters as colored chips.
    """

    st.markdown(f"#### {title}")

    if not letters:
        st.write("-")
        return

    chips = ""

    for letter in sorted(letters):
        chips += f"""
<span style="
display:inline-block;
margin:4px;
padding:6px 12px;
border-radius:20px;
background:{color};
color:white;
font-weight:bold;
">
{letter.upper()}
</span>
"""

    st.markdown(
        chips,
        unsafe_allow_html=True,
    )


def render_guess_chips(
    title: str,
    letters: set[str],
    color: str,
) -> None:
    """
    Render guessed letters as colored chips.
    """

    st.markdown(f"#### {title}")

    if not letters:
        st.write("-")
        return

    chips = ""

    for letter in sorted(letters):
        chips += f"""
<span style="
display:inline-block;
margin:4px;
padding:6px 12px;
border-radius:20px;
background:{color};
color:white;
font-weight:bold;
">
{letter.upper()}
</span>
"""

    st.markdown(
        chips,
        unsafe_allow_html=True,
    )
