import streamlit as st
from translator import translate_text
from utils import get_language_list

st.set_page_config(
    page_title="TransLingua Pro",
    page_icon="🌍",
    layout="wide"
)

# Title
st.title("🌍 TransLingua Pro")
st.write("AI Powered Multi-Language Translator (Gemini 2.5)")

# Load languages
languages = get_language_list()

# Language selection
col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox("Source Language", languages)

with col2:
    target_language = st.selectbox("Target Language", languages)

# Text input
text = st.text_area("Enter text to translate", height=200)

# Initialize history
if "history" not in st.session_state:
    st.session_state.history = []

# Translate Button
if st.button("🚀 Translate"):

    if not text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Translating..."):
            result = translate_text(text, source_language, target_language)

        if result.startswith("Error"):
            st.error(result)
        else:
            st.success("Translation Completed ✅")

            st.subheader("Translated Text")
            st.write(result)

            # Save history
            st.session_state.history.append({
                "input": text,
                "output": result
            })

            # Download option
            st.download_button(
                label="📥 Download Translation",
                data=result,
                file_name="translation.txt"
            )

# Show History
if st.session_state.history:
    st.subheader("📜 Translation History")

    for item in reversed(st.session_state.history):
        st.write("Input:", item["input"])
        st.write("Output:", item["output"])
        st.write("---")
