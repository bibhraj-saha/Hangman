"""
Leaderboard page.
"""

import streamlit as st

from src.high_score import HighScoreManager

manager = HighScoreManager()

st.title("🏆 Leaderboard")

scores = manager.top_scores()

if not scores:

    st.info(
        "No games played yet."
    )

else:

    st.table(
        [
            {
                "Player": s.player,
                "Score": s.score,
                "Category": s.category,
                "Difficulty": s.difficulty,
            }
            for s in scores
        ]
    )