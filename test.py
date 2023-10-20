import streamlit as st
import PyPDF2
from langchain.text_splitter import CharacterTextSplitter
import os

st.title("Quality Checker")
st.write("This application will allow you to upload your dataset and run a quality check on it.")
st.markdown("---")

# Initialize the CharacterTextSplitter
document_splitter = CharacterTextSplitter(separator='\n', chunk_size=500, chunk_overlap=100)

# Function to process PDFs
def process_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    total_pages = len(pdf_reader.pages)
    st.write(f"Total Pages: {total_pages}")
    
    for page_num, page in enumerate(pdf_reader.pages, 1):
        page_text = page.extract_text()
        
        # Split the page text into chunks using the CharacterTextSplitter
        document_chunks = document_splitter.split_documents([page_text])
        
        for chunk_num, chunk in enumerate(document_chunks, 1):
            st.subheader(f"Page {page_num}, Chunk {chunk_num}")
            st.write(chunk)
        
# Upload PDF files
pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)

if st.button("Process"):
    if pdf_docs:
        with st.spinner("Processing"):
            for pdf_file in pdf_docs:
                process_pdf(pdf_file)
