"""
Leaderboard Page.
"""

from __future__ import annotations

import streamlit as st

from src.high_score import HighScoreManager
from src.ui.components import (
    render_subtitle,
    render_title,
)
from src.ui.leaderboard import (
    render_score_card,
)
from src.ui.styles import apply_styles

apply_styles()

render_title()

render_subtitle()

st.divider()

st.header("🏆 Leaderboard")

manager = HighScoreManager()

if "show_all_scores" not in st.session_state:
    st.session_state.show_all_scores = False

# ==========================================================
# STATISTICS
# ==========================================================

left, right = st.columns(2)

with left:
    st.metric(
        "Games Played",
        manager.total_games(),
    )

with right:
    st.metric(
        "Highest Score",
        manager.best_score(),
    )

st.divider()

# ==========================================================
# SHOW SCORES
# ==========================================================

if st.session_state.show_all_scores:
    scores = manager.get_all_scores()

else:
    scores = manager.get_top_scores()

if not scores:
    st.info("No games played yet.")

else:
    for rank, score in enumerate(
        scores,
        start=1,
    ):
        render_score_card(
            rank,
            score,
        )

st.divider()

# ==========================================================
# ACTIONS
# ==========================================================

left, right = st.columns(2)

with left:
    if st.button(
        "📋 Show All" if not st.session_state.show_all_scores else "📋 Show Top 5",
        use_container_width=True,
    ):
        st.session_state.show_all_scores = not st.session_state.show_all_scores

        st.rerun()

with right:
    if st.button(
        "🗑️ Clear Leaderboard",
        use_container_width=True,
    ):
        manager.clear_scores()

        st.success("Leaderboard cleared.")

        st.rerun()
