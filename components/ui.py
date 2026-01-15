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


def get_lang() -> str:
    """Return current language (defaults to English)."""
    if "lang" not in st.session_state:
        st.session_state.lang = LANG_EN
    return st.session_state.lang


def t(key: str) -> str:
    """Translate a key based on current language."""
    lang = get_lang()
    if key not in TEXT:
        return key
    return TEXT[key].get(lang, TEXT[key].get(LANG_EN, key))


def apply_brand_styles():
    """
    Applies your calm, pastel design language to the overall app (theme-like CSS layer).
    Adjust hex values to match your exact palette if needed.
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
            --card-bg: rgba(255, 255, 255, 0.78);
            --border: rgba(50, 50, 50, 0.10);
        }

        html, body, [class*="css"]  {
            color: var(--ink);
        }

        .block-container {
            padding-top: 1.2rem;
        }

        /* Sidebar background: gentle gradient using your palette */
        [data-testid="stSidebar"] {
            background: linear-gradient(
              180deg,
              rgba(143, 185, 255, 0.18) 0%,
              rgba(217, 200, 255, 0.14) 45%,
              rgba(255, 241, 168, 0.10) 100%
            );
            border-right: 1px solid var(--border);
        }

        /* Soft cards / bordered blocks */
        [data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 14px;
            box-shadow: 0 2px 18px rgba(0,0,0,0.04);
        }

        /* Expanders: calmer hover */
        details > summary {
            border-radius: 12px !important;
        }
        details > summary:hover {
            background: rgba(143, 185, 255, 0.10);
        }

        /* Buttons + download buttons */
        .stButton > button,
        .stDownloadButton > button,
        .stLinkButton > a {
            border-radius: 12px !important;
            border: 1px solid rgba(143, 185, 255, 0.35) !important;
        }

        /* Alerts: gentle look */
        [data-testid="stAlert"] {
            border-radius: 14px;
            border: 1px solid var(--border);
        }

        /* Our "Menu" header styling */
        .custom-menu-wrap {
            display: flex;
            align-items: center;
            gap: 10px;
            margin: 8px 0 10px 0;
        }
        .custom-menu-title {
            font-size: 14px;
            font-weight: 600;
            opacity: 0.85;
            line-height: 1.1;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def set_sidebar_branding(title: str | None = None, icon_path: str = "assets/dots.png", icon_width: int = 28):
    """
    Option A:
    - Hides Streamlit's built-in sidebar nav header ("app")
    - Inserts our own 'Menu' title ABOVE the pages list visually
    - Optionally shows your dots icon at the very top of the sidebar

    Call this near the top of every page BEFORE adding other sidebar widgets.
    """
    if title is None:
        title = t("menu_title")

    # Hide built-in nav header ("app") — use a couple selectors for robustness
    st.markdown(
        """
        <style>
        [data-testid="stSidebarNav"] > div:first-child { display: none !important; }
        [data-testid="stSidebarNav"] header { display: none !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Top branding row: icon + Menu title
    icon_file = Path(icon_path)
    if icon_file.exists():
        col1, col2 = st.sidebar.columns([1, 6])
        with col1:
            st.image(str(icon_file), width=icon_width)
        with col2:
            st.markdown(f'<div class="custom-menu-title">{title}</div>', unsafe_allow_html=True)
    else:
        st.sidebar.markdown(f'<div class="custom-menu-title">{title}</div>', unsafe_allow_html=True)


def language_toggle(sidebar: bool = True) -> str:
    """
    Language selector. Call set_sidebar_branding() before this so Menu + icon appear above pages.
    """
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
    """Consistent page header."""
    st.title(title)
    if subtitle:
        st.caption(subtitle)
    st.divider()
