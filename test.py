import streamlit as st
from PyPDF2 import PdfFileReader
from langchain.text_splitter import CharacterTextSplitter
import subprocess
import os

# Retrieve the OpenAI API key from the environment variable
api_key = os.environ.get("OPENAI_API_KEY")

# Check if the API key is available
if api_key is None:
    st.warning("API key not found. Please set the OPENAI_API_KEY environment variable.")
else:
    st.title("Quality Checker")
    st.write("This application allows you to upload and process PDF documents.")
    st.markdown("---")

    # File Upload
    uploaded_files = st.file_uploader("Upload PDF Files", type=["pdf"], accept_multiple_files=True)

    # You can continue building your Streamlit application here
