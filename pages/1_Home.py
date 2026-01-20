import streamlit as st
from components.ui import (
    apply_brand_styles,
    set_sidebar_branding,
    language_toggle,
    get_lang,
    page_header,
    t,
    get_app_icon_path,
)

st.set_page_config(
    page_title="Home",
    page_icon=get_app_icon_path(),
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Global styles + sidebar
apply_brand_styles()
set_sidebar_branding("Menu" if get_lang() == "English" else "メニュー")
language_toggle(sidebar=True)

lang = get_lang()

# --- Optional: Home-only button color styling (Quick actions + Explore) ---
# NOTE: This relies on Quick actions being the first 3-column button row
# and Explore being the second 3-column button row on this page.
st.markdown(
    """
    <style>
    /* Shared tile styling */
    .stButton > button {
        color: #2B2B2B !important;
        font-weight: 650 !important;
        padding: 0.95rem 1rem !important;
        border-radius: 14px !important;
        border: 1px solid rgba(50,50,50,0.10) !important;
    }

    /* -------- Quick actions (row 1): Parents / Students / Colleagues -------- */
    /* peach */
    div[data-testid="stHorizontalBlock"]:nth-of-type(1)
      div[data-testid="column"]:nth-child(1) .stButton > button {
        background: rgba(255, 199, 178, 0.38) !important;
        border-color: rgba(255, 199, 178, 0.70) !important;
    }
    /* mint */
    div[data-testid="stHorizontalBlock"]:nth-of-type(1)
      div[data-testid="column"]:nth-child(2) .stButton > button {
        background: rgba(174, 235, 213, 0.38) !important;
        border-color: rgba(174, 235, 213, 0.70) !important;
    }
    /* lavender */
    div[data-testid="stHorizontalBlock"]:nth-of-type(1)
      div[data-testid="column"]:nth-child(3) .stButton > button {
        background: rgba(217, 200, 255, 0.38) !important;
        border-color: rgba(217, 200, 255, 0.70) !important;
    }

    /* Hover */
    div[data-testid="stHorizontalBlock"]:nth-of-type(1)
      .stButton > button:hover {
        filter: brightness(0.97);
    }

    /* -------- Explore (row 2): Soft blue / Pale yellow / Lavender -------- */
    /* soft blue */
    div[data-testid="stHorizontalBlock"]:nth-of-type(2)
      div[data-testid="column"]:nth-child(1) .stButton > button {
        background: rgba(143, 185, 255, 0.28) !important;
        border-color: rgba(143, 185, 255, 0.55) !important;
    }
    /* pale yellow */
    div[data-testid="stHorizontalBlock"]:nth-of-type(2)
      div[data-testid="column"]:nth-child(2) .stButton > button {
        background: rgba(255, 241, 168, 0.42) !important;
        border-color: rgba(255, 241, 168, 0.70) !important;
    }
    /* lavender */
    div[data-testid="stHorizontalBlock"]:nth-of-type(2)
      div[data-testid="column"]:nth-child(3) .stButton > button {
        background: rgba(217, 200, 255, 0.32) !important;
        border-color: rgba(217, 200, 255, 0.60) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Home text ---
page_header(t("home_title"), t("home_subtitle"))
st.write(t("home_intro"))

# --- Quick actions ---
st.subheader("Quick actions" if lang == "English" else "クイックアクション")
c1, c2, c3 = st.columns(3)

with c1:
    if st.button(
        "I’m talking to parents" if lang == "English" else "保護者と話す",
        use_container_width=True,
        key="qa_parents",
    ):
        st.switch_page("pages/4_Guides.py")

with c2:
    if st.button(
        "I’m talking to students" if lang == "English" else "生徒と話す",
        use_container_width=True,
        key="qa_students",
    ):
        st.switch_page("pages/4_Guides.py")

with c3:
    if st.button(
        "I’m talking to colleagues" if lang == "English" else "同僚と話す",
        use_container_width=True,
        key="qa_colleagues",
    ):
        st.switch_page("pages/4_Guides.py")

st.divider()

# --- Explore ---
st.subheader("Explore" if lang == "English" else "探す")
q1, q2, q3 = st.columns(3)

with q1:
    if st.button(
        "Browse phrases & scripts" if lang == "English" else "フレーズ／台本を見る",
        use_container_width=True,
        key="ex_phrases",
    ):
        st.switch_page("pages/2_Phrases_and_Scripts.py")

with q2:
    if st.button(
        "Explore visual tools" if lang == "English" else "視覚ツールを見る",
        use_container_width=True,
        key="ex_visual",
    ):
        st.switch_page("pages/3_Visual_Tools.py")

with q3:
    if st.button(
        "View conversation guides" if lang == "English" else "会話ガイドを見る",
        use_container_width=True,
        key="ex_guides",
    ):
        st.switch_page("pages/4_Guides.py")
