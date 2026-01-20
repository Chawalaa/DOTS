import streamlit as st
from components.ui import set_sidebar_branding, language_toggle

# Auto-go to Home when app opens (especially on mobile)
if "boot" not in st.session_state:
    st.session_state.boot = True
    st.switch_page("pages/1_Home.py")


st.set_page_config(page_title="Neurodiversity Communication Toolkit", layout="wide")

# Hide the default "app" label and show Menu at the top
set_sidebar_branding("Menu")
language_toggle(sidebar=True)


