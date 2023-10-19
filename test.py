import streamlit as st
from PyPDF2 import PdfFileReader
import os

# Create a Streamlit app
st.title("Quality Checker")
st.write("This application will allow you to upload your dataset and run a quality check on it.")
st.markdown("---")

# Function to process PDFs
def process_pdf(pdf_file):
    pdf_reader = PdfFileReader(pdf_file)
    total_pages = pdf_reader.getNumPages()
    st.write(f"Total Pages: {total_pages}")
    for page_num in range(total_pages):
        page = pdf_reader.getPage(page_num)
        page_text = page.extractText()
        st.subheader(f"Page {page_num + 1}")
        st.write(page_text)

# Upload PDF files
pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)

if st.button("Process"):
    if pdf_docs:
        with st.spinner("Processing"):
            for pdf_file in pdf_docs:
                process_pdf(pdf_file)

# Note: You don't need the package installation part in this code, as it's not directly related to the PDF processing.
