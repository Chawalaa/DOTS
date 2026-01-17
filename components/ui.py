import streamlit as st
from pathlib import Path

LANG_EN = "English"
LANG_JA = "日本語"

TEXT = {
    "toggle_label": {LANG_EN: "Language", LANG_JA: "言語"},
    "menu_title": {LANG_EN: "Menu", LANG_JA: "メニュー"},
    "home_title": {
        LANG_EN: "Neurodiversity Communication Toolkit",
        LANG_JA: "ニューロダイバーシティ・コミュニケーション ツールキット",
    },
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
}


# -----------------------------
# Language helpers
# -----------------------------
def get_lang() -> str:
    if "lang" not in st.session_state:
        st.session_state.lang = LANG_EN
    return st.session_state.lang


def t(key: str) -> str:
    lang = get_lang()
    if key not in TEXT:
        return key
    return TEXT[key].get(lang, TEXT[key].get(LANG_EN, key))


# -----------------------------
# Global styles (pastel + airy)
# -----------------------------
def apply_brand_styles():
    """
    Light, calm, pastel look without heavy "boxed screenshot" boundaries.
    Call on every page after st.set_page_config(...).
    """
    st.markdown(
        """
        <style>
        :root{
            --soft-blue: #8FB9FF;
            --mint-green: #AEEBD5;
            --peach: #FFC7B2;
            --lavender: #D9C8FF;
            --pale-yellow: #FFF1A8;

            --ink: #2B2B2B;
            --border: rgba(50, 50, 50, 0.10);
        }

        html, body, [class*="css"]  { color: var(--ink); }

        /* Main page background (soft warm white) */
        [data-testid="stAppViewContainer"]{
            background: #FFFDF8;
        }

        /* Airy layout */
        .block-container {
            padding-top: 1.1rem;
            padding-bottom: 2.2rem;
            max-width: 980px;  /* polished reading width */
        }

        /* Sidebar background: gentle gradient */
        [data-testid="stSidebar"]{
            background: linear-gradient(
              180deg,
              rgba(143, 185, 255, 0.14) 0%,
              rgba(217, 200, 255, 0.12) 45%,
              rgba(255, 241, 168, 0.08) 100%
            );
            border-right: 1px solid rgba(50,50,50,0.06);
        }

        /* IMPORTANT: remove the "everything is a card" look */
        [data-testid="stVerticalBlockBorderWrapper"]{
            background: transparent !important;
            border: none !important;
            border-radius: 0 !important;
            box-shadow: none !important;
        }

        /* Expanders: gentle hover */
        details > summary { border-radius: 12px !important; }
        details > summary:hover { background: rgba(143,185,255,0.08); }

        /* Buttons: soft and consistent */
        .stButton > button,
        .stDownloadButton > button,
        .stLinkButton > a{
            border-radius: 12px !important;
            border: 1px solid rgba(143,185,255,0.30) !important;
        }

        /* Alerts: softer look */
        [data-testid="stAlert"]{
            border-radius: 14px;
            border: 1px solid rgba(50,50,50,0.08);
            box-shadow: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def soft_card(html: str):
    """
    Optional: use this only where YOU want a gentle card.
    Example:
        soft_card("<b>Tip</b><br>Keep language calm and non-evaluative.")
    """
    st.markdown(
        f"""
        <div style="
            background: rgba(255,255,255,0.75);
            border: 1px solid rgba(50,50,50,0.08);
            border-radius: 14px;
            padding: 16px 16px;
            margin: 10px 0 14px 0;
        ">
            {html}
        </div>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# Sidebar "Menu" above pages
# -----------------------------
def set_sidebar_branding(title: str | None = None):
    """
    Reliable on Streamlit Cloud:
    - Hide the built-in nav header that shows "app"
    - Inject our own header above the page list using CSS
    - Uses dot glyphs (•••) as the icon for reliability
    """
    if title is None:
        title = t("menu_title")

    safe_title = title.replace('"', '\\"')

    st.markdown(
        f"""
        <style>
        /* Try multiple targets to hide the default header ('app') */
        [data-testid="stSidebarNav"] > div:first-child {{ display: none !important; }}
        [data-testid="stSidebarNav"] header {{ display: none !important; }}
        [data-testid="stSidebarNavTitle"] {{ display: none !important; }}

        /* Add our own header above the pages list */
        [data-testid="stSidebarNav"]::before {{
            content: "•••  {safe_title}";
            display: block;
            font-size: 14px;
            font-weight: 600;
            opacity: 0.90;
            padding: 10px 12px 6px 12px;
            margin-top: 2px;
            color: var(--ink);
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# Language toggle
# -----------------------------
def language_toggle(sidebar: bool = True) -> str:
    container = st.sidebar if sidebar else st
    current = get_lang()
    options = [LANG_JA, LANG_EN]
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


# -----------------------------
# Page header helper
# -----------------------------
def page_header(title: str, subtitle: str | None = None):
    st.title(title)
    if subtitle:
        st.caption(subtitle)
    st.divider()


# -----------------------------
# App icon helper (tab icon)
# -----------------------------
def get_app_icon_path(default: str = "assets/dots.png") -> str | None:
    p = Path(default)
    return str(p) if p.exists() else None
