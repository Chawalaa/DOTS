import streamlit as st
from components.ui import apply_brand_styles, set_sidebar_branding, language_toggle, get_lang, page_header

st.set_page_config(page_title="Phrases & Scripts", layout="wide", initial_sidebar_state="collapsed")

# Branding + sidebar
apply_brand_styles()
set_sidebar_branding("Menu")
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
import urllib.parse

st.divider()
st.subheader("Conversation Support Card" if get_lang() == "English" else "会話サポートカード")

# IMPORTANT: your filename has a space before .pdf
pdf_path = Path("assets/Conversation Support Card .pdf")

raw_pdf_url = "https://raw.githubusercontent.com/Chawalaa/DOTS/main/assets/Conversation%20Support%20Card%20.pdf"

# This viewer URL forces in-browser viewing
viewer_url = "https://drive.google.com/viewerng/viewer?embedded=true&url=" + urllib.parse.quote(raw_pdf_url, safe="")

if pdf_path.exists():
    pdf_bytes = pdf_path.read_bytes()

    st.caption(
        "View the PDF in a new tab, or download it below."
        if get_lang() == "English"
        else "PDFは新しいタブで表示するか、下からダウンロードできます。"
    )

    # View (opens in a viewer tab, not download)
    if hasattr(st, "link_button"):
        st.link_button(
            "View Conversation Support Card (PDF)"
            if get_lang() == "English"
            else "会話サポートカード（PDF）を表示",
            viewer_url,
            use_container_width=True,
        )
    else:
        st.markdown(
            f"[{('View Conversation Support Card (PDF)' if get_lang() == 'English' else '会話サポートカード（PDF）を表示')}]({viewer_url})"
        )

    # Download (from your app assets — always works)
    st.download_button(
        label="Download Conversation Support Card (PDF)"
        if get_lang() == "English"
        else "会話サポートカード（PDF）をダウンロード",
        data=pdf_bytes,
        file_name="Conversation Support Card.pdf",
        mime="application/pdf",
        use_container_width=True,
    )

else:
    st.error(
        "PDF not found in the app at: assets/Conversation Support Card .pdf. "
        "Make sure the filename matches exactly (including the space before .pdf)."
        if get_lang() == "English"
        else
        "アプリ内でPDFが見つかりません：assets/Conversation Support Card .pdf。"
        "ファイル名が完全一致しているか（.pdfの前のスペース含む）確認してください。"
    )
