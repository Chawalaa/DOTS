import streamlit as st
from components.ui import set_sidebar_branding, language_toggle

set_sidebar_branding("Menu")
language_toggle(sidebar=True)


st.set_page_config(page_title="Home", layout="wide")

language_toggle(sidebar=True)

page_header(t("home_title"), t("home_subtitle"))
st.write(t("home_intro"))

st.subheader("Quick actions" if get_lang() == "English" else "クイックアクション")
c1, c2, c3 = st.columns(3)

with c1:
    st.page_link("pages/4_Guides.py", label="I’m talking to parents" if get_lang()=="English" else "保護者と話す",)
with c2:
    st.page_link("pages/4_Guides.py", label="I’m talking to students" if get_lang()=="English" else "生徒と話す",)
with c3:
    st.page_link("pages/4_Guides.py", label="I’m talking to colleagues" if get_lang()=="English" else "同僚と話す",)

st.divider()

st.subheader("Explore" if get_lang() == "English" else "探す")
q1, q2, q3 = st.columns(3)
with q1:
    st.page_link("pages/2_Phrases_and_Scripts.py", label="Browse phrases & scripts" if get_lang()=="English" else "フレーズ／台本を見る",)
with q2:
    st.page_link("pages/3_Visual_Tools.py", label="Explore visual tools" if get_lang()=="English" else "視覚ツールを見る",)
with q3:
    st.page_link("pages/4_Guides.py", label="View conversation guides" if get_lang()=="English" else "会話ガイドを見る",)

