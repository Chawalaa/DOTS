import streamlit as st
from pathlib import Path
import urllib.parse
import urllib.request

from components.ui import (
    apply_brand_styles,
    set_sidebar_branding,
    language_toggle,
    get_lang,
    page_header,
    get_app_icon_path,
)

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Phrases and Scripts",
    page_icon=get_app_icon_path() or "💬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------
# Branding + sidebar
# ----------------------------
apply_brand_styles()
set_sidebar_branding("Menu" if get_lang() == "English" else "メニュー")
language_toggle(sidebar=True)

lang = get_lang()

# ----------------------------
# PDF helpers (Quick Staffroom Reference)
# ----------------------------
QUICK_REF_RAW_URL = "https://raw.githubusercontent.com/Chawalaa/DOTS/main/assets/Quick%20Staff%20Room%20Reference%20.pdf"
QUICK_REF_VIEW_URL = "https://drive.google.com/viewerng/viewer?embedded=true&url=" + urllib.parse.quote(
    QUICK_REF_RAW_URL, safe=""
)

def load_quick_ref_pdf_bytes():
    # Try local first (supports both with/without the extra space before .pdf)
    candidates = [
        Path("assets") / "Quick Staff Room Reference.pdf",
        Path("assets") / "Quick Staff Room Reference .pdf",  # space before .pdf
    ]
    for p in candidates:
        if p.exists():
            return p.read_bytes(), p.name

    # Fallback: fetch from GitHub raw
    try:
        with urllib.request.urlopen(QUICK_REF_RAW_URL) as resp:
            return resp.read(), "Quick Staff Room Reference.pdf"
    except Exception:
        return None, "Quick Staff Room Reference.pdf"


# ----------------------------
# Content
# ----------------------------
page_header(
    "Phrases and Scripts" if lang == "English" else "フレーズと台本",
    "Practical language for calm, culturally respectful conversations."
    if lang == "English"
    else "落ち着いた、文化的配慮のある対話のための実用的な言い回し。",
)

st.write(
    "Use these phrases to keep conversations non-clinical, non-evaluative, and focused on shared understanding."
    if lang == "English"
    else "これらのフレーズは、非臨床・非評価の姿勢を保ちながら、共通理解に焦点を当てて対話を進めるために使えます。"
)

st.divider()

# ----------------------------
# Quick Staffroom Reference (View + Download)
# ----------------------------
st.markdown("### " + ("Quick Staffroom Reference" if lang == "English" else "職員室クイック参照"))

pdf_bytes, pdf_name = load_quick_ref_pdf_bytes()

c1, c2 = st.columns(2)

with c1:
    # View (opens in new tab, does not download)
    if hasattr(st, "link_button"):
        st.link_button(
            "View (opens in new tab)" if lang == "English" else "表示（新しいタブ）",
            QUICK_REF_VIEW_URL,
            use_container_width=True,
        )
    else:
        st.markdown(
            f"[{('View (opens in new tab)' if lang == 'English' else '表示（新しいタブ）')}]({QUICK_REF_VIEW_URL})"
        )

with c2:
    # Download
    if pdf_bytes:
        st.download_button(
            label="Download PDF" if lang == "English" else "PDFをダウンロード",
            data=pdf_bytes,
            file_name="Quick Staff Room Reference.pdf",
            mime="application/pdf",
            use_container_width=True,
        )
    else:
        st.warning(
            "Couldn’t load the PDF. Confirm it exists in GitHub assets and the filename matches."
            if lang == "English"
            else "PDFを読み込めませんでした。GitHubのassetsに存在し、ファイル名が一致しているか確認してください。"
        )

st.divider()

# ----------------------------
# Core phrase sets (starter content)
# ----------------------------
st.subheader("Foundational phrases" if lang == "English" else "基本フレーズ")

st.markdown(
    (
        "- “I’d like to share some observations about how learning seems to feel for them.”\n"
        "- “This is not about labels. It’s about what support helps.”\n"
        "- “We can take this step by step and adjust as we learn.”\n"
        "- “Different environments can make learning feel easier or harder.”\n"
        "- “Let’s focus on comfort, clarity, and consistency.”"
    )
    if lang == "English"
    else
    (
        "- 「学びがどのように感じられているか、いくつか観察を共有したいです。」\n"
        "- 「ラベルの話ではなく、“どんな支援が助けになるか”の話です。」\n"
        "- 「焦らず一歩ずつ、様子を見ながら調整していけます。」\n"
        "- 「環境によって、学びやすさ／難しさは変わることがあります。」\n"
        "- 「心地よさ・わかりやすさ・一貫性を大切にしたいです。」"
    )
)

st.divider()

st.subheader("For parents" if lang == "English" else "保護者向け")

st.markdown(
    (
        "**Opening**\n"
        "- “Thank you for making time. I want to share what we’re noticing at school.”\n\n"
        "**Neutral observations**\n"
        "- “In some settings, they engage easily; in others, it seems to take more energy.”\n\n"
        "**Collaboration**\n"
        "- “Would it be okay if we try a few small supports and review together?”"
    )
    if lang == "English"
    else
    (
        "**導入**\n"
        "- 「お時間をありがとうございます。学校での様子について共有させてください。」\n\n"
        "**中立的な観察**\n"
        "- 「場面によってはスムーズに取り組めますが、別の場面では少しエネルギーが必要そうです。」\n\n"
        "**協働**\n"
        "- 「いくつか小さな工夫を試して、一緒に振り返ってもよろしいでしょうか。」"
    )
)

st.divider()

st.subheader("For students" if lang == "English" else "生徒向け")

st.markdown(
    (
        "- “Everyone’s brain works in different ways.”\n"
        "- “There’s no single right way—let’s find what helps you.”\n"
        "- “If something feels too loud/fast/hard, we can adjust.”\n"
        "- “You don’t have to explain everything. We can just try what feels better.”"
    )
    if lang == "English"
    else
    (
        "- 「みんな、頭の働き方は少しずつ違うよ。」\n"
        "- 「正しいやり方は一つじゃない。やりやすい方法を一緒に探そう。」\n"
        "- 「うるさい／速い／難しいと感じたら、調整できるよ。」\n"
        "- 「全部説明しなくても大丈夫。楽になる方法を試してみよう。」"
    )
)

st.divider()

st.subheader("For colleagues" if lang == "English" else "同僚向け")

st.markdown(
    (
        "- “Let’s keep our language consistent across classes.”\n"
        "- “I’m noticing patterns across environments rather than ‘good/bad’ behavior.”\n"
        "- “Can we agree on a small set of supports to try for two weeks?”\n"
        "- “Let’s share what works and refine together.”"
    )
    if lang == "English"
    else
    (
        "- 「クラスが変わっても同じ支援が伝わるように、言葉を揃えませんか。」\n"
        "- 「“良い／悪い”ではなく、環境によるパターンとして見ています。」\n"
        "- 「2週間だけ、試す支援を少数に絞って合意しませんか。」\n"
        "- 「うまくいった点を共有して、一緒に改善していきましょう。」"
    )
)

st.caption(
    "Tip: Keep phrasing descriptive and collaborative; avoid labels, conclusions, or urgency."
    if lang == "English"
    else "ヒント：ラベル・結論・緊急性を避け、描写的で協働的な言い回しを意識すると安心感が高まります。"
)
