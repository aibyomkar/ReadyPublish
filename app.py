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
# WORDPRESS AI CONTENT CLEANER (Lean Production Version)
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
# STREAMLIT CONFIG
# ==================================================

st.set_page_config(
    page_title="ReadyPublish",
    page_icon="🚀",
    layout="wide"
)


# ==================================================
# PREMIUM AI SAAS UI STYLING
# ==================================================

st.markdown("""
<style>

.block-container {
    padding-top: 1.2rem !important;
    max-width: 1200px;
}

header, footer {visibility: hidden;}

.stApp {
    background: radial-gradient(circle at 20% 20%, #1e293b 0%, #0f172a 45%, #020617 100%);
    color: #e2e8f0;
}

/* Soft Glow Effects */
.stApp:before {
    content: "";
    position: fixed;
    top: -150px;
    left: -150px;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(99,102,241,0.25) 0%, transparent 70%);
    filter: blur(120px);
    z-index: 0;
}

.stApp:after {
    content: "";
    position: fixed;
    bottom: -150px;
    right: -150px;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(168,85,247,0.25) 0%, transparent 70%);
    filter: blur(120px);
    z-index: 0;
}

/* Hero Title */
.hero-title {
    font-size: 56px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #6366f1, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.4rem;
}

/* Tagline */
.hero-subtitle {
    text-align: center;
    font-size: 20px;
    color: #94a3b8;
    margin-bottom: 2rem;
}

/* Glass Card */
.stTextArea textarea {
    background: rgba(15, 23, 42, 0.7) !important;
    backdrop-filter: blur(18px);
    border: 1px solid rgba(148, 163, 184, 0.2) !important;
    border-radius: 18px !important;
    color: #e2e8f0 !important;
    padding: 18px !important;
    font-size: 15px !important;
    transition: 0.3s ease;
}

.stTextArea textarea:focus {
    border: 1px solid #6366f1 !important;
    box-shadow: 0 0 30px rgba(99,102,241,0.4);
}

/* Button */
.stButton > button {
    width: 240px;
    height: 60px;
    background: linear-gradient(135deg, #6366f1, #a855f7);
    color: white;
    border-radius: 18px;
    border: none;
    font-weight: 700;
    font-size: 16px;
    box-shadow: 0 15px 40px rgba(99,102,241,0.5);
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 45px rgba(168,85,247,0.6);
}

.stButton > button:active {
    transform: scale(0.97);
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
# MAIN LAYOUT
# ==================================================

col1, col2 = st.columns(2)

with col1:
    input_text = st.text_area("Paste Your AI Draft", height=380)

with col2:
    st.text_area("Publish-Ready Output", value=st.session_state.cleaned_text, height=380)


st.markdown("<br>", unsafe_allow_html=True)

col_left, col_center, col_right = st.columns([2,1,2])

with col_center:
    clean_clicked = st.button("🚀 Clean & Make Ready", use_container_width=True)


# ==================================================
# ACTION
# ==================================================

if clean_clicked:
    st.session_state.cleaned_text = clean_ai_text(input_text)
    st.rerun()
