import streamlit as st
from components.ui import apply_brand_styles, set_sidebar_branding, language_toggle, get_lang, page_header, t

st.set_page_config(
    page_title="Home",
    layout="wide",
    initial_sidebar_state="collapsed"
)

apply_brand_styles()
set_sidebar_branding("Menu" if get_lang() == "English" else "メニュー")
language_toggle(sidebar=True)

page_header(t("home_title"), t("home_subtitle"))
st.write(t("home_intro"))

lang = get_lang()
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

lang = get_lang()

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


