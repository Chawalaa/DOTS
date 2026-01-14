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
# --- NEW: Layout & Material Rules ---
st.subheader("Layout & Material Rules" if get_lang() == "English" else "レイアウト／素材ルール")

st.write(
    "Layout and material choices are designed to support clarity, calm attention, and ease of use. "
    "The goal is quick consultation in real-world educational settings."
    if get_lang() == "English"
    else
    "レイアウトと素材の選択は、明確さ・落ち着いた注意・使いやすさを支えるために設計します。"
    "教育現場で“すぐ参照できる”ことを優先します。"
)

with st.expander("Layout Principles", expanded=True):
    if get_lang() == "English":
        st.markdown(
            "- Use generous margins and white space\n"
            "- Avoid dense or cluttered layouts\n"
            "- Maintain clear visual hierarchy\n"
            "- Allow content to breathe\n"
            "- Layouts should feel open, calm, and approachable"
        )
    else:
        st.markdown(
            "- 余白（マージン）とホワイトスペースを十分に取る\n"
            "- 密集／ごちゃごちゃした配置を避ける\n"
            "- 明確な視覚的ヒエラルキー（見出し→本文）を保つ\n"
            "- 情報が“息ができる”配置にする\n"
            "- 開放的で落ち着きがあり、話しかけやすい印象にする"
        )

with st.expander("Content Focus", expanded=False):
    if get_lang() == "English":
        st.markdown(
            "- One main idea per card or screen\n"
            "- Avoid combining multiple instructions or messages\n"
            "- Break information into short, digestible units\n"
            "- This supports quick understanding and reduces cognitive load"
        )
    else:
        st.markdown(
            "- 1枚（1画面）につき主題は1つ\n"
            "- 複数の指示／メッセージを混ぜない\n"
            "- 短く消化しやすい単位に分ける\n"
            "- すばやい理解と認知負荷の軽減につながる"
        )

with st.expander("Suitable Formats", expanded=False):
    if get_lang() == "English":
        st.markdown(
            "- A6 narrative cards\n"
            "- Quick-reference guides\n"
            "- Mobile-first app screens\n\n"
            "These reflect how educators access information during daily practice."
        )
    else:
        st.markdown(
            "- A6ナラティブカード\n"
            "- クイック参照ガイド\n"
            "- モバイル前提のアプリ画面\n\n"
            "教育者が日常の実践の中で情報にアクセスする方法を前提にしています。"
        )

with st.expander("Interaction Philosophy", expanded=False):
    if get_lang() == "English":
        st.markdown(
            "- Layouts are designed to be consulted, not studied\n"
            "- Content should be readable at a glance\n"
            "- Users should not need extended attention or explanation\n"
            "- Tools should support, not interrupt, communication"
        )
    else:
        st.markdown(
            "- レイアウトは「学習」ではなく「参照」される設計\n"
            "- ひと目で読めること\n"
            "- 長い集中や追加説明を必要としないこと\n"
            "- 会話を妨げず、支えるツールであること"
        )

with st.expander("Consistency Across Materials", expanded=False):
    if get_lang() == "English":
        st.markdown(
            "- Keep layout rules consistent across:\n"
            "  - printed cards\n"
            "  - app screens\n"
            "  - visual tools\n\n"
            "Consistency supports familiarity and emotional safety over time."
        )
    else:
        st.markdown(
            "- ルールは次の媒体で一貫させる：\n"
            "  - 印刷カード\n"
            "  - アプリ画面\n"
            "  - 視覚ツール\n\n"
            "一貫性は、慣れと安心感（心理的安全性）を積み重ねます。"
        )

st.info(
    "Summary: Layout emphasizes restraint, clarity, and usability so the tools remain supportive rather than demanding."
    if get_lang() == "English"
    else
    "まとめ：レイアウトは抑制・明確さ・実用性を重視し、ツールが“負担”ではなく“支え”として機能するようにします。"
)

layout_md = """# Layout & Material Rules

Layout and material choices support clarity, calm attention, and ease of use.
The framework prioritizes layouts that can be consulted quickly in real-world educational settings.

## Layout Principles
- Use generous margins and white space
- Avoid dense or cluttered layouts
- Maintain clear visual hierarchy
- Allow content to breathe
- Layouts should feel open, calm, and approachable

## Content Focus
- One main idea per card or screen
- Avoid combining multiple instructions or messages
- Break information into short, digestible units
- Supports quick understanding and reduces cognitive load

## Suitable Formats
- A6 narrative cards
- Quick-reference guides
- Mobile-first app screens

These formats reflect how educators access information during daily practice.

## Interaction Philosophy
- Layouts are designed to be consulted, not studied
- Content should be readable at a glance
- Users should not need extended attention or explanation
- Tools should support, not interrupt, communication

## Consistency Across Materials
Keep layout rules consistent across:
- printed cards
- app screens
- visual tools

Consistency supports familiarity and emotional safety over time.

## Summary
Layout emphasizes restraint, clarity, and usability, ensuring tools remain supportive rather than demanding.
"""

st.download_button(
    label="Download Layout & Material Rules" if get_lang() == "English" else "レイアウト／素材ルールをダウンロード",
    data=layout_md.encode("utf-8"),
    file_name="layout_material_rules.md",
    mime="text/markdown",
)

st.divider()

# --- NEW: Explicit Exclusions ---
st.subheader("Explicit Exclusions" if get_lang() == "English" else "明確な除外項目")

st.write(
    "Certain visual elements are intentionally excluded to protect the framework’s non-clinical, non-evaluative positioning. "
    "These exclusions help prevent labeling, comparison, or unintended judgment."
    if get_lang() == "English"
    else
    "本フレームワークが「非臨床／非評価」の立ち位置を保つため、特定の表現を意図的に除外します。"
    "これにより、ラベル付け・比較・意図しない判断を防ぎます。"
)

with st.expander("Not Permitted Within the Framework", expanded=True):
    if get_lang() == "English":
        st.markdown(
            "- Brain imagery\n"
            "- Human figures or faces\n"
            "- Diagnostic icons or medical symbols\n"
            "- Labels associated with disability or assessment\n"
            "- Arrows indicating “improvement,” “correction,” or progression\n"
            "- Visuals implying normal / abnormal distinctions"
        )
    else:
        st.markdown(
            "- 脳のイメージ\n"
            "- 人物（顔を含む）\n"
            "- 診断アイコン／医療シンボル\n"
            "- 障害や評価・判定を連想させるラベル\n"
            "- 「改善」「矯正」「進歩」を示す矢印\n"
            "- 正常／異常の区別を示唆する表現"
        )

with st.expander("Rationale", expanded=False):
    if get_lang() == "English":
        st.markdown(
            "These elements may:\n"
            "- introduce clinical or diagnostic associations\n"
            "- suggest deficit-based thinking\n"
            "- create unintended hierarchy or comparison\n"
            "- reduce emotional safety in communication\n\n"
            "Their exclusion supports neutral, culturally responsive communication."
        )
    else:
        st.markdown(
            "これらの要素は次のリスクがあります：\n"
            "- 臨床／診断の連想を生む\n"
            "- 欠如ベースの見方につながる\n"
            "- 意図しない序列化や比較を生む\n"
            "- 対話の心理的安全性を下げる\n\n"
            "除外することで、中立で文化応答的なコミュニケーションを守ります。"
        )

with st.expander("Design Boundary (applies across formats)", expanded=False):
    if get_lang() == "English":
        st.markdown(
            "These exclusions apply across:\n"
            "- app screens\n"
            "- narrative cards\n"
            "- posters\n"
            "- printed materials\n"
            "- visual tools\n\n"
            "Consistency ensures the framework remains emotionally safe and non-stigmatizing."
        )
    else:
        st.markdown(
            "この除外は次の媒体すべてに適用します：\n"
            "- アプリ画面\n"
            "- ナラティブカード\n"
            "- ポスター\n"
            "- 印刷物\n"
            "- 視覚ツール\n\n"
            "一貫性によって、心理的安全性と非スティグマ性を保ちます。"
        )

st.info(
    "Summary: Exclusions are protective boundaries that preserve the framework’s intent and integrity."
    if get_lang() == "English"
    else
    "まとめ：除外項目は“制限”ではなく、意図と一貫性を守るための保護的な境界です。"
)

exclusions_md = """# Explicit Exclusions

Certain visual elements are intentionally excluded to protect the framework’s non-clinical, non-evaluative positioning.
These exclusions help prevent labeling, comparison, or unintended judgment.

## Not Permitted Within the Framework
Do not use:
- Brain imagery
- Human figures or faces
- Diagnostic icons or medical symbols
- Labels associated with disability or assessment
- Arrows indicating “improvement,” “correction,” or progression
- Visuals implying normal / abnormal distinctions

## Rationale
These elements may:
- introduce clinical or diagnostic associations
- suggest deficit-based thinking
- create unintended hierarchy or comparison
- reduce emotional safety in communication

Their exclusion supports neutral, culturally responsive communication.

## Design Boundary
These exclusions apply across all formats:
- app screens
- narrative cards
- posters
- printed materials
- visual tools

Consistency ensures the framework remains emotionally safe and non-stigmatizing.

## Summary
Exclusions are protective boundaries that preserve the framework’s intent and integrity.
"""

st.download_button(
    label="Download Explicit Exclusions" if get_lang() == "English" else "除外項目をダウンロード",
    data=exclusions_md.encode("utf-8"),
    file_name="explicit_exclusions.md",
    mime="text/markdown",
)

