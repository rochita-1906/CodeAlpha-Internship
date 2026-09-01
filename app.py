import streamlit as st
from chatbot import get_answer

st.set_page_config(
    page_title="CodeAlpha FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 CodeAlpha FAQ Chatbot")
st.write("Ask questions about the CodeAlpha internship.")

st.divider()

user_question = st.text_input(
    "💬 Type your question:",
    placeholder="Example: What are the AI tasks?"
)

if user_question:
    answer = get_answer(user_question)

    st.subheader("🤖 Answer")
    st.info(answer)

st.divider()

st.caption("AI Internship Project | CodeAlpha")