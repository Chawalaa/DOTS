import streamlit as st
from components.ui import language_toggle, get_lang, page_header

st.set_page_config(page_title="Phrases & Scripts", page_icon="🗣️", layout="wide")
language_toggle(sidebar=True)

page_header(
    "Phrases & Scripts" if get_lang()=="English" else "フレーズ／台本",
    "Example phrases educators can adapt (strength-based, non-medical, culturally considerate)."
    if get_lang()=="English" else
    "教育者が状況に合わせて調整できる例文（強みベース／非医療的／文化的配慮）。"
)

st.write(
    "This section provides example phrases that educators can adapt when discussing neurodiversity."
    if get_lang()=="English" else
    "このセクションでは、ニューロダイバーシティについて話す際に調整して使える例文を提供します。"
)

st.divider()

st.subheader("Opening with strengths" if get_lang()=="English" else "強みから始める")
st.markdown(
    "- First, I’d like to share some of your child’s strengths.\n"
    "- ○○ has many positive qualities, including curiosity and creativity.\n"
    "- ○○ shows their own unique way of thinking and learning."
)

st.subheader("Describing needs without labels" if get_lang()=="English" else "ラベルなしでニーズを伝える")
st.markdown(
    "- There are situations where learning feels easier, and others where it feels more challenging.\n"
    "- ○○ seems to focus better in quieter or more structured environments.\n"
    "- This is not about what ○○ cannot do, but about how we can support them better."
)

st.subheader("Inviting collaboration" if get_lang()=="English" else "協働を促す")
st.markdown(
    "- We would like to think together about what kind of support might be helpful.\n"
    "- Your insights as a parent are very important to us.\n"
    "- We see this as a shared effort between home and school."
)

st.subheader("Closing the conversation" if get_lang()=="English" else "安心して終える")
st.markdown(
    "- Please feel free to share any concerns or questions at any time.\n"
    "- We can take this step by step.\n"
    "- Our goal is for ○○ to feel comfortable and supported."
)
