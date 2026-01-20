import streamlit as st
from components.ui import (
    apply_brand_styles,
    set_sidebar_branding,
    language_toggle,
    get_lang,
    get_app_icon_path,
)

st.set_page_config(
    page_title="DOTS Toolkit",
    page_icon=get_app_icon_path(),
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Apply global styles + sidebar header (Menu)
apply_brand_styles()
set_sidebar_branding("Menu" if get_lang() == "English" else "メニュー")
language_toggle(sidebar=True)

# Always land on Home (especially important on mobile)
if "boot" not in st.session_state:
    st.session_state.boot = True
    st.switch_page("pages/1_Home.py")

# Fallback if someone somehow lands here after boot
lang = get_lang()
st.write("Open Home from the sidebar →" if lang == "English" else "サイドバーからホームを開いてください →")
