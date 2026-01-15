import streamlit as st
from components.ui import set_sidebar_branding, language_toggle

st.set_page_config(page_title="Neurodiversity Communication Toolkit", layout="wide")

# Hide the default "app" label and show Menu at the top
set_sidebar_branding("Menu")
language_toggle(sidebar=True)

st.write("Open the Home page from the sidebar →")
st.info("If you don’t see it, confirm you created pages/1_Home.py in GitHub.")

