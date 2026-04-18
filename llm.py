from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
import streamlit as st
load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=st.secrets["GROQ_API_KEY"]
)
