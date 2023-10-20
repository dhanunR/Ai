import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from transformers import AutoTokenizer, AutoModel  
#import AutoTokenizer from transformers
import subprocess
import os

# Install the transformers library
subprocess.call(["pip", "install", "transformers", "-q"])

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# Upgrade PyPDF2 to the latest version
subprocess.call(["pip", "install", "PyPDF2", "--upgrade", "-q"])

# Create a Streamlit app
st.title("Quality Checker")
st.write("This application will allow you to upload your dataset and run a quality check on it.")
st.markdown("---")

# Load a pre-trained model and tokenizer from Hugging Face
model_name = 'sentence-transformers/all-MiniLM-L6-v2'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

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
            
            # Tokenize and generate embeddings for the chunk
            inputs = tokenizer(chunk, return_tensors="pt", padding=True, truncation=True)
            with st.spinner("Generating Embeddings"):
                outputs = model(**inputs)
            chunk_embeddings = outputs.last_hidden_state.mean(dim=1).squeeze()
            st.write("Embeddings:")
            st.write(chunk_embeddings)

# Upload PDF files
pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)

if st.button("Process"):
    if pdf_docs:
        with st.spinner("Processing"):
            for pdf_file in pdf_docs:
                process_pdf(pdf_file)
