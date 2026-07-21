"""
Leaderboard UI components.
"""

from __future__ import annotations

import streamlit as st

from src.models import ScoreEntry

MEDALS = {
    1: "🥇",
    2: "🥈",
    3: "🥉",
}


def render_score_card(
    rank: int,
    score: ScoreEntry,
) -> None:
    """
    Render one leaderboard entry.
    """

    medal = MEDALS.get(rank, f"#{rank}")

    result = "🏆 Won" if score.won else "💀 Lost"

    st.markdown(
        f"""
<div style="
background:white;
padding:18px;
border-radius:14px;
border:1px solid #E5E7EB;
margin-bottom:14px;
">

<h4>{medal} {score.player}</h4>

<b>⭐ Score:</b> {score.score}<br>

<b>📂 Category:</b> {score.category}<br>

<b>🎯 Difficulty:</b> {score.difficulty}<br>

<b>📝 Word:</b> {score.word.upper()}<br>

<b>🎮 Result:</b> {result}<br>

<b>📅 Played:</b> {score.timestamp}

</div>
""",
        unsafe_allow_html=True,
    )
