import streamlit as st
from components.ui import language_toggle, get_lang, page_header

st.set_page_config(page_title="About", page_icon="ℹ️", layout="wide")
language_toggle(sidebar=True)

page_header("About This Toolkit" if get_lang()=="English" else "ツールキットについて")

st.write(
    "This toolkit is part of a research project on culturally responsive communication for neurodiversity in Japan.\n\n"
    "It is based on the idea that communication itself plays a key role in inclusion—especially in high-context cultural "
    "settings where harmony and indirect expression are valued."
    if get_lang()=="English" else
    "本ツールキットは、日本におけるニューロダイバーシティの文化応答的コミュニケーションに関する研究プロジェクトの一部です。\n\n"
    "特に、調和や間接表現が重視されるハイコンテクスト文化において、コミュニケーションそのものがインクルージョンの鍵になるという考えに基づいています。"
)

st.subheader("Framework (3 layers)" if get_lang()=="English" else "フレームワーク（3層）")
st.markdown(
    "- **Language Layer:** Tone, phrasing, and indirect communication that reduce emotional risk.\n"
    "- **Visual Layer:** Abstract metaphors and visuals that support understanding without labels.\n"
    "- **Interaction Layer:** Conversation structures that support collaboration and trust."
)

st.warning(
    "Disclaimer: This toolkit is not a diagnostic or medical tool. It does not assess, label, or classify individuals. "
    "Its purpose is to support communication and understanding."
    if get_lang()=="English" else
    "免責事項：本ツールキットは診断や医療目的のツールではありません。個人を評価・ラベル付け・分類しません。目的は対話と理解の支援です。"
)
