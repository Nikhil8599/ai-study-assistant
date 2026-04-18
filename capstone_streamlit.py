import streamlit as st
import uuid
from agent import ask
st.set_page_config(page_title="AI Study Assistant", layout="centered")

st.title("AI Study Assistant")

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.chat_message("user").write(chat["content"])
    else:
        st.chat_message("assistant").write(chat["content"])

user_input = st.chat_input("Ask your question...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })

    response = ask(user_input, st.session_state.thread_id)
    st.chat_message("assistant").write(response)
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": response
    })
st.sidebar.title("About")
st.sidebar.info("""
AI Study Assistant built using:
- LangGraph (Agent flow)
- ChromaDB (Vector DB)
- Groq LLM
- Streamlit UI

Features:
- Answers from knowledge base
- Memory (thread_id)
- Tool support (date/time)
- No hallucination
""")

if st.sidebar.button("New Conversation"):
    st.session_state.thread_id = str(uuid.uuid4())
    st.session_state.chat_history = []
    st.rerun()