import streamlit as st
from components.ui import apply_brand_styles, set_sidebar_branding, language_toggle, get_lang, page_header

from pathlib import Path
import urllib.parse

st.set_page_config(page_title="Visual Tools", layout="wide", initial_sidebar_state="collapsed")

# Branding + sidebar
apply_brand_styles()
set_sidebar_branding("Menu")
language_toggle(sidebar=True)

page_header(
    "Visual & Narrative Tools" if get_lang() == "English" else "視覚／ナラティブツール",
    "Simple metaphors and design guidance to support understanding without labels."
    if get_lang() == "English"
    else "ラベルなしで理解を助けるメタファーとデザイン指針。",
)

# -----------------------------
# Helpers: View + Download PDFs
# -----------------------------
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/Chawalaa/DOTS/main/assets/"

def pdf_view_download_buttons(label_title_en: str, label_title_ja: str, pdf_filename: str):
    """
    Shows a View button (opens in new tab) + Download button (downloads bytes).
    - View uses Google viewer on the GitHub raw URL.
    - Download uses local assets/ file if present (shows error if missing).
    """
    title = label_title_en if get_lang() == "English" else label_title_ja
    st.markdown(f"**{title}**")

    # Encode filename for URL (spaces etc.)
    pdf_url_encoded = urllib.parse.quote(pdf_filename)
    raw_url = GITHUB_RAW_BASE + pdf_url_encoded
    view_url = "https://drive.google.com/viewerng/viewer?embedded=true&url=" + urllib.parse.quote(raw_url, safe="")

    c1, c2 = st.columns(2)

    with c1:
        if hasattr(st, "link_button"):
            st.link_button(
                "View (opens in new tab)" if get_lang() == "English" else "表示（新しいタブ）",
                view_url,
                use_container_width=True,
            )
        else:
            st.markdown(
                f"[{('View (opens in new tab)' if get_lang() == 'English' else '表示（新しいタブ）')}]({view_url})"
            )

    with c2:
        pdf_path = Path("assets") / pdf_filename
        if pdf_path.exists():
            st.download_button(
                label="Download PDF" if get_lang() == "English" else "PDFをダウンロード",
                data=pdf_path.read_bytes(),
                file_name=pdf_filename,
                mime="application/pdf",
                use_container_width=True,
            )
        else:
            st.error(
                f"PDF not found: assets/{pdf_filename}. Upload it to your GitHub repo under assets/."
                if get_lang() == "English"
                else f"PDFが見つかりません：assets/{pdf_filename} をGitHubの assets/ にアップロードしてください。"
            )

# ----------------------------------------
# Visual Metaphors (structured + PDF links)
# ----------------------------------------
st.subheader("Visual Metaphors" if get_lang() == "English" else "ビジュアル・メタファー")

st.write(
    "These metaphors help communicate neurodiversity in a calm, non-clinical, and non-hierarchical way. "
    "They support understanding without labels, diagnosis language, or comparison."
    if get_lang() == "English"
    else
    "これらのメタファーは、ニューロダイバーシティを落ち着いて、非臨床的かつ非階層的に伝えるためのものです。"
    "ラベルや診断的な言葉、比較を避けながら理解を支えます。"
)

st.divider()

# --- Dots ---
with st.expander("Dots Narrative" if get_lang() == "English" else "Dots（ドット）ナラティブ", expanded=True):
    st.write(
        "A gentle metaphor for diversity as different “dots” that form unique patterns—"
        "emphasizing variation without ranking or evaluation."
        if get_lang() == "English"
        else
        "多様性を「異なるドットが形づくるユニークなパターン」として捉える、やさしいメタファーです。"
        "優劣や評価を含まず、違いをそのまま尊重します。"
    )

    st.markdown(
        "- **Use when:** introducing neurodiversity without labels\n"
        "- **Supports:** emotional safety, curiosity, shared understanding\n"
        "- **Avoids:** “normal/abnormal” framing, clinical imagery"
        if get_lang() == "English"
        else
        "- **使う場面：** ラベルを使わずにニューロダイバーシティを紹介したいとき\n"
        "- **支えるもの：** 心理的安全性、好奇心、共通理解\n"
        "- **避けるもの：** 正常／異常の枠組み、臨床的イメージ"
    )

    pdf_view_download_buttons(
        label_title_en="Dots Narrative (PDF)",
        label_title_ja="Dots ナラティブ（PDF）",
        pdf_filename="Dots.pdf",
    )

# --- Waves ---
with st.expander("Waves Narrative" if get_lang() == "English" else "Waves（波）ナラティブ", expanded=False):
    st.write(
        "A metaphor for different rhythms and intensity in communication and learning—"
        "supporting the idea that people regulate and respond differently."
        if get_lang() == "English"
        else
        "コミュニケーションや学びの「リズムや強さの違い」を波として表すメタファーです。"
        "人それぞれ調整や反応の仕方が違うことを自然に伝えます。"
    )

    st.markdown(
        "- **Use when:** explaining sensory load, pacing, or emotional regulation\n"
        "- **Supports:** calm reframing, reduced blame, practical adjustments\n"
        "- **Avoids:** deficit language, correction/improvement framing"
        if get_lang() == "English"
        else
        "- **使う場面：** 感覚負荷、ペース、情動の調整を説明したいとき\n"
        "- **支えるもの：** 落ち着いた捉え直し、責めない理解、実務的な調整\n"
        "- **避けるもの：** 欠如表現、矯正／改善の枠組み"
    )

    pdf_view_download_buttons(
        label_title_en="Waves Narrative (PDF)",
        label_title_ja="Waves ナラティブ（PDF）",
        pdf_filename="Waves.pdf",
    )

# --- Pathways ---
with st.expander("Pathways Narrative" if get_lang() == "English" else "Pathways（道筋）ナラティブ", expanded=False):
    st.write(
        "A metaphor for different paths to the same goal—"
        "highlighting that learning and communication can succeed through multiple routes."
        if get_lang() == "English"
        else
        "「同じ目的でも道筋は一つではない」というメタファーです。"
        "学びや対話は複数のルートで成立することを示します。"
    )

    st.markdown(
        "- **Use when:** discussing support strategies, accommodations, or alternative methods\n"
        "- **Supports:** collaboration, flexibility, shared problem-solving\n"
        "- **Avoids:** “one correct way” assumptions"
        if get_lang() == "English"
        else
        "- **使う場面：** 支援方法、合理的配慮、別のやり方を話すとき\n"
        "- **支えるもの：** 協働、柔軟性、共同での問題解決\n"
        "- **避けるもの：** 「正しい方法は一つ」という前提"
    )

    pdf_view_download_buttons(
        label_title_en="Pathways Narrative (PDF)",
        label_title_ja="Pathways ナラティブ（PDF）",
        pdf_filename="Pathways.pdf",
    )

st.info(
    "Tip: These metaphors work best when paired with strengths-based language and non-evaluative phrasing."
    if get_lang() == "English"
    else
    "ヒント：これらのメタファーは、強みベースで評価しない言い回しと組み合わせると最も効果的です。"
)

st.divider()

# ----------------------------------------
# Color Guidelines (View + Download)
# ----------------------------------------
st.subheader("Color Guidelines" if get_lang() == "English" else "カラーガイドライン")

st.write(
    "Color in this framework supports emotional safety, clarity, and non-hierarchical communication. "
    "Colors express variation and diversity without implying value, ability, or priority."
    if get_lang() == "English"
    else
    "色は、安心感・明確さ・非階層的なコミュニケーションを支えます。"
    "価値や能力の優劣、正しさ、優先度を示すためには使いません。"
)

with st.expander("Palette Direction (soft pastel tones only)", expanded=True):
    st.markdown(
        "- Soft, pastel tones only\n"
        "- Limited palette to maintain calmness and consistency\n\n"
        "**Core colors include:**\n"
        "- Soft blue\n"
        "- Mint green\n"
        "- Peach\n"
        "- Lavender\n"
        "- Pale yellow\n\n"
        "These colors are selected to avoid urgency, evaluation, or medical association."
    )

with st.expander("Color Usage Rules", expanded=False):
    st.markdown(
        "- No single color should dominate a layout\n"
        "- Color must not encode:\n"
        "  - ability\n"
        "  - value\n"
        "  - correctness\n"
        "  - priority\n"
        "- All colors should be used evenly and gently\n"
        "- Color variation communicates difference without hierarchy"
    )

with st.expander("Colors to Avoid", expanded=False):
    st.markdown(
        "- Red / green oppositions\n"
        "- Black–white binaries\n"
        "- Medical, warning, or alert colors\n\n"
        "These schemes may introduce unintended emotional pressure or evaluative meaning."
    )

with st.expander("Accessibility & Consistency", expanded=False):
    st.markdown(
        "- Colors must support readability on light backgrounds\n"
        "- Meaning should never rely on color alone\n"
        "- Color use should remain consistent across:\n"
        "  - cards\n"
        "  - visuals\n"
        "  - app screens\n"
        "  - printed materials"
    )

st.info(
    "Summary: Color is expressive but restrained. It supports calm communication and shared understanding without directing judgment or comparison."
    if get_lang() == "English"
    else
    "まとめ：色は表現的ですが抑制的に。判断や比較を誘導せず、落ち着いた対話と共通理解を支えます。"
)

pdf_view_download_buttons(
    label_title_en="Color Guidelines (PDF)",
    label_title_ja="カラーガイドライン（PDF）",
    pdf_filename="color_guidelines.pdf",
)

st.divider()

# ----------------------------------------
# Typography (text only)
# ----------------------------------------
st.subheader("Typography" if get_lang() == "English" else "タイポグラフィ")

st.write(
    "Typography is designed to support clarity, emotional safety, and cultural neutrality. "
    "Fonts are chosen to reduce cognitive load and avoid an authoritative or clinical tone."
    if get_lang() == "English"
    else
    "タイポグラフィは、明確さ・心理的安全性・文化的中立性を支えるために設計します。"
    "認知負荷を下げ、権威的／臨床的な印象を避けるフォントを選びます。"
)

with st.expander("Primary Typeface (Neutral Sans-Serif)", expanded=True):
    if get_lang() == "English":
        st.markdown(
            "- Recommended fonts:\n"
            "  - **English:** Inter / Source Sans 3\n"
            "  - **Japanese:** Noto Sans JP\n\n"
            "These fonts are:\n"
            "- highly legible at small sizes\n"
            "- visually calm and non-decorative\n"
            "- suitable for educational and professional contexts"
        )
    else:
        st.markdown(
            "- 推奨フォント：\n"
            "  - **英語:** Inter / Source Sans 3\n"
            "  - **日本語:** Noto Sans JP\n\n"
            "これらのフォントは：\n"
            "- 小さなサイズでも読みやすい\n"
            "- 落ち着いた印象で装飾性が低い\n"
            "- 教育・プロフェッショナル環境に適している"
        )
