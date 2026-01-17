import streamlit as st

from components.ui import (
    apply_brand_styles,
    set_sidebar_branding,
    language_toggle,
    get_lang,
    page_header,
    get_app_icon_path,
)

st.set_page_config(
    page_title="Guides",
    page_icon=get_app_icon_path(),
    layout="wide",
)

# Global look + sidebar "Menu" above pages + language toggle
apply_brand_styles()
set_sidebar_branding("Menu")
language_toggle(sidebar=True)

lang = get_lang()

page_header(
    "Guides for Common Situations" if lang == "English" else "よくある場面のガイド",
    "Short structures for conversations educators often find stressful or unclear."
    if lang == "English"
    else "ストレスや不明確さを感じやすい場面で使える、短い会話構造。",
)

st.write(
    "These guides offer structure for situations that educators often find stressful or unclear."
    if lang == "English"
    else "このガイドは、教育者がストレスや曖昧さを感じやすい場面で、会話に骨組みを与えます。"
)

st.divider()

# --- Parents ---
st.subheader("First conversation with parents" if lang == "English" else "保護者との最初の会話")

st.markdown(
    (
        "**Keep in mind:**\n"
        "- Start with strengths and observations, not conclusions\n"
        "- Avoid technical or diagnostic language\n"
        "- Allow silence and reflection\n\n"
        "**Suggested approach:**\n"
        "1) Share positive observations\n"
        "2) Describe learning environments that help\n"
        "3) Invite collaboration rather than agreement\n\n"
        "**Example closing line:**\n"
        "“We can take this step by step, and we’ll think together about what support feels helpful.”"
    )
    if lang == "English"
    else
    (
        "**ポイント：**\n"
        "- 結論ではなく、強みと観察から始める\n"
        "- 専門用語／診断的な言葉を避ける\n"
        "- 沈黙や振り返りの時間を許容する\n\n"
        "**進め方（例）：**\n"
        "1) ポジティブな観察を共有\n"
        "2) 学びやすい環境・条件を説明\n"
        "3) 同意を求めるより、協働を提案する\n\n"
        "**締めの一言（例）：**\n"
        "「焦らず一歩ずつ、一緒に“合う支援”を考えていけたらと思います。」"
    )
)

st.divider()

# --- Students ---
st.subheader("Talking with students" if lang == "English" else "生徒と話す")

st.markdown(
    (
        "**Keep in mind:**\n"
        "- Use age-appropriate language\n"
        "- Avoid making the student feel “different” or “wrong”\n"
        "- Focus on comfort and learning styles\n\n"
        "**Suggested approach:**\n"
        "1) Explain that everyone learns differently\n"
        "2) Use simple metaphors (dots/waves/pathways)\n"
        "3) Emphasize support, not correction\n\n"
        "**Example line:**\n"
        "“There’s no single ‘right’ way—let’s find the way that feels easiest for you.”"
    )
    if lang == "English"
    else
    (
        "**ポイント：**\n"
        "- 年齢に合った言葉で話す\n"
        "- 「違う／間違い」を感じさせない\n"
        "- 心地よさと学び方に焦点を置く\n\n"
        "**進め方（例）：**\n"
        "1) 人それぞれ学び方が違うと伝える\n"
        "2) ドット／波／道筋などのメタファーを使う\n"
        "3) 矯正ではなく“支え”を強調する\n\n"
        "**例文：**\n"
        "「正しいやり方は一つじゃないよ。あなたが一番やりやすい方法を一緒に探そう。」"
    )
)

st.divider()

# --- Colleagues ---
st.subheader("Talking with colleagues" if lang == "English" else "同僚と話す")

st.markdown(
    (
        "**Keep in mind:**\n"
        "- Aim for shared understanding, not persuasion\n"
        "- Use consistent language across staff\n"
        "- Keep it practical\n\n"
        "**Suggested approach:**\n"
        "1) Share observations, not judgments\n"
        "2) Focus on classroom strategies and environment\n"
        "3) Align on supportive language and next steps\n\n"
        "**Example line:**\n"
        "“Let’s keep the language consistent so the student experiences the same support across classes.”"
    )
    if lang == "English"
    else
    (
        "**ポイント：**\n"
        "- 説得より“共通理解”を目指す\n"
        "- 職員間で言葉づかいを揃える\n"
        "- 実務的・具体的にする\n\n"
        "**進め方（例）：**\n"
        "1) 判断ではなく観察を共有\n"
        "2) 教室の工夫や環境に焦点を当てる\n"
        "3) 支援的な言葉と次の一手を揃える\n\n"
        "**例文：**\n"
        "「クラスが変わっても同じ支援が伝わるように、言葉を揃えませんか。」"
    )
)

st.caption(
    "These guides are designed to stay non-clinical, non-evaluative, and collaboration-focused."
    if lang == "English"
    else "このガイドは、非臨床・非評価・協働重視の立ち位置を保つために設計されています。"
)

