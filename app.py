# import streamlit as st
# import re
# import unicodedata


# # ==================================================
# # WORDPRESS AI CONTENT CLEANER (Lean Production Version)
# # For: Software + Study Abroad Articles
# # ==================================================

# def clean_ai_text(text: str) -> str:
#     """
#     Clean AI-generated content for WordPress publishing.

#     ✔ Normalize Unicode
#     ✔ Remove invisible characters
#     ✔ Remove unsafe control characters
#     ✔ Normalize smart punctuation
#     ✔ Remove emojis
#     ✔ Normalize whitespace
#     ✔ Preserve multilingual characters
#     ✔ Preserve structure

#     No overengineering.
#     """

#     # --------------------------------------------------
#     # 1️⃣ Normalize Unicode (critical for consistency)
#     # --------------------------------------------------
#     text = unicodedata.normalize("NFKC", text)

#     # --------------------------------------------------
#     # 2️⃣ Standardize line endings
#     # --------------------------------------------------
#     text = text.replace("\r\n", "\n").replace("\r", "\n")

#     # --------------------------------------------------
#     # 3️⃣ Remove invisible / problematic Unicode
#     # --------------------------------------------------
#     cleaned_chars = []
#     for char in text:
#         category = unicodedata.category(char)

#         # Remove format, surrogate, private use, unassigned
#         if category in ("Cf", "Cs", "Co", "Cn"):
#             continue

#         # Remove control characters except newline & tab
#         if category == "Cc" and char not in ("\n", "\t"):
#             continue

#         cleaned_chars.append(char)

#     text = "".join(cleaned_chars)

#     # --------------------------------------------------
#     # 4️⃣ Normalize problematic whitespace
#     # --------------------------------------------------
#     text = text.replace("\u00A0", " ")  # non-breaking space
#     text = text.replace("\u2007", " ")
#     text = text.replace("\u202F", " ")

#     # --------------------------------------------------
#     # 5️⃣ Normalize smart punctuation
#     # Important for software articles & code clarity
#     # --------------------------------------------------
#     replacements = {
#         "“": '"',
#         "”": '"',
#         "‘": "'",
#         "’": "'",
#         "–": "-",
#         "—": "-",
#         "…": "...",
#     }

#     for k, v in replacements.items():
#         text = text.replace(k, v)

#     # --------------------------------------------------
#     # 6️⃣ Remove emojis (professional publishing)
#     # --------------------------------------------------
#     emoji_pattern = re.compile(
#         "["
#         "\U0001F600-\U0001F64F"
#         "\U0001F300-\U0001F5FF"
#         "\U0001F680-\U0001F6FF"
#         "\U0001F700-\U0001F77F"
#         "\U0001F780-\U0001F7FF"
#         "\U0001F800-\U0001F8FF"
#         "\U0001F900-\U0001F9FF"
#         "\U0001FA00-\U0001FAFF"
#         "\U00002700-\U000027BF"
#         "]+",
#         flags=re.UNICODE,
#     )

#     text = emoji_pattern.sub("", text)

#     # --------------------------------------------------
#     # 7️⃣ Clean excessive whitespace
#     # --------------------------------------------------
#     text = re.sub(r"[ \t]+", " ", text)
#     text = re.sub(r" +\n", "\n", text)
#     text = re.sub(r"\n{3,}", "\n\n", text)

#     return text.strip()


# # ==================================================
# # STREAMLIT APP
# # ==================================================

# st.set_page_config(
#     page_title="AIClean",
#     page_icon="✨",
#     layout="wide"
# )

# st.markdown(
#     """
#     <h1 style="text-align:center;">AIClean</h1>
#     <p style="text-align:center;">
#     AI Content Cleaner for Software & Study Abroad WordPress Publishing
#     </p>
#     <hr>
#     """,
#     unsafe_allow_html=True
# )


# # --------------------------------------------------
# # Session State
# # --------------------------------------------------

# if "cleaned_text" not in st.session_state:
#     st.session_state.cleaned_text = ""


# # --------------------------------------------------
# # Layout
# # --------------------------------------------------

# col1, col2 = st.columns(2)

# with col1:
#     input_text = st.text_area("Input Text", height=350)

# with col2:
#     st.text_area("Cleaned Output", value=st.session_state.cleaned_text, height=350)


# col_left, col_center, col_right = st.columns([2, 1, 2])

# with col_center:
#     clean_clicked = st.button("Clean Text", use_container_width=True)


# # --------------------------------------------------
# # Cleaning Action
# # --------------------------------------------------

# if clean_clicked:
#     st.session_state.cleaned_text = clean_ai_text(input_text)
#     st.rerun()






































import streamlit as st
import re
import unicodedata


# ==================================================
# CLEANING ENGINE (Lean Production Version)
# ==================================================

def clean_ai_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    cleaned_chars = []
    for char in text:
        category = unicodedata.category(char)

        if category in ("Cf", "Cs", "Co", "Cn"):
            continue

        if category == "Cc" and char not in ("\n", "\t"):
            continue

        cleaned_chars.append(char)

    text = "".join(cleaned_chars)

    text = text.replace("\u00A0", " ")
    text = text.replace("\u2007", " ")
    text = text.replace("\u202F", " ")

    replacements = {
        "“": '"', "”": '"',
        "‘": "'", "’": "'",
        "–": "-", "—": "-",
        "…": "...",
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

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

    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" +\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="ReadyPublish",
    page_icon="🚀",
    layout="wide"
)


# ==================================================
# PERFECTLY FITTING UI STYLING
# ==================================================

st.markdown("""
<style>

/* Remove default spacing */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 0rem !important;
    max-width: 1200px;
}

header, footer {visibility: hidden;}

/* Full height layout */
html, body, [data-testid="stAppViewContainer"] {
    height: 100%;
}

/* Background */
.stApp {
    background: radial-gradient(circle at 20% 20%, #1e293b 0%, #0f172a 50%, #020617 100%);
    color: #e2e8f0;
}

/* Hero */
.hero-title {
    font-size: 54px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #6366f1, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.2rem;
}

.hero-subtitle {
    text-align: center;
    font-size: 18px;
    color: #94a3b8;
    margin-bottom: 2rem;
}

/* Text Areas */
.stTextArea textarea {
    background: rgba(15, 23, 42, 0.7) !important;
    backdrop-filter: blur(16px);
    border: 1px solid rgba(148, 163, 184, 0.2) !important;
    border-radius: 16px !important;
    color: #e2e8f0 !important;
    padding: 16px !important;
    font-size: 15px !important;
    height: 380px !important;
}

/* Button */
.stButton > button {
    width: 220px;
    height: 55px;
    margin: 0 auto;
    display: block;
    background: linear-gradient(135deg, #6366f1, #a855f7);
    color: white;
    border-radius: 16px;
    border: none;
    font-weight: 700;
    font-size: 15px;
    box-shadow: 0 12px 30px rgba(99,102,241,0.5);
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 18px 40px rgba(168,85,247,0.6);
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# HERO SECTION
# ==================================================

st.markdown("""
<div class="hero-title">ReadyPublish</div>
<div class="hero-subtitle">
Make Every AI Draft Ready to Go Live.
</div>
""", unsafe_allow_html=True)


# ==================================================
# SESSION STATE
# ==================================================

if "cleaned_text" not in st.session_state:
    st.session_state.cleaned_text = ""


# ==================================================
# MAIN GRID (Perfect Alignment)
# ==================================================

col1, col2 = st.columns(2, gap="large")

with col1:
    input_text = st.text_area("Paste Your AI Draft")

with col2:
    st.text_area("Publish-Ready Output", value=st.session_state.cleaned_text)


# Center Button
st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)

clean_clicked = st.button("🚀 Clean & Make Ready")

if clean_clicked:
    st.session_state.cleaned_text = clean_ai_text(input_text)
    st.rerun()
