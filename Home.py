"""
Hangman Home Page.
"""

import streamlit as st

from src.constants import APP_NAME, APP_VERSION
from src.ui.session import initialize_session
from src.ui.styles import apply_styles

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🎯",
    layout="wide",
)

apply_styles()
initialize_session()

st.markdown(
    f"""
<div class="main-card">

<h1>🎯 Hangman</h1>

<h2>Modern Python & Streamlit Edition</h2>

<hr>

<p>
Welcome to the modernized Hangman project.
</p>

<p>
Use the navigation panel on the left to:
</p>

<ul>
    <li>🎮 Play Game</li>
    <li>🏆 View Leaderboard</li>
    <li>ℹ️ Learn about the project</li>
</ul>

<br>

<div style="
background:#F4E8C1;
border:1px solid #E5E7EB;
border-radius:12px;
padding:16px;
">

<b>Version</b> {APP_VERSION}<br>
Developed by <b>Bibhraj Saha</b>

</div>

</div>
""",
    unsafe_allow_html=True,
)
