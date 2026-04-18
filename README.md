# AI Study Assistant

<img width="1919" height="905" alt="Screenshot 2026-04-18 102740" src="https://github.com/user-attachments/assets/12ef5b8e-dda7-4010-b380-28b9fbd262ee" />

An AI-powered assistant that answers engineering questions using RAG.

## Features

- Knowledge-based answers
- Retrieval-Augmented Generation (RAG)
- Memory (thread_id)
- LLM (Groq)
- ChromaDB
- Streamlit UI
- Tool support

## Architecture

User Query → Embedding → ChromaDB → Retrieval → LLM → Response



## Run

pip install -r requirements.txt

streamlit run capstone_streamlit.py

