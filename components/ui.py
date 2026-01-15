import streamlit as st

LANG_EN = "English"
LANG_JA = "日本語"

TEXT = {
    "toggle_label": {LANG_EN: "Language", LANG_JA: "言語"},
    "home_title": {LANG_EN: "Neurodiversity Communication Toolkit", LANG_JA: "ニューロダイバーシティ・コミュニケーション ツールキット"},
    "home_subtitle": {
        LANG_EN: "Support for gentle, clear conversations about neurodiversity in Japanese educational contexts.",
        LANG_JA: "日本の教育現場におけるニューロダイバーシティをめぐる、やさしく明確な対話を支えるツールです。",
    },
    "home_intro": {
        LANG_EN: (
            "This toolkit supports educators in communicating about neurodiversity in ways that are culturally respectful, "
            "emotionally safe, and practically useful.\n\n"
            "It does not provide diagnoses or labels. Instead, it offers language, visuals, and guidance to help conversations "
            "feel clearer and less stressful for everyone involved."
        ),
        LANG_JA: (
            "本ツールキットは、教育者がニューロダイバーシティについて話すときに、文化的配慮・心理的安全性・実用性を両立しながら、"
            "対話を進めるための支援を目的としています。\n\n"
            "診断やラベル付けを行うものではありません。代わりに、言葉・視覚的メタファー・会話の進め方を通して、"
            "対話がより明確で、ストレスの少ないものになるよう助けます。"
        ),
    },
    "menu_title": {LANG_EN: "Menu", LANG_JA: "メニュー"},
}

def get_lang() -> str:
    if "lang" not in st.session_state:
        st.session_state.lang = LANG_EN
    return st.session_state.lang

def t(key: str) -> str:
    lang = get_lang()
    if key not in TEXT:
        return key
    return TEXT[key].get(lang, TEXT[key].get(LANG_EN, key))

def sidebar_menu_header():
    """
    Adds a friendly 'Menu' label above the page navigation.
    Streamlit's built-in page list renders above other sidebar elements,
    so we show this header inside the sidebar to make navigation clearer.
    """
    st.sidebar.markdown(f"### {t('menu_title')}")

def language_toggle(sidebar: bool = True) -> str:
    """Put a language selector in sidebar by default."""
    # Add the Menu label near the top
    sidebar_menu_header()

    container = st.sidebar if sidebar else st
    current = get_lang()
    options = [LANG_JA, LANG_EN]  # show JA first
    index = options.index(current) if current in options else 1

    selected = container.radio(
        t("toggle_label"),
        options=options,
        index=index,
        horizontal=True,
        key="lang_selector",
    )
    st.session_state.lang = selected
    return selected

def page_header(title: str, subtitle: str | None = None):
    st.title(title)
    if subtitle:
        st.caption(subtitle)
    st.divider()
