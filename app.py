import re
import unicodedata


# -------------------------
# WordPress-Optimized AI Cleaning Engine
# -------------------------
def clean_ai_text(text: str) -> str:
    """
    Production-grade AI content sanitizer for WordPress publishing.
    - Preserves multilingual UTF-8 characters
    - Removes invisible / malicious Unicode
    - Normalizes smart punctuation
    - Removes emojis
    - Converts NBSP to regular space
    - Preserves structure
    """

    # --------------------------------------------------
    # 1. Normalize Unicode (critical)
    # --------------------------------------------------
    text = unicodedata.normalize("NFKC", text)

    # --------------------------------------------------
    # 2. Standardize line endings
    # --------------------------------------------------
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # --------------------------------------------------
    # 3. Remove invisible and dangerous Unicode categories
    # --------------------------------------------------
    cleaned_chars = []
    for char in text:
        category = unicodedata.category(char)

        # Remove format, surrogate, private use, unassigned
        if category in ("Cf", "Cs", "Co", "Cn"):
            continue

        # Remove control characters except newline and tab
        if category == "Cc" and char not in ("\n", "\t"):
            continue

        cleaned_chars.append(char)

    text = "".join(cleaned_chars)

    # --------------------------------------------------
    # 4. Replace problematic whitespace
    # --------------------------------------------------
    text = text.replace("\u00A0", " ")  # Non-breaking space → normal space
    text = text.replace("\u2007", " ")
    text = text.replace("\u202F", " ")

    # --------------------------------------------------
    # 5. Normalize smart punctuation to web-safe equivalents
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
    # 6. Remove emojis (safe for blog body text)
    # --------------------------------------------------
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport
        "\U0001F700-\U0001F77F"
        "\U0001F780-\U0001F7FF"
        "\U0001F800-\U0001F8FF"
        "\U0001F900-\U0001F9FF"
        "\U0001FA00-\U0001FAFF"
        "\U00002700-\U000027BF"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE,
    )
    text = emoji_pattern.sub("", text)

    # --------------------------------------------------
    # 7. Clean excessive whitespace
    # --------------------------------------------------
    text = re.sub(r"[ \t]+", " ", text)        # Collapse multiple spaces
    text = re.sub(r" +\n", "\n", text)         # Remove trailing spaces
    text = re.sub(r"\n{3,}", "\n\n", text)     # Limit excessive blank lines

    # --------------------------------------------------
    # 8. Final trim
    # --------------------------------------------------
    return text.strip()

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="AIClean",
    page_icon="✨",   # You can use emoji
    layout="wide"
)

# -------------------------
# TRUE AI SaaS UI (Tight Hero Layout)
# -------------------------
st.markdown(
    """
    <style>

    /* ===== Remove ALL Default Spacing ===== */
    .block-container {
        padding-top: 0.8rem !important;
        padding-bottom: 0rem !important;
        margin-top: 0rem !important;
        max-width: 1200px;
    }

    header, footer {
        visibility: hidden;
    }

    html, body {
        overflow-x: hidden;
        height: 100vh;
    }

    /* ===== Background ===== */
    .stApp {
        background: radial-gradient(circle at 15% 20%, #1e293b 0%, #0f172a 45%, #020617 100%);
        color: #e2e8f0;
    }

    /* Soft glow accents */
    .stApp:before {
        content: "";
        position: fixed;
        top: -150px;
        left: -150px;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(99,102,241,0.25) 0%, transparent 70%);
        filter: blur(100px);
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
        filter: blur(100px);
        z-index: 0;
    }

    /* ===== Hero Title ===== */
    h1 {
        font-size: 46px;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #6366f1, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
        margin-top: 0rem;
    }

    /* Subtitle */
    p {
        text-align: center;
        font-size: 17px !important;
        color: #94a3b8 !important;
        margin-bottom: 1.2rem !important;
    }

    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, #334155, transparent);
        margin-top: 8px;
        margin-bottom: 22px;
    }

    /* ===== Text Areas (Glass SaaS Card) ===== */
    .stTextArea textarea {
        background: rgba(15, 23, 42, 0.75) !important;
        backdrop-filter: blur(16px);
        color: #e2e8f0 !important;
        border: 1px solid rgba(148, 163, 184, 0.15) !important;
        border-radius: 20px !important;
        padding: 18px !important;
        font-size: 15px !important;
        transition: all 0.3s ease;
    }

    .stTextArea textarea:focus {
        border: 1px solid #6366f1 !important;
        box-shadow: 0 0 30px rgba(99,102,241,0.5);
    }

    label {
        color: #cbd5e1 !important;
        font-weight: 600;
        letter-spacing: 0.4px;
    }

    /* ===== Premium SaaS Button ===== */

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
    line-height: 1 !important;          /* 🔥 Critical fix */

    box-shadow: 0 12px 35px rgba(99,102,241,0.45);
    transition: all 0.3s ease;
    }

    /* Force inner text container to center */
    .stButton > button > div {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100%;
    }

    /* Remove any default text spacing */
    .stButton > button p {
        margin: 0 !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 18px 45px rgba(168,85,247,0.6);
    }

    .stButton > button:active {
        transform: scale(0.98);
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
# Session State
# -------------------------
if "cleaned_text" not in st.session_state:
    st.session_state.cleaned_text = ""


# -------------------------
# Layout (UNCHANGED)
# -------------------------
col1, col2 = st.columns(2)

with col1:
    input_text = st.text_area("Input Text", height=300)

with col2:
    st.text_area("Output", value=st.session_state.cleaned_text, height=300)

col_left, col_center, col_right = st.columns([2, 1, 2])

with col_center:
    clean_clicked = st.button("Clean Text", use_container_width=True)

if clean_clicked:
    st.session_state.cleaned_text = clean_ai_text(input_text)
    st.rerun()
