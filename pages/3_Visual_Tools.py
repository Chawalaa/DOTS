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

