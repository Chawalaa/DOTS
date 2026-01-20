import streamlit as st
from components.ui import apply_brand_styles, set_sidebar_branding, language_toggle, get_lang, page_header

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

from pathlib import Path
import streamlit as st

# --- Visual Metaphors (structured like Color Guidelines + PDF downloads) ---
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

def pdf_download_button(label_en: str, label_ja: str, pdf_filename: str):
    """Reusable PDF download button for assets/ PDFs (supports spaces in filenames)."""
    pdf_path = Path("assets") / pdf_filename
    if pdf_path.exists():
        st.download_button(
            label=label_en if get_lang() == "English" else label_ja,
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

    pdf_download_button(
        label_en="Download Dots Narrative (PDF)",
        label_ja="Dots ナラティブ（PDF）をダウンロード",
        pdf_filename="Dots Narrative.pdf",
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

    pdf_download_button(
        label_en="Download Waves Narrative (PDF)",
        label_ja="Waves ナラティブ（PDF）をダウンロード",
        pdf_filename="Waves Narrative.pdf",
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

    pdf_download_button(
        label_en="Download Pathways Narrative (PDF)",
        label_ja="Pathways ナラティブ（PDF）をダウンロード",
        pdf_filename="Pathways Narrative.pdf",
    )

st.info(
    "Tip: These metaphors work best when paired with strengths-based language and non-evaluative phrasing."
    if get_lang() == "English"
    else
    "ヒント：これらのメタファーは、強みベースで評価しない言い回しと組み合わせると最も効果的です。"
)


from pathlib import Path
import streamlit as st

# --- Color Guidelines (with PDF download from assets/) ---
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

# PDF download (assets/color_guidelines.pdf)
pdf_path = Path("assets/color_guidelines.pdf")

if pdf_path.exists():
    st.download_button(
        label="Download Color Guidelines (PDF)" if get_lang() == "English" else "カラーガイドライン（PDF）をダウンロード",
        data=pdf_path.read_bytes(),
        file_name="color_guidelines.pdf",
        mime="application/pdf",
        use_container_width=True,
    )
else:
    st.error(
        "PDF not found: assets/color_guidelines.pdf. Upload it to your GitHub repo under the assets/ folder."
        if get_lang() == "English"
        else
        "PDFが見つかりません：assets/color_guidelines.pdf をGitHubリポジトリの assets/ フォルダにアップロードしてください。"
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
    "Summary: Typography is functional, calm, and inclusive; part of the communication system, not a stylistic choice."
    if get_lang() == "English"
    else
    "まとめ：タイポグラフィは機能的で落ち着きがあり、インクルーシブ。装飾ではなく、コミュニケーションの一部です。"
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

# --- NEW: Explicit Exclusions ---
st.subheader("Explicit Exclusions" if get_lang() == "English" else "明確な除外項目")

st.write(
    "Certain visual elements are intentionally excluded to protect the framework’s non-clinical, and non-evaluative positioning. "
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

