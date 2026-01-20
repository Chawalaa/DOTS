import streamlit as st
from pathlib import Path

from components.ui import apply_brand_styles, set_sidebar_branding, language_toggle, get_lang, page_header

st.set_page_config(page_title="Contact Team", layout="wide", initial_sidebar_state="collapsed")

# Branding + sidebar
apply_brand_styles()
set_sidebar_branding("Menu")
language_toggle(sidebar=True)

lang = get_lang()

page_header(
    "Contact Team" if lang == "English" else "お問い合わせ",
    "Reach the project team, share questions, or request collaboration."
    if lang == "English"
    else "質問・相談・連携のご希望はこちらからご連絡ください。",
)

# --- Recommended contact methods ---
st.subheader("How to reach us" if lang == "English" else "連絡方法")

st.markdown(
    """
- **Email:** chawala.banda@keio.jp  
- **Response time:** 2–5 business days  
- **For schools:** Please include school name, role, and preferred language (English/Japanese)
"""
    if lang == "English"
    else
    """
- **メール：** chawala.banda@keio.jp  
- **返信目安：** 2〜5営業日  
- **学校関係の方：** 学校名・ご担当・希望言語（日本語／英語）を添えてください
"""
)

st.divider()

# --- Quick message form (sends nowhere; shows copy-paste email) ---
st.subheader("Send a message" if lang == "English" else "メッセージを送る")

with st.form("contact_form"):
    name = st.text_input("Your name" if lang == "English" else "お名前")
    affiliation = st.text_input("Affiliation (optional)" if lang == "English" else "所属（任意）")
    email = st.text_input("Your email (optional)" if lang == "English" else "メールアドレス（任意）")
    topic = st.selectbox(
        "Topic" if lang == "English" else "内容",
        [
            "General question",
            "School implementation",
            "Workshop / training request",
            "Collaboration / research",
            "Report an issue",
            "Other",
        ]
        if lang == "English"
        else
        [
            "一般的な質問",
            "学校導入について",
            "研修・ワークショップ依頼",
            "共同研究・連携",
            "不具合の報告",
            "その他",
        ],
    )
    message = st.text_area(
        "Message" if lang == "English" else "メッセージ",
        height=160,
        placeholder="Write your message here..." if lang == "English" else "ここにご記入ください…",
    )
    consent = st.checkbox(
        "I understand this is not a diagnostic service."
        if lang == "English"
        else "これは診断サービスではないことを理解しています。"
    )

    submitted = st.form_submit_button("Generate email text" if lang == "English" else "メール文を生成")

if submitted:
    if not consent:
        st.warning(
            "Please tick the acknowledgement checkbox before generating."
            if lang == "English"
            else "生成の前に確認チェックを入れてください。"
        )
    else:
        # Create a copy-paste email (since Streamlit Cloud cannot send email by default)
        to_address = "chawala.banda@keio.jp"
        subject = f"[Toolkit Contact] {topic}"
        body = (
            f"Name: {name}\n"
            f"Affiliation: {affiliation}\n"
            f"Email: {email}\n"
            f"Topic: {topic}\n\n"
            f"Message:\n{message}\n"
        )

        st.success(
            "Copy and paste the text below into your email app."
            if lang == "English"
            else "下の文章をコピーしてメールに貼り付けてください。"
        )

        st.code(f"To: {to_address}\nSubject: {subject}\n\n{body}", language="text")

        # Optional convenience button to open mail client
        st.markdown(
            f"[Open email draft in your mail app]"
            f"(mailto:{to_address}?subject={subject.replace(' ', '%20')})"
            if lang == "English"
            else
            f"[メールアプリで下書きを開く]"
            f"(mailto:{to_address}?subject={subject.replace(' ', '%20')})"
        )

st.divider()

# --- Footer note ---
st.caption(
    "This toolkit supports communication and understanding. It does not provide diagnosis or clinical assessment."
    if lang == "English"
    else "本ツールキットは理解と対話を支援するものであり、診断や臨床評価は行いません。"
)
