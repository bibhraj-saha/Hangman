"""
Play Game Page.
"""

from __future__ import annotations

from datetime import datetime

import streamlit as st

from src.ui.styles import apply_styles
from src.ui.session import initialize_session
from src.ui.game_manager import (
    loader,
    start_new_game,
)

from src.ui.keyboard import (
    render_keyboard,
)

from src.high_score import (
    HighScoreManager,
)

from src.models import (
    ScoreEntry,
)

from src.ui.components import (
    render_title,
    render_subtitle,
    render_hearts,
    render_progress,
    render_word,
    render_guess_history,
)

# ---------------------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------------------

apply_styles()

initialize_session()

high_score_manager = HighScoreManager()

if "score_saved" not in st.session_state:
    st.session_state.score_saved = False

render_title()

render_subtitle()

st.divider()

# ---------------------------------------------------------------------
# GAME SETUP
# ---------------------------------------------------------------------

if not st.session_state.game_started:

    st.subheader("🎮 Start New Game")

    left, right = st.columns([3, 1])

    with left:

        player_name = st.text_input(
            "Player Name",
            value=st.session_state.player_name,
            placeholder="Enter your name",
        )

        category = st.selectbox(
            "Category",
            loader.get_categories(),
        )

        difficulty = st.selectbox(
            "Difficulty",
            loader.get_difficulties(category),
        )

    with right:

        st.write("")
        st.write("")

        start_game = st.button(
            "🎯 Start Game",
            use_container_width=True,
        )

    if start_game:

        if not player_name.strip():

            st.error(
                "Please enter your name."
            )

            st.stop()

        engine = start_new_game(
            player_name,
            category,
            difficulty,
        )

        st.session_state.player_name = player_name
        st.session_state.category = category
        st.session_state.difficulty = difficulty
        st.session_state.engine = engine
        st.session_state.game_started = True
        st.session_state.score_saved = False

        st.rerun()

    st.info(
        "Choose your settings and press **Start Game**."
    )

    st.stop()

# ---------------------------------------------------------------------
# ACTIVE GAME
# ---------------------------------------------------------------------

engine = st.session_state.engine

state = engine.state

# ==========================================================
# GAME HEADER
# ==========================================================

st.markdown(
    f"""
### 🎮 {st.session_state.player_name}

**Category:** {st.session_state.category}
&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;
**Difficulty:** {st.session_state.difficulty}
""",
)

st.divider()

st.write("")

# ==========================================================
# GAME STATUS
# ==========================================================

render_hearts(
    state.remaining_attempts,
)

guessed = len(state.guessed_letters)

total = len(set(state.word))

render_progress(
    guessed,
    total,
)

st.write("")

# ==========================================================
# WORD
# ==========================================================

st.markdown("## 🔤 Word")

render_word(
    engine.current_word(),
)

st.divider()

# ==========================================================
# GUESS HISTORY
# ==========================================================

st.markdown("## 📝 Guess History")

left, right = st.columns(2)

with left:

    render_guess_history(
        "🟢 Correct",
        state.guessed_letters,
        "#16A34A",
    )

with right:

    render_guess_history(
        "🔴 Wrong",
        state.incorrect_letters,
        "#DC2626",
    )

# ==========================================================
# KEYBOARD
# ==========================================================


def handle_guess(letter: str) -> None:
    """
    Handle one guessed letter.
    """

    if engine.is_won():
        return

    if engine.is_lost():
        return

    engine.guess(letter)

    st.session_state.engine = engine

    st.rerun()


guessed_letters = (
    state.guessed_letters
    |
    state.incorrect_letters
)

st.markdown("## ⌨️ Choose a Letter")

render_keyboard(
    guessed_letters,
    handle_guess,
)

st.divider()

# ==========================================================
# GAME RESULT
# ==========================================================

game_finished = False
score = 0

if engine.is_won():

    game_finished = True

    score = (
        state.remaining_attempts * 100
        + len(state.word) * 25
    )

    st.success("🎉 Congratulations!")

    st.balloons()

    st.markdown(
        f"""
### 🏆 You guessed the word!

## **{state.word.upper()}**

### ⭐ Final Score: **{score}**
"""
    )

elif engine.is_lost():

    game_finished = True

    st.error("💀 Game Over")

    st.markdown(
        f"""
### The correct word was

# **{state.word.upper()}**

Better luck next time!
"""
    )

# ==========================================================
# SAVE HIGH SCORE
# ==========================================================

if (
    game_finished
    and not st.session_state.score_saved
):

    high_score_manager.add_score(
        ScoreEntry(
            player=st.session_state.player_name,
            score=score,
            category=st.session_state.category,
            difficulty=st.session_state.difficulty,
            word=state.word,
            won=engine.is_won(),
            timestamp=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        )
    )

    st.session_state.score_saved = True

    st.success("🏆 High score saved!")

# ==========================================================
# ACTIONS
# ==========================================================

st.divider()

left, middle, right = st.columns([1, 1, 1])

with left:

    if st.button(
        "🎮 New Game",
        use_container_width=True,
    ):

        st.session_state.game_started = False
        st.session_state.engine = None
        st.session_state.score_saved = False

        st.rerun()

with middle:

    if st.button(
        "🔄 Play Again",
        use_container_width=True,
    ):

        engine = start_new_game(
            st.session_state.player_name,
            st.session_state.category,
            st.session_state.difficulty,
        )

        st.session_state.engine = engine
        st.session_state.score_saved = False

        st.rerun()

if game_finished:

    st.metric(
        "Score",
        score,
    )