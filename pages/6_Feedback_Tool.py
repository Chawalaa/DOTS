import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import csv
import io

# If you already have your language toggle helpers, keep this import.
# If not, you can delete these 2 lines and also delete the language_toggle/get_lang usage below.
try:
    from components.ui import language_toggle, get_lang
except Exception:
    language_toggle = None
    get_lang = lambda: "English"

# Your Google Form URL (expanded from your short forms.gle link)
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScifOKrnjNajCSDbCwWBGdaw8HfZzH5lEaz9qZY5BZtysfJ_w/viewform?usp=send_form"

st.set_page_config(page_title="Feedback Tool", layout="wide")

if language_toggle:
    language_toggle(sidebar=True)

lang = get_lang()

title = "Feedback Tool" if lang == "English" else "フィードバック"
subtitle = (
    "Share feedback to help improve the toolkit. Your responses are collected via Google Forms."
    if lang == "English"
    else "ツールキット改善のためのフィードバックをお寄せください。回答はGoogleフォームで収集されます。"
)

st.title(title)
st.caption(subtitle)
st.divider()

# --- Primary: Link button (always works) ---
st.subheader("Submit via Google Form" if lang == "English" else "Googleフォームで送信")
st.write(
    "If the embedded form doesn’t load, use the button below."
    if lang == "English"
    else "埋め込みフォームが表示されない場合は、下のボタンから開いてください。"
)

# Streamlit has st.link_button in newer versions; fall back to markdown if not available.
if hasattr(st, "link_button"):
    st.link_button(
        "Open Feedback Form" if lang == "English" else "フィードバックフォームを開く",
        FORM_URL,
        use_container_width=True,
    )
else:
    st.markdown(f"- [{('Open Feedback Form' if lang == 'English' else 'フィードバックフォームを開く')}]({FORM_URL})")

st.divider()

# --- Embed: Google Form inside the page ---
st.subheader("Fill the form here" if lang == "English" else "ここで回答する")

# Use an iframe embed. If you have the special embed URL, you can replace FORM_URL with it.
# Often, Google Forms embed works best with /viewform?embedded=true
embed_url = FORM_URL
if "embedded=true" not in embed_url:
    joiner = "&" if "?" in embed_url else "?"
    embed_url = f"{embed_url}{joiner}embedded=true"

components.iframe(embed_url, height=950, scrolling=True)

st.divider()

# --- Optional backup: Simple in-app form + CSV download ---
with st.expander("Backup: Quick feedback (downloadable CSV)", expanded=False):
    st.write(
        "Use this only if Google Forms is unavailable. You can download your entry as a CSV and send it to the project team."
        if lang == "English"
        else "Googleフォームが使えない場合の予備です。入力内容をCSVとしてダウンロードできます。"
    )

    with st.form("quick_feedback"):
        name = st.text_input("Name (optional)" if lang == "English" else "お名前（任意）")
        role = st.selectbox(
            "Your role" if lang == "English" else "立場",
            ["Teacher/Educator", "School staff", "Parent/Guardian", "Student", "Other"]
            if lang == "English"
            else ["教員", "学校職員", "保護者", "生徒", "その他"],
        )
        rating = st.slider(
            "Overall usefulness" if lang == "English" else "全体の有用性",
            min_value=1, max_value=5, value=4,
        )
        comment = st.text_area(
            "What worked well? What should be improved?"
            if lang == "English"
            else "良かった点／改善点を教えてください。",
            height=140,
        )
        submitted = st.form_submit_button("Generate CSV" if lang == "English" else "CSVを作成")

    if submitted:
        ts = datetime.utcnow().isoformat()
        rows = [
            ["timestamp_utc", ts],
            ["name", name],
            ["role", role],
            ["rating_1_5", str(rating)],
            ["comment", comment],
        ]

        # Create a simple 2-column CSV
        buf = io.StringIO()
        w = csv.writer(buf)
        w.writerow(["field", "value"])
        for r in rows:
            w.writerow(r)

        st.success("CSV ready." if lang == "English" else "CSVを作成しました。")
        st.download_button(
            label="Download CSV" if lang == "English" else "CSVをダウンロード",
            data=buf.getvalue().encode("utf-8"),
            file_name="toolkit_feedback.csv",
            mime="text/csv",
        )
