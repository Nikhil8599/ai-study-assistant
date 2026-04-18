# AI Study Assistant

<img width="1919" height="907" alt="image" src="https://github.com/user-attachments/assets/f93d9d7d-c943-4e9c-8882-122acd40056a" />


An AI-powered assistant that answers engineering questions using RAG.

## Live Demo

https://ai-study-assistant-ir4bpufc2nsylyrshsmxve.streamlit.app/#ai-study-assistant

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

## Tech Stack

- Python
- LangGraph
- ChromaDB
- Sentence Transformers
- Groq LLM
- Streamlit

## Deployment

The application is deployed using **Streamlit Cloud**.

- Platform: Streamlit Cloud  
- Secrets Management: Streamlit Secrets  
- Environment: Python  

To run locally:

1. Install dependencies:
   pip install -r requirements.txt

2. Add API key in .env:
   GROQ_API_KEY=your_key

3. Run:
   streamlit run capstone_streamlit.py



