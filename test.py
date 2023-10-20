import streamlit as st
from PyPDF2 import PdfFileReader
from langchain.text_splitter import CharacterTextSplitter
import subprocess
import os

# Access the OpenAI API key from the environment variable
openai_api_key = os.environ.get("OPENAI_API_KEY")

st.title("Quality Checker")
st.write("This application allows you to upload and process PDF documents.")
st.markdown("---")

# Check if the API key is available
if openai_api_key:
    st.write(f"OpenAI API Key: {openai_api_key}")
    st.info("API key is available and can be used for OpenAI requests.")
else:
    st.warning("OpenAI API Key not found. Please set it as a GitHub secret.")

    # File Upload
    uploaded_files = st.file_uploader("Upload PDF Files", type=["pdf"], accept_multiple_files=True)

    # You can continue building your Streamlit application here
