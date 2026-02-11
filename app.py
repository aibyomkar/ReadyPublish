import streamlit as st
import re
import unicodedata

# -------------------------
# Cleaning Engine
# -------------------------
def clean_ai_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    cleaned_chars = []
    for char in text:
        category = unicodedata.category(char)
        if (
            category in ("Cf", "Cs", "Co", "Cn", "Mn") or
            (category == "Cc" and char not in ("\n", "\t"))
        ):
            continue
        cleaned_chars.append(char)

    text = "".join(cleaned_chars)
    text = text.replace("—", " ").replace("–", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title="AIClean", layout="wide")


# -------------------------
# Session State
# -------------------------
if "cleaned_text" not in st.session_state:
    st.session_state.cleaned_text = ""


# -------------------------
# UI Styling
# -------------------------
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 0.8rem !important;
        padding-bottom: 0rem !important;
        max-width: 1200px;
    }

    header, footer { visibility: hidden; }

    .stApp {
        background: radial-gradient(circle at 15% 20%, #1e293b 0%, #0f172a 45%, #020617 100%);
        color: #e2e8f0;
    }

    h1 {
        font-size: 46px;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #6366f1, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
    }

    p {
        text-align: center;
        font-size: 17px !important;
        color: #94a3b8 !important;
        margin-bottom: 1.2rem !important;
    }

    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, #334155, transparent);
        margin-bottom: 22px;
    }

    .stTextArea textarea {
        background: rgba(15, 23, 42, 0.75) !important;
        backdrop-filter: blur(16px);
        color: #e2e8f0 !important;
        border: 1px solid rgba(148, 163, 184, 0.15) !important;
        border-radius: 20px !important;
        padding: 18px !important;
        font-size: 15px !important;
        resize: vertical !important;
    }

    .stButton > button {
        width: 200px;
        height: 56px;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 auto;
        padding: 0 !important;
        background: linear-gradient(135deg, #6366f1, #a855f7);
        color: white;
        border-radius: 18px;
        border: none;
        font-weight: 700;
        font-size: 15px;
        letter-spacing: 0.4px;
        line-height: 1 !important;
        box-shadow: 0 12px 35px rgba(99,102,241,0.45);
    }

    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 18px 45px rgba(168,85,247,0.6);
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -------------------------
# Branding
# -------------------------
st.markdown(
    """
    <h1>AIClean</h1>
    <p>Remove Hidden AI Characters. Instantly.</p>
    <hr>
    """,
    unsafe_allow_html=True
)


# -------------------------
# Layout
# -------------------------
col1, col2 = st.columns(2)

with col1:
    input_text = st.text_area("Input Text", height=300)

with col2:
    st.text_area(
        "Output",
        value=st.session_state.cleaned_text,
        height=300,
        key="output_area",
        disabled=True
    )

col_left, col_center, col_right = st.columns([2, 1, 2])

with col_center:
    clean_clicked = st.button("Clean Text")

if clean_clicked:
    st.session_state.cleaned_text = clean_ai_text(input_text)
