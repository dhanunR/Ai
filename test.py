import streamlit as st
from PyPDF2 import PdfFileReader, PdfFileReader
from langchain.text_splitter import CharacterTextSplitter
from transformers import AutoTokenizer, AutoModel
import subprocess
import os

# Install necessary packages
required_packages = [
    "langchain",
    "bitsandbytes",
    "accelerate",
    "xformers",
    "einops",
    "datasets",
    "loralib",
    "sentencepiece",
    "pypdf2",
    "chromadb",
    "openai",
    "tiktoken",
    "sentence_transformers",
]
for package in required_packages:
    subprocess.check_call(["pip", "install", package, "-q"])

# Install or upgrade specific packages
subprocess.check_call(["pip", "install", "transformers", "--upgrade", "-q"])
subprocess.check_call(["pip", "install", "PyPDF2", "--upgrade", "-q"])

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# Streamlit app setup
st.title("Quality Checker")
st.write("This application allows you to upload and process PDF documents.")
st.markdown("---")

# Load pre-trained model and tokenizer
model_name = 'sentence-transformers/all-MiniLM-L6-v2'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Function to process PDFs
def process_pdf(pdf_file):
    pdf_reader = PdfFileReader(pdf_file)
    total_pages = pdf_reader.getNumPages()
    st.write(f"Total Pages: {total_pages}")
    
    # Initialize the CharacterTextSplitter
    document_splitter = CharacterTextSplitter(separator='\n', chunk_size=500, chunk_overlap=100)
    
    for page_num in range(total_pages):
        page = pdf_reader.getPage(page_num)
        page_text = page.extract_text()
        
        # Split the page text into chunks
        document_chunks = document_splitter.split_documents([page_text])
        
        # Display each chunk separately
        for chunk_num, chunk in enumerate(document_chunks, 1):
            st.subheader(f"Page {page_num + 1}, Chunk {chunk_num}")
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
