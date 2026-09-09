import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌐"
)

st.title("🌐 Language Translation Tool")
st.write("Translate text between different languages using an online translation service.")

languages = {
    "English": "en",
    "Kannada": "kn",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja"
}

col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_language = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

text = st.text_area(
    "Enter text to translate:",
    height=150,
    placeholder="Type your text here..."
)

if st.button("🔄 Translate", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some text first.")

    elif source_language == target_language:
        st.info("Source and target languages are the same.")
        st.text_area(
            "Translated Text",
            value=text,
            height=150
        )

    else:
        try:
            translated_text = GoogleTranslator(
                source=languages[source_language],
                target=languages[target_language]
            ).translate(text)

            st.success("Translation completed!")

            st.text_area(
                "Translated Text",
                value=translated_text,
                height=150
            )

        except Exception as e:
            st.error("Translation failed. Please check your internet connection and try again.")