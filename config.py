import os
from dotenv import load_dotenv

load_dotenv()

try:
    import streamlit as st
except ImportError:
    st = None


def _get_secret(name):
    if st is not None:
        try:
            value = st.secrets.get(name)
            if value:
                return value
        except (FileNotFoundError, KeyError):
            pass
    return os.getenv(name)


GEMINI_API_KEY = _get_secret("GEMINI_API_KEY")
TAVILY_API_KEY = _get_secret("TAVILY_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment or Streamlit secrets")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY not found in environment or Streamlit secrets")