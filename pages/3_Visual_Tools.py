import streamlit as st
from components.ui import language_toggle, get_lang, page_header

st.set_page_config(page_title="Visual Tools", page_icon="🧩", layout="wide")
language_toggle(sidebar=True)

page_header(
    "Visual & Narrative Tools" if get_lang()=="English" else "視覚／ナラティブツール",
    "Simple metaphors to support understanding without labels."
    if get_lang()=="English" else
    "ラベル付けを避けつつ理解を助ける、シンプルなメタファー。"
)

st.write(
    "Some ideas are easier to understand through simple metaphors rather than explanations."
    if get_lang()=="English" else
    "説明よりも、シンプルなメタファーの方が理解しやすい場合があります。"
)

st.divider()

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

st.caption("Source: DOTS toolkit layout. :contentReference[oaicite:3]{index=3}")
