import streamlit as st
from components.ui import language_toggle, get_lang, page_header

st.set_page_config(page_title="Guides", layout="wide")
language_toggle(sidebar=True)
import streamlit as st
from pathlib import Path

from components.ui import apply_brand_styles, set_sidebar_branding, language_toggle, get_lang, page_header

# Branding + sidebar
apply_brand_styles()
set_sidebar_branding("Menu")
language_toggle(sidebar=True)

page_header(
    "Guides for Common Situations" if get_lang()=="English" else "よくある場面のガイド",
    "Short structures for conversations educators often find stressful or unclear."
    if get_lang()=="English" else
    "ストレスや不明確さを感じやすい場面で使える、短い会話構造。"
)

st.write(
    "These guides offer structure for situations that educators often find stressful or unclear."
    if get_lang()=="English" else
    "このガイドは、教育者がストレスや曖昧さを感じやすい場面で、会話に骨組みを与えます。"
)

st.divider()

st.subheader("First conversation with parents" if get_lang()=="English" else "保護者との最初の会話")
st.markdown(
    "**Keep in mind:**\n"
    "- Start with strengths and observations, not conclusions\n"
    "- Avoid technical or diagnostic language\n"
    "- Allow silence and reflection\n\n"
    "**Suggested approach:**\n"
    "1) Share positive observations\n"
    "2) Describe learning environments that help\n"
    "3) Invite collaboration rather than agreement"
)

st.subheader("Talking with students" if get_lang()=="English" else "生徒と話す")
st.markdown(
    "**Keep in mind:**\n"
    "- Use age-appropriate language\n"
    "- Avoid making the student feel “different” or “wrong”\n"
    "- Focus on comfort and learning styles\n\n"
    "**Suggested approach:**\n"
    "1) Explain that everyone learns differently\n"
    "2) Use visual/metaphor tools\n"
    "3) Emphasize support, not correction"
)

st.subheader("Talking with colleagues" if get_lang()=="English" else "同僚と話す")
st.markdown(
    "**Keep in mind:**\n"
    "- Aim for shared understanding, not persuasion\n"
    "- Use consistent language across staff\n"
    "- Keep conversations practical\n\n"
    "**Suggested approach:**\n"
    "1) Share observations, not judgments\n"
    "2) Focus on classroom strategies\n"
    "3) Align on supportive language"
)

