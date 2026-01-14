import streamlit as st
from components.ui import language_toggle, get_lang, page_header

# Visual tools should feel calm, non-clinical, and non-hierarchical:
# - Soft pastel palette, no dominant color
# - One main idea per card
# - No brain imagery, no faces, no diagnostic symbols, no "improvement" arrows
# (Based on your Framework Design Language rules)  :contentReference[oaicite:1]{index=1}

st.set_page_config(page_title="Visual Tools", page_icon="🧩", layout="wide")
language_toggle(sidebar=True)

page_header(
    "Visual & Narrative Tools" if get_lang() == "English" else "視覚／ナラティブツール",
    "Abstract metaphors that support understanding without labels."
    if get_lang() == "English"
    else "ラベル付けを避けつつ理解を助ける、抽象的なメタファー。"
)

# --- Pastel palette (soft + emotionally safe) ---
PALETTE = {
    "soft_blue": "#DCEBFF",
    "mint": "#D9F5E8",
    "peach": "#FFE2D1",
    "lavender": "#E9E2FF",
    "pale_yellow": "#FFF4C7",
}

def card(title: str, body: str, bg_hex: str):
    """A calm A6-like card style: airy spacing, one idea, neutral tone."""
    st.markdown(
        f"""
        <div style="
            background: {bg_hex};
            border-radius: 18px;
            padding: 18px 18px;
            margin: 10px 0 14px 0;
            border: 1px solid rgba(0,0,0,0.06);
        ">
            <div style="
                font-family: Inter, 'Source Sans 3', 'Noto Sans JP', system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
                font-size: 18px;
                font-weight: 700;
                margin-bottom: 8px;
                color: rgba(0,0,0,0.78);
            ">{title}</div>

            <div style="
                font-family: Inter, 'Source Sans 3', 'Noto Sans JP', system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
                font-size: 15px;
                line-height: 1.7;
                color: rgba(0,0,0,0.72);
            ">{body}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Page intro (don’t rely on color alone; colors are expressive but restrained) ---
st.info(
    "These tools use calm, abstract metaphors. Color is used gently and evenly—never to rank, label, or imply correctness."
    if get_lang() == "English"
    else "落ち着いた抽象メタファーを用います。色はやさしく均等に使い、順位付け・ラベル付け・正しさの示唆に使いません。"
)

st.divider()

# Tabs keep the layout clean and “consultable”
tabs = st.tabs(
    ["Dots", "Waves", "Paths"] if get_lang() == "English" else ["ドット", "波", "道（パス）"]
)

# --- DOTS ---
with tabs[0]:
    st.subheader("Dots: Different patterns, shared value" if get_lang() == "English" else "ドット：違う配置、同じ価値")

    card(
        "What it means" if get_lang() == "English" else "意味",
        (
            "Everyone is made up of many dots. Some dots are bright, some are quiet, and some take time to appear. "
            "Different arrangements create different patterns—and every pattern can be meaningful."
            if get_lang() == "English"
            else
            "人はたくさんの「ドット」でできています。目立つドットもあれば、静かなドットもあり、時間をかけて見えてくるドットもあります。"
            "配置が違えば模様も違い、どの模様にも意味があります。"
        ),
        PALETTE["soft_blue"],
    )

    card(
        "How to use it in a conversation" if get_lang() == "English" else "会話での使い方",
        (
            "Use dots to describe variation without labeling. Keep it observational: "
            "“I notice different situations bring out different dots.” Then ask: “Which dots feel easiest at home?”"
            if get_lang() == "English"
            else
            "ラベルではなく「違い」を伝えるために使います。観察ベースで："
            "「場面によって出てくるドットが違うように見えます」→「家ではどんなドットが出やすいですか？」と尋ねます。"
        ),
        PALETTE["mint"],
    )

    card(
        "One gentle reminder" if get_lang() == "English" else "やさしい一言",
        (
            "This is not about what someone cannot do—it’s about which environments help their pattern show clearly."
            if get_lang() == "English"
            else
            "できないことの話ではなく、どんな環境だとその人の模様が見えやすいか、という話です。"
        ),
        PALETTE["pale_yellow"],
    )

# --- WAVES ---
with tabs[1]:
    st.subheader("Waves: Different rhythms" if get_lang() == "English" else "波：それぞれのリズム")

    card(
        "What it means" if get_lang() == "English" else "意味",
        (
            "People have different rhythms for attention, energy, and communication. "
            "Some rhythms need calm space; others need movement or variety."
            if get_lang() == "English"
            else
            "注意・エネルギー・コミュニケーションにはそれぞれのリズムがあります。"
            "落ち着いた空間が合うリズムもあれば、動きや変化が合うリズムもあります。"
        ),
        PALETTE["lavender"],
    )

    card(
        "How to use it in a conversation" if get_lang() == "English" else "会話での使い方",
        (
            "Use waves to normalize fluctuation: “Some days are calmer, some are stronger.” "
            "Then collaboratively identify supports: “What helps the wave feel steady at school?”"
            if get_lang() == "English"
            else
            "波で「ゆらぎ」を普通のものとして扱います："
            "「穏やかな日もあれば、強い日もあります」→「学校で波が整いやすい工夫は何でしょう？」と一緒に考えます。"
        ),
        PALETTE["peach"],
    )

    card(
        "One gentle reminder" if get_lang() == "English" else "やさしい一言",
        (
            "Different rhythms are not problems to fix. They are patterns to understand."
            if get_lang() == "English"
            else
            "違うリズムは直すべき問題ではなく、理解すべきパターンです。"
        ),
        PALETTE["soft_blue"],
    )

# --- PATHS ---
with tabs[2]:
    st.subheader("Paths: Different routes to understanding" if get_lang() == "English" else "道（パス）：理解への別ルート")

    card(
        "What it means" if get_lang() == "English" else "意味",
        (
            "People take different routes when they learn or communicate. Some routes are direct; others include pauses, curves, or detours. "
            "A different route doesn’t mean being lost."
            if get_lang() == "English"
            else
            "学び方・伝え方には別ルートがあります。まっすぐな道もあれば、休憩や曲がり道、遠回りがある道もあります。"
            "別ルートは「迷っている」ことではありません。"
        ),
        PALETTE["mint"],
    )

    card(
        "How to use it in a conversation" if get_lang() == "English" else "会話での使い方",
        (
            "Use ‘paths’ to reduce pressure. Instead of “progress” talk, use “fit”: "
            "“Which route helps understanding happen with less stress?”"
            if get_lang() == "English"
            else
            "プレッシャーを下げるために使います。「成長／改善」ではなく「合う道」に寄せます："
            "「どんなルートだと、負担が少なく理解につながりますか？」"
        ),
        PALETTE["pale_yellow"],
    )

    card(
        "One gentle reminder" if get_lang() == "English" else "やさしい一言",
        (
            "Support is not about pushing forward. It’s about making the route feel safer."
            if get_lang() == "English"
            else
            "支援は前に押すことではなく、その道を安心にすることです。"
        ),
        PALETTE["lavender"],
    )

st.divider()

with st.expander("Design boundaries (kept intentionally non-clinical)", expanded=False):
    st.write(
        "- No brain imagery\n"
        "- No human figures/faces\n"
        "- No diagnostic icons/labels\n"
        "- No arrows implying improvement/correction\n"
        "- No normal/abnormal comparisons\n\n"
        "These boundaries protect emotional safety and avoid unintended hierarchy."
        if get_lang() == "English"
        else
        "・脳のイメージは使わない\n"
        "・人の顔や人物図は使わない\n"
        "・診断アイコン／ラベルは使わない\n"
        "・改善／修正を示す矢印は使わない\n"
        "・正常／異常の比較は使わない\n\n"
        "これらは心理的安全性を守り、意図しない序列化を避けるための境界です。"
    )

