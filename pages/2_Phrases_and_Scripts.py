import streamlit as st
from components.ui import language_toggle, get_lang, page_header

st.set_page_config(page_title="Phrases & Scripts", layout="wide")
language_toggle(sidebar=True)

page_header(
    "Phrases & Scripts" if get_lang()=="English" else "フレーズ／台本",
    "Example phrases educators can adapt (strength-based, non-medical, culturally considerate)."
    if get_lang()=="English" else
    "教育者が状況に合わせて調整できる例文（強みベース／非医療的／文化的配慮）。"
)

st.write(
    "This section provides example phrases that educators can adapt when discussing neurodiversity."
    if get_lang()=="English" else
    "このセクションでは、ニューロダイバーシティについて話す際に調整して使える例文を提供します。"
)

st.divider()

st.subheader("Opening with strengths" if get_lang()=="English" else "強みから始める")
st.markdown(
    "- First, I’d like to share some of your child’s strengths.\n"
    "- ○○ has many positive qualities, including curiosity and creativity.\n"
    "- ○○ shows their own unique way of thinking and learning."
)

st.subheader("Describing needs without labels" if get_lang()=="English" else "ラベルなしでニーズを伝える")
st.markdown(
    "- There are situations where learning feels easier, and others where it feels more challenging.\n"
    "- ○○ seems to focus better in quieter or more structured environments.\n"
    "- This is not about what ○○ cannot do, but about how we can support them better."
)

st.subheader("Inviting collaboration" if get_lang()=="English" else "協働を促す")
st.markdown(
    "- We would like to think together about what kind of support might be helpful.\n"
    "- Your insights as a parent are very important to us.\n"
    "- We see this as a shared effort between home and school."
)

st.subheader("Closing the conversation" if get_lang()=="English" else "安心して終える")
st.markdown(
    "- Please feel free to share any concerns or questions at any time.\n"
    "- We can take this step by step.\n"
    "- Our goal is for ○○ to feel comfortable and supported."
)
from pathlib import Path
import streamlit as st

st.divider()
st.subheader("Conversation Support Card" if get_lang() == "English" else "会話サポートカード")

pdf_path = Path("assets/Conversation Support Card .pdf")

if pdf_path.exists():
    pdf_bytes = pdf_path.read_bytes()

    st.caption(
        "View or download the PDF below."
        if get_lang() == "English"
        else "PDFは下から表示またはダウンロードできます。"
    )

    # 1) Download (always works)
    st.download_button(
        label="Download Conversation Support Card (PDF)"
        if get_lang() == "English"
        else "会話サポートカード（PDF）をダウンロード",
        data=pdf_bytes,
        file_name="Conversation Support Card.pdf",
        mime="application/pdf",
        use_container_width=True,
    )

    # 2) View (open in new tab) — safest
    # Streamlit can serve static files if you place them in /static or use st.link_button to the GitHub raw link.
    # Easiest reliable method on Community Cloud: link to the GitHub "raw" file.
    #
    # 👉 Replace the URL below with your own repo raw URL once you confirm your repo name.
    st.info(
        
    )

    # TODO: Replace this with your raw GitHub URL:
    # Example format:
    # https://raw.githubusercontent.com/<USERNAME>/<REPO>/main/assets/Conversation%20Support%20Card .pdf
    pdf_url = "PASTE_YOUR_RAW_GITHUB_PDF_URL_HERE"

    if hasattr(st, "link_button"):
        st.link_button(
            "View Conversation Support Card (PDF)"
            if get_lang() == "English"
            else "会話サポートカード（PDF）を表示",
            pdf_url,
            use_container_width=True,
        )
    else:
        st.markdown(f"[View Conversation Support Card (PDF)]({pdf_url})")

else:
    st.error(
        "PDF not found: assets/Conversation Support Card .pdf. Make sure the filename (including spaces) matches exactly in GitHub."
        if get_lang() == "English"
        else
        "PDFが見つかりません：assets/Conversation Support Card .pdf（スペースを含むファイル名がGitHub上と完全一致しているか確認してください）"
    )
