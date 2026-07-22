"""
About Page.
"""

from __future__ import annotations

import streamlit as st

from src.ui.components import (
    render_subtitle,
    render_title,
)
from src.ui.styles import apply_styles

apply_styles()

render_title()

render_subtitle()

st.divider()

st.header("ℹ️ About This Project")

st.markdown(
    """
## 🎯 Project Overview

Hangman is a modern Python implementation of the classic word guessing game.

This project was originally developed as a college assignment and has now been
completely redesigned into a portfolio-quality application using modern Python
software engineering practices.

Rather than being just a simple console game, it demonstrates how even a small
project can be structured like a real-world application with clean architecture,
modular design, testing, configuration management and an interactive web UI.
"""
)

st.divider()

st.header("✨ Features")

features = [
    "Interactive Streamlit web application",
    "Multiple categories",
    "Multiple difficulty levels",
    "Large curated word database",
    "Persistent leaderboard",
    "Session state management",
    "Game scoring system",
    "Progress tracking",
    "Responsive user interface",
    "Modern Python project structure",
]

for feature in features:
    st.markdown(f"- {feature}")

st.divider()

st.header("🛠️ Technology Stack")

left, right = st.columns(2)

with left:
    st.markdown(
        """
### Backend

- Python 3
- Object-Oriented Programming
- JSON
- Logging
- Session Management
"""
    )

with right:
    st.markdown(
        """
### Frontend

- Streamlit
- Custom CSS
- Responsive Layout
- Interactive Components
"""
    )

st.divider()

st.header("📂 Project Structure")

st.code(
    """
Hangman
│
├── Home.py
├── pages/
├── src/
├── data/
├── config/
├── docs/
├── tests/
└── validation/
""",
    language="text",
)

st.divider()

st.header("👨‍💻 Developer")

st.markdown(
    """
**Bibhraj Saha**

Data Engineer

This project demonstrates software engineering fundamentals including clean
architecture, modular programming, object-oriented design, testing,
configuration management and interactive application development.
"""
)

st.divider()

st.success("Thank you for exploring the Hangman project!")
