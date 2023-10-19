import streamlit as st
from PyPDF2 import PdfReader
import os

# Upgrade PyPDF2 to the latest version
pip install PyPDF2 --upgrade -q


# Create a Streamlit app
st.title("Quality Checker")
st.write("This application will allow you to upload your dataset and run a quality check on it.")
st.markdown("---")

# Function to process PDFs
def process_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    total_pages = len(pdf_reader.pages)
    st.write(f"Total Pages: {total_pages}")
    for page_num, page in enumerate(pdf_reader.pages, 1):
        page_text = page.extract_text()
        st.subheader(f"Page {page_num}")
        st.write(page_text)

# Upload PDF files
pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)

if st.button("Process"):
    if pdf_docs:
        with st.spinner("Processing"):
            for pdf_file in pdf_docs:
                process_pdf(pdf_file)
