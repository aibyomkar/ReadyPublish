import streamlit as st
import re
import unicodedata


# ==================================================
# WORDPRESS AI CONTENT CLEANER (Lean Production Version)
# For: Software + Study Abroad Articles
# ==================================================

def clean_ai_text(text: str) -> str:
    """
    Clean AI-generated content for WordPress publishing.

    ✔ Normalize Unicode
    ✔ Remove invisible characters
    ✔ Remove unsafe control characters
    ✔ Normalize smart punctuation
    ✔ Remove emojis
    ✔ Normalize whitespace
    ✔ Preserve multilingual characters
    ✔ Preserve structure

    No overengineering.
    """

    # --------------------------------------------------
    # 1️⃣ Normalize Unicode (critical for consistency)
    # --------------------------------------------------
    text = unicodedata.normalize("NFKC", text)

    # --------------------------------------------------
    # 2️⃣ Standardize line endings
    # --------------------------------------------------
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # --------------------------------------------------
    # 3️⃣ Remove invisible / problematic Unicode
    # --------------------------------------------------
    cleaned_chars = []
    for char in text:
        category = unicodedata.category(char)

        # Remove format, surrogate, private use, unassigned
        if category in ("Cf", "Cs", "Co", "Cn"):
            continue

        # Remove control characters except newline & tab
        if category == "Cc" and char not in ("\n", "\t"):
            continue

        cleaned_chars.append(char)

    text = "".join(cleaned_chars)

    # --------------------------------------------------
    # 4️⃣ Normalize problematic whitespace
    # --------------------------------------------------
    text = text.replace("\u00A0", " ")  # non-breaking space
    text = text.replace("\u2007", " ")
    text = text.replace("\u202F", " ")

    # --------------------------------------------------
    # 5️⃣ Normalize smart punctuation
    # Important for software articles & code clarity
    # --------------------------------------------------
    replacements = {
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "–": "-",
        "—": "-",
        "…": "...",
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    # --------------------------------------------------
    # 6️⃣ Remove emojis (professional publishing)
    # --------------------------------------------------
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F700-\U0001F77F"
        "\U0001F780-\U0001F7FF"
        "\U0001F800-\U0001F8FF"
        "\U0001F900-\U0001F9FF"
        "\U0001FA00-\U0001FAFF"
        "\U00002700-\U000027BF"
        "]+",
        flags=re.UNICODE,
    )

    text = emoji_pattern.sub("", text)

    # --------------------------------------------------
    # 7️⃣ Clean excessive whitespace
    # --------------------------------------------------
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" +\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


# ==================================================
# STREAMLIT APP
# ==================================================

st.set_page_config(
    page_title="AIClean",
    page_icon="✨",
    layout="wide"
)

st.markdown(
    """
    <h1 style="text-align:center;">AIClean</h1>
    <p style="text-align:center;">
    AI Content Cleaner for Software & Study Abroad WordPress Publishing
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Session State
# --------------------------------------------------

if "cleaned_text" not in st.session_state:
    st.session_state.cleaned_text = ""


# --------------------------------------------------
# Layout
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    input_text = st.text_area("Input Text", height=350)

with col2:
    st.text_area("Cleaned Output", value=st.session_state.cleaned_text, height=350)


col_left, col_center, col_right = st.columns([2, 1, 2])

with col_center:
    clean_clicked = st.button("Clean Text", use_container_width=True)


# --------------------------------------------------
# Cleaning Action
# --------------------------------------------------

if clean_clicked:
    st.session_state.cleaned_text = clean_ai_text(input_text)
    st.rerun()