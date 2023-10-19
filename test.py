import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
import sentence_transformers  
import sentence_transformers
import subprocess
import os

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# Upgrade PyPDF2 to the latest version
subprocess.call(["pip", "install", "PyPDF2", "--upgrade", "-q"])

# Install sentence-transformers package
subprocess.call(["pip", "install", "sentence-transformers", "-q"])


# Create a Streamlit app
st.title("Quality Checker")
st.write("This application will allow you to upload your dataset and run a quality check on it.")
st.markdown("---")

# Load a sentence-transformers model
embedder = sentence_transformers.SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Function to process PDFs
def process_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    total_pages = len(pdf_reader.pages)
    st.write(f"Total Pages: {total_pages}")
    
    # Initialize the CharacterTextSplitter
    document_splitter = CharacterTextSplitter(separator='\n', chunk_size=500, chunk_overlap=100)
    
    for page_num, page in enumerate(pdf_reader.pages, 1):
        page_text = page.extract_text()
        
        # Split the page text into chunks
        document_chunks = document_splitter.split_documents([page_text])
        
        # Display each chunk separately
        for chunk_num, chunk in enumerate(document_chunks, 1):
            st.subheader(f"Page {page_num}, Chunk {chunk_num}")
            st.write(chunk)
            
            # Generate embeddings for the chunk
            chunk_embeddings = embedder.encode([chunk], convert_to_tensor=True)
            st.write("Embeddings:")
            st.write(chunk_embeddings)

# Upload PDF files
pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)

if st.button("Process"):
    if pdf_docs:
        with st.spinner("Processing"):
            for pdf_file in pdf_docs:
                process_pdf(pdf_file)
