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
        }

        html, body, [class*="css"]  { color: var(--ink); }

        /* App background */
        [data-testid="stAppViewContainer"]{
            background: #FFFDF8;
        }

        /* Content width on desktop */
        .block-container{
            padding-top: 1.1rem;
            padding-bottom: 2.2rem;
            max-width: 980px;
        }

        /* Sidebar background MUST be opaque (no rgba) */
        [data-testid="stSidebar"]{
            background: linear-gradient(
              180deg,
              #F3F7FF 0%,
              #F7F2FF 45%,
              #FFF9E8 100%
            );
            border-right: 1px solid rgba(50,50,50,0.06);
        }

        /* Make sidebar overlay look clean on mobile */
        @media (max-width: 768px){
            /* keep content readable */
            .block-container{
                padding-left: 1rem;
                padding-right: 1rem;
                max-width: 100%;
            }

            /* reduce huge titles on phone */
            h1{
                font-size: 2.0rem !important;
                line-height: 1.15 !important;
            }
            h2{
                font-size: 1.35rem !important;
                line-height: 1.2 !important;
            }
        }

        /* Buttons */
        .stButton > button,
        .stDownloadButton > button,
        .stLinkButton > a{
            border-radius: 12px !important;
            border: 1px solid rgba(143,185,255,0.30) !important;
        }
        /* ---------- Quick actions: colored tiles (Parents / Students / Colleagues) ---------- */
/* Targets the 3 buttons in the first 3-column row on the page.
   If you later add more 3-column rows above it, tell me and I'll make it key-based. */

div[data-testid="column"]:nth-child(1) .stButton > button {
    background: rgba(255, 199, 178, 0.32) !important;   /* peach */
    border: 1px solid rgba(255, 199, 178, 0.55) !important;
}

div[data-testid="column"]:nth-child(2) .stButton > button {
    background: rgba(174, 235, 213, 0.32) !important;   /* mint */
    border: 1px solid rgba(174, 235, 213, 0.55) !important;
}

div[data-testid="column"]:nth-child(3) .stButton > button {
    background: rgba(217, 200, 255, 0.32) !important;   /* lavender */
    border: 1px solid rgba(217, 200, 255, 0.55) !important;
}

/* Shared tile styling */
.stButton > button {
    color: #2B2B2B !important;
    font-weight: 650 !important;
    padding: 0.95rem 1rem !important;
    border-radius: 14px !important;
}

/* Hover */
div[data-testid="column"]:nth-child(1) .stButton > button:hover {
    background: rgba(255, 199, 178, 0.42) !important;
}
div[data-testid="column"]:nth-child(2) .stButton > button:hover {
    background: rgba(174, 235, 213, 0.42) !important;
}
div[data-testid="column"]:nth-child(3) .stButton > button:hover {
    background: rgba(217, 200, 255, 0.42) !important;
}

/* ---------- Explore: colored tiles ---------- */
/* This targets the next 3-column row of buttons after Quick actions.
   If you later add more 3-column rows, tell me and I’ll make it key-based. */

div[data-testid="column"]:nth-child(1) .stButton > button[key="ex_phrases"] {}

/* Key-based is not supported directly by CSS selectors in Streamlit markup,
   so we style the "Explore row" by using a container hook approach below. */

/* Style the Explore buttons by the order within THEIR row.
   This works if Explore is the second 3-column row of buttons on Home. */

/* Soft Blue */
div[data-testid="stHorizontalBlock"] + div[data-testid="stHorizontalBlock"]
  div[data-testid="column"]:nth-child(1) .stButton > button {
    background: rgba(143, 185, 255, 0.24) !important;
    border: 1px solid rgba(143, 185, 255, 0.45) !important;
}

/* Pale Yellow */
div[data-testid="stHorizontalBlock"] + div[data-testid="stHorizontalBlock"]
  div[data-testid="column"]:nth-child(2) .stButton > button {
    background: rgba(255, 241, 168, 0.32) !important;
    border: 1px solid rgba(255, 241, 168, 0.55) !important;
}

/* Lavender */
div[data-testid="stHorizontalBlock"] + div[data-testid="stHorizontalBlock"]
  div[data-testid="column"]:nth-child(3) .stButton > button {
    background: rgba(217, 200, 255, 0.32) !important;
    border: 1px solid rgba(217, 200, 255, 0.55) !important;
}

/* Hover states */
div[data-testid="stHorizontalBlock"] + div[data-testid="stHorizontalBlock"]
  div[data-testid="column"]:nth-child(1) .stButton > button:hover {
    background: rgba(143, 185, 255, 0.34) !important;
}
div[data-testid="stHorizontalBlock"] + div[data-testid="stHorizontalBlock"]
  div[data-testid="column"]:nth-child(2) .stButton > button:hover {
    background: rgba(255, 241, 168, 0.42) !important;
}
div[data-testid="stHorizontalBlock"] + div[data-testid="stHorizontalBlock"]
  div[data-testid="column"]:nth-child(3) .stButton > button:hover {
    background: rgba(217, 200, 255, 0.42) !important;
}

        </style>
        """,
        unsafe_allow_html=True,
    )


def set_sidebar_branding(title: str = "Menu"):
    safe_title = title.replace('"', '\\"')

    st.markdown(
        f"""
        <style>
        /* Hide the first two children inside the sidebar nav container */
        [data-testid="stSidebarNav"] > div:nth-child(-n+2) {{
            display: none !important;
        }}

        [data-testid="stSidebarNav"]::before {{
            content: "•••  {safe_title}";
            display: block;
            font-size: 14px;
            font-weight: 700;
            opacity: 0.92;
            padding: 10px 12px 6px 12px;
            margin-top: 2px;
            color: #2B2B2B;
        }}
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
