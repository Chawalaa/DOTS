import streamlit as st
from components.ui import language_toggle, get_lang, page_header

st.set_page_config(page_title="Visual Tools", page_icon="🧩", layout="wide")
language_toggle(sidebar=True)

page_header(
    "Visual & Narrative Tools" if get_lang() == "English" else "視覚／ナラティブツール",
    "Simple metaphors and design guidance to support understanding without labels."
    if get_lang() == "English"
    else "ラベルなしで理解を助けるメタファーとデザイン指針。",
)

st.write(
    "Some ideas are easier to understand through simple metaphors rather than explanations."
    if get_lang() == "English"
    else "説明よりも、シンプルなメタファーの方が理解しやすい場合があります。"
)

st.divider()

# --- Narrative tools (your existing content) ---
with st.expander("Different dots, different strengths", expanded=True):
    st.write(
        "Everyone is made up of many dots.\n\n"
        "Some dots are bright, some are quiet, and some take time to appear.\n\n"
        "When dots are arranged differently, they create different patterns.\n\n"
        "Neurodiversity means that everyone’s pattern is unique, and all patterns have value."
    )

with st.expander("Different waves, different rhythms", expanded=False):
    st.write(
        "Some people move like gentle waves, others like strong waves.\n\n"
        "Some waves need calm space, while others enjoy movement.\n\n"
        "Learning and communication also have rhythms.\n\n"
        "Neurodiversity means respecting different rhythms, not forcing one pattern."
    )

with st.expander("Different paths to the same place", expanded=False):
    st.write(
        "People take different paths when they learn or communicate.\n\n"
        "Some paths are straight; others have curves or pauses.\n\n"
        "Taking a different path does not mean being lost.\n\n"
        "Neurodiversity means allowing different paths to reach understanding."
    )

st.divider()

# --- NEW: Color Guidelines section (Design Language) ---
st.subheader("Color Guidelines" if get_lang() == "English" else "カラーガイドライン")

st.write(
    "Color supports emotional safety, clarity, and non-hierarchical communication. "
    "It expresses variation without implying value, ability, or priority."
    if get_lang() == "English"
    else
    "色は、安心感・明確さ・非階層的なコミュニケーションを支えます。価値や能力の優劣を示すためには使いません。"
)

with st.expander("Palette Direction (soft pastel tones only)", expanded=True):
    st.markdown(
        "- Use a limited pastel palette to maintain calmness and consistency.\n"
        "- Core colors:\n"
        "  - Soft blue\n"
        "  - Mint green\n"
        "  - Peach\n"
        "  - Lavender\n"
        "  - Pale yellow\n"
        "- These choices avoid urgency, evaluation, or medical association."
    )

with st.expander("Color Usage Rules", expanded=False):
    st.markdown(
        "- No single color should dominate a layout.\n"
        "- Color must **not** encode:\n"
        "  - ability\n"
        "  - value\n"
        "  - correctness\n"
        "  - priority\n"
        "- Use colors evenly and gently.\n"
        "- Variation communicates difference **without hierarchy**."
    )

with st.expander("Colors to Avoid", expanded=False):
    st.markdown(
        "- Red/green oppositions\n"
        "- Black–white binaries\n"
        "- Medical, warning, or alert colors\n\n"
        "These combinations can create emotional pressure or evaluative meaning."
    )

with st.expander("Accessibility & Consistency", expanded=False):
    st.markdown(
        "- Support readability on light backgrounds.\n"
        "- Meaning should **never** rely on color alone.\n"
        "- Keep usage consistent across:\n"
        "  - cards\n"
        "  - visuals\n"
        "  - app screens\n"
        "  - printed materials"
    )

st.info(
    "Summary: Color is expressive but restrained—supporting calm communication and shared understanding without judgment."
    if get_lang() == "English"
    else
    "まとめ：色は表現的ですが抑制的に。判断や比較を誘導せず、落ち着いた対話と共通理解を支えます。"
)

# Download button
guidelines_md = """# Color Guidelines

Color supports emotional safety, clarity, and non-hierarchical communication.
Colors express variation and diversity without implying value, ability, correctness, or priority.

## Palette Direction (soft pastel tones only)
Use a limited pastel palette to maintain calmness and consistency.

Core colors:
- Soft blue
- Mint green
- Peach
- Lavender
- Pale yellow

These choices avoid urgency, evaluation, or medical association.

## Color Usage Rules
- No single color should dominate a layout.
- Color must not encode: ability, value, correctness, priority.
- Use colors evenly and gently.
- Variation communicates difference without hierarchy.

## Colors to Avoid
Do not use:
- Red/green oppositions
- Black–white binaries
- Medical, warning, or alert colors

These may introduce emotional pressure or evaluative meaning.

## Accessibility & Consistency
- Support readability on light backgrounds.
- Meaning should never rely on color alone.
- Keep color usage consistent across cards, visuals, app screens, and printed materials.

## Summary
Color is expressive but restrained. It supports calm communication and shared understanding without directing judgment or comparison.
"""

st.download_button(
    label="Download Color Guidelines" if get_lang() == "English" else "カラーガイドラインをダウンロード",
    data=guidelines_md.encode("utf-8"),
    file_name="color_guidelines.md",
    mime="text/markdown",
)
# --- NEW: Typography section (Design Language) ---
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

with st.expander("Text Hierarchy", expanded=False):
    if get_lang() == "English":
        st.markdown(
            "**Section Headings**\n"
            "- Font: Neutral Sans-Serif (**Bold**)\n"
            "- Usage: Section titles, card titles, screen headers\n"
            "- Tone: Calm emphasis, not instructional\n"
            "- Example: *Conversation Support*\n\n"
            "**Sub-Headings**\n"
            "- Font: Neutral Sans-Serif (Regular)\n"
            "- Usage: Labels, short descriptors, categories\n"
            "- Tone: Supportive, non-directive\n"
            "- Example: *Context: Talking with parents*\n\n"
            "**Body Text**\n"
            "- Font: Neutral Sans-Serif (Regular)\n"
            "- Usage: Phrases, guidance text, narratives\n"
            "- Tone: Gentle, explanatory, non-judgmental\n"
            "- Example: “There are situations where learning feels easier, and others where it feels more challenging.”\n\n"
            "**Notes / Captions**\n"
            "- Font: Neutral Sans-Serif (Regular)\n"
            "- Usage: Short reminders, clarifications\n"
            "- Tone: Reassuring, optional\n"
            "- Example: *This is not about diagnosis or labels.*"
        )
    else:
        st.markdown(
            "**セクション見出し**\n"
            "- フォント：Neutral Sans-Serif（**太字**）\n"
            "- 用途：セクションタイトル、カードタイトル、画面ヘッダー\n"
            "- トーン：落ち着いた強調（指示的にしない）\n"
            "- 例：*Conversation Support*\n\n"
            "**サブ見出し**\n"
            "- フォント：Neutral Sans-Serif（標準）\n"
            "- 用途：ラベル、短い説明、カテゴリ\n"
            "- トーン：支援的（誘導しない）\n"
            "- 例：*Context: Talking with parents*\n\n"
            "**本文**\n"
            "- フォント：Neutral Sans-Serif（標準）\n"
            "- 用途：フレーズ、ガイダンス文、ナラティブ\n"
            "- トーン：やさしく説明的（判断しない）\n"
            "- 例：「学びやすい場面もあれば、難しく感じる場面もあります。」\n\n"
            "**注記／キャプション**\n"
            "- フォント：Neutral Sans-Serif（標準）\n"
            "- 用途：短いリマインド、補足\n"
            "- トーン：安心できる（任意）\n"
            "- 例：*This is not about diagnosis or labels.*"
        )

with st.expander("Typography Rules", expanded=False):
    if get_lang() == "English":
        st.markdown(
            "- No decorative or display fonts in communication content\n"
            "- No italics for emphasis\n"
            "- Limited use of bold (headings only)\n"
            "- Line spacing should feel open and breathable\n"
            "- Text should never feel crowded or dense\n"
            "- Typography should support the message, not draw attention to itself"
        )
    else:
        st.markdown(
            "- 装飾的／ディスプレイ系フォントは使用しない\n"
            "- 強調のためのイタリックは使用しない\n"
            "- 太字は見出しのみ（使いすぎない）\n"
            "- 行間は開放的で息ができる感覚に\n"
            "- 文字が詰まって見えないようにする\n"
            "- タイポグラフィは主張せず、メッセージを支える"
        )

with st.expander("What Not to Use", expanded=False):
    if get_lang() == "English":
        st.markdown(
            "- Script or handwritten fonts\n"
            "- Display fonts (e.g., Boston Angel) in body text\n"
            "- Fonts associated with diagnosis, instruction, or authority\n\n"
            "These are excluded to maintain emotional safety and neutrality."
        )
    else:
        st.markdown(
            "- 筆記体／手書き風フォント\n"
            "- 本文でのディスプレイフォント（例：Boston Angel）\n"
            "- 診断・指示・権威を連想させるフォント\n\n"
            "心理的安全性と中立性を守るため、これらは除外します。"
        )

with st.expander("Accessibility Notes", expanded=False):
    if get_lang() == "English":
        st.markdown(
            "- Text must remain readable on light pastel backgrounds\n"
            "- Meaning should never rely on font weight or style alone\n"
            "- Font size should support quick reading in school environments"
        )
    else:
        st.markdown(
            "- 淡いパステル背景でも可読性を確保する\n"
            "- 太さやスタイルだけに意味を依存させない\n"
            "- 学校環境で“ぱっと読める”サイズにする"
        )

st.info(
    "Summary: Typography is functional, calm, and inclusive—part of the communication system, not a stylistic choice."
    if get_lang() == "English"
    else
    "まとめ：タイポグラフィは機能的で落ち着きがあり、インクルーシブ。装飾ではなく、コミュニケーションの一部です。"
)

# Download button
typography_md = """# Typography Guidelines

Typography supports clarity, emotional safety, and cultural neutrality.
Fonts are chosen to reduce cognitive load and avoid authoritative or clinical tone.

## Primary Typeface (Neutral Sans-Serif)
Recommended fonts:
- English: Inter / Source Sans 3
- Japanese: Noto Sans JP

These fonts are:
- highly legible at small sizes
- visually calm and non-decorative
- suitable for educational and professional contexts

## Text Hierarchy
### Section Headings
- Font: Neutral Sans-Serif (Bold)
- Usage: Section titles, card titles, screen headers
- Tone: Calm emphasis, not instructional

### Sub-Headings
- Font: Neutral Sans-Serif (Regular)
- Usage: Labels, short descriptors, categories
- Tone: Supportive, non-directive

### Body Text
- Font: Neutral Sans-Serif (Regular)
- Usage: Phrases, guidance text, narratives
- Tone: Gentle, explanatory, non-judgmental

### Notes / Captions
- Font: Neutral Sans-Serif (Regular)
- Usage: Short reminders, clarifications
- Tone: Reassuring, optional

## Typography Rules
- No decorative or display fonts in communication content
- No italics for emphasis
- Limited use of bold (headings only)
- Line spacing should feel open and breathable
- Text should never feel crowded or dense
- Typography should support the message, not draw attention to itself

## What Not to Use
- Script or handwritten fonts
- Display fonts (e.g., Boston Angel) in body text
- Fonts associated with diagnosis, instruction, or authority

These are excluded to maintain emotional safety and neutrality.

## Accessibility Notes
- Text must remain readable on light pastel backgrounds
- Meaning should never rely on font weight or style alone
- Font size should support quick reading in school environments

## Summary
Typography is functional, calm, and inclusive. It is part of the communication system, not a stylistic choice.
"""

st.download_button(
    label="Download Typography Guidelines" if get_lang() == "English" else "タイポグラフィガイドラインをダウンロード",
    data=typography_md.encode("utf-8"),
    file_name="typography_guidelines.md",
    mime="text/markdown",
)

