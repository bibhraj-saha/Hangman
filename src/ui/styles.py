"""
Application styling.
"""

import streamlit as st


def apply_styles() -> None:
    """Apply custom application theme."""

    st.markdown(
        """
<style>

/* ==========================================================
   MAIN APP
========================================================== */

.stApp{
    background:#FFF8E7;
    color:#1F2937;
}


/* ==========================================================
   HEADER
========================================================== */

header[data-testid="stHeader"]{
    background:#FFF8E7;
    border-bottom:1px solid #E5E7EB;
}

header[data-testid="stHeader"] *{
    color:#1F2937 !important;
}


/* ==========================================================
   SIDEBAR
========================================================== */

section[data-testid="stSidebar"]{
    background:#F4E8C1;
    border-right:1px solid #E5E7EB;
}

section[data-testid="stSidebarNav"] a{
    color:#1F2937 !important;
    font-weight:600;
    border-radius:10px;
    transition:0.2s;
}

section[data-testid="stSidebarNav"] a:hover{
    background:#F8E3AA;
}

section[data-testid="stSidebarNav"] a[aria-current="page"]{
    background:#D97706 !important;
    color:white !important;
}


/* ==========================================================
   MAIN CONTENT CARD
========================================================== */

.main-card{

    background:white;

    border-radius:18px;

    padding:32px;

    border:1px solid #E5E7EB;

    box-shadow:
        0 6px 18px rgba(0,0,0,0.08);

}


/* ==========================================================
   BUTTONS
========================================================== */

.stButton > button{

    width:100%;

    background:#D97706;

    color:white;

    border:none;

    border-radius:10px;

    font-weight:600;

}

.stButton > button:hover{

    background:#B45309;

    color:white;

}


/* ==========================================================
   METRICS
========================================================== */

div[data-testid="stMetric"]{

    background:white;

    border-radius:12px;

    border:1px solid #E5E7EB;

    padding:18px;

}


/* ==========================================================
   TEXT
========================================================== */

h1,h2,h3,h4,h5,h6,p,label,span{

    color:#1F2937;

}


/* ==========================================================
   PAGE
========================================================== */

.block-container {
    padding-top: 4.5rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

</style>
""",
        unsafe_allow_html=True,
    )
