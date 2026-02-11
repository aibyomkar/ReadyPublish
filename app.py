import streamlit as st
import re
import unicodedata


# ==================================================
# HOMOGLYPH MAP (Common Cyrillic & Greek lookalikes)
# ==================================================

HOMOGLYPH_MAP = {
    # Cyrillic → Latin
    "а": "a", "е": "e", "о": "o", "р": "p",
    "с": "c", "у": "y", "х": "x", "і": "i", "ӏ": "l",

    # Greek → Latin
    "Α": "A", "Β": "B", "Ε": "E", "Ζ": "Z",
    "Η": "H", "Ι": "I", "Κ": "K", "Μ": "M",
    "Ν": "N", "Ο": "O", "Ρ": "P", "Τ": "T",
    "Υ": "Y", "Χ": "X",
    "α": "a", "β": "b", "γ": "y",
    "ι": "i", "ο": "o", "ρ": "p",
    "τ": "t", "χ": "x",
}


# ==================================================
# AUTO-CORRECT HOMOGLYPHS
# ==================================================

def correct_homoglyphs(text):
    corrected = []
    replaced_chars = []

    for char in text:
        if char in HOMOGLYPH_MAP:
            corrected.append(HOMOGLYPH_MAP[char])
            replaced_chars.append(char)
        else:
            corrected.append(char)

    return "".join(corrected), replaced_chars


# ==================================================
# DETECT MIXED SCRIPT WORDS
# ==================================================

def detect_mixed_scripts(text):
    suspicious_words = []
    words = re.findall(r"\b\w+\b", text)

    for word in words:
        has_latin = False
        has_other = False

        for char in word:
            name = unicodedata.name(char, "")
            if "LATIN" in name:
                has_latin = True
            elif "CYRILLIC" in name or "GREEK" in name:
                has_other = True

        if has_latin and has_other:
            suspicious_words.append(word)

    return suspicious_words


# ==================================================
# WORDPRESS-OPTIMIZED AI CLEANING ENGINE
# ==================================================

def clean_ai_text(text: str):

    # 1️⃣ Normalize Unicode
    text = unicodedata.normalize("NFKC", text)

    # 2️⃣ Standardize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # 3️⃣ Remove invisible / dangerous Unicode
    cleaned_chars = []
    for char in text:
        category = unicodedata.category(char)

        if category in ("Cf", "Cs", "Co", "Cn"):
            continue

        if category == "Cc" and char not in ("\n", "\t"):
            continue

        cleaned_chars.append(char)

    text = "".join(cleaned_chars)

    # 4️⃣ Normalize problematic whitespace
    text = text.replace("\u00A0", " ")
    text = text.replace("\u2007", " ")
    text = text.replace("\u202F", " ")

    # 5️⃣ Normalize smart punctuation
    smart_replacements = {
        "“": '"', "”": '"',
        "‘": "'", "’": "'",
        "–": "-", "—": "-",
        "…": "...",
    }

    for k, v in smart_replacements.items():
        text = text.replace(k, v)

    # 6️⃣ Remove emojis
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

    # 7️⃣ Auto-correct homoglyphs
    text, replaced_chars = correct_homoglyphs(text)

    # 8️⃣ Detect mixed-script risks
    suspicious_words = detect_mixed_scripts(text)

    # 9️⃣ Clean excessive whitespace
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" +\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    text = text.strip()

    return text, suspicious_words, replaced_chars


# ==================================================
# STREAMLIT APP CONFIG
# ==================================================

st.set_page_config(
    page_title="AIClean",
    page_icon="✨",
    layout="wide"
)

st.markdown(
    """
    <h1 style="text-align:center;">AIClean</h1>
    <p style="text-align:center;">WordPress AI Content Sanitizer (Security Hardened)</p>
    <hr>
    """,
    unsafe_allow_html=True
)


# ==================================================
# SESSION STATE
# ==================================================

if "cleaned_text" not in st.session_state:
    st.session_state.cleaned_text = ""

if "suspicious_words" not in st.session_state:
    st.session_state.suspicious_words = []

if "replaced_chars" not in st.session_state:
    st.session_state.replaced_chars = []


# ==================================================
# LAYOUT
# ==================================================

col1, col2 = st.columns(2)

with col1:
    input_text = st.text_area("Input Text", height=350)

with col2:
    st.text_area("Cleaned Output", value=st.session_state.cleaned_text, height=350)


col_left, col_center, col_right = st.columns([2, 1, 2])

with col_center:
    clean_clicked = st.button("Clean Text", use_container_width=True)


# ==================================================
# CLEANING ACTION
# ==================================================

if clean_clicked:
    cleaned, suspicious, replaced = clean_ai_text(input_text)
    st.session_state.cleaned_text = cleaned
    st.session_state.suspicious_words = suspicious
    st.session_state.replaced_chars = replaced
    st.rerun()


# ==================================================
# SECURITY REPORTING
# ==================================================

if st.session_state.replaced_chars:
    st.info(f"Auto-corrected homoglyph characters: {set(st.session_state.replaced_chars)}")

if st.session_state.suspicious_words:
    st.warning("Mixed-script words detected:")
    st.write(st.session_state.suspicious_words)
