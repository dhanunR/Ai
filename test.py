import streamlit as st
import PyPDF2
import os

st.title("AI Model")
st.markdown("---")

# Function to split text into chunks
def split_text_into_chunks(text, chunk_size, chunk_overlap):
    chunks = []
    text_length = len(text)
    start = 0

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - chunk_overlap

    return chunks

# Function to process PDFs
def process_pdf(pdf_files, chunk_size=500, chunk_overlap=100):
    total_chunks = 0

    for pdf_file in pdf_files:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)
        st.write(f"Total Pages: {total_pages}")

        for page_num, page in enumerate(pdf_reader.pages, 1):
            page_text = page.extract_text()

            # Split the page text into chunks
            document_chunks = split_text_into_chunks(page_text, chunk_size, chunk_overlap)
            total_chunks += len(document_chunks)

            for chunk_num, chunk in enumerate(document_chunks, 1):
                st.subheader(f"Page {page_num}, Chunk {chunk_num}")
                st.write(chunk)

    st.write(f"Total Chunks: {total_chunks}")

# Upload PDF files
pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)

if st.button("Process"):
    if pdf_docs:
        with st.spinner("Processing"):
            process_pdf(pdf_docs)
