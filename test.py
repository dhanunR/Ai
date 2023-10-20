#import streamlit as st
#from PyPDF2 import PdfReader
#from langchain.text_splitter import CharacterTextSplitter
#from transformers import AutoTokenizer, AutoModel  
#import AutoTokenizer from transformers
#import subprocess
#import os

# List of packages to install
packages_to_install = [
    "langchain",
    "bitsandbytes",
    "accelerate",
    "xformers",
    "einops",
    "datasets",
    "loralib",
    "sentencepiece",
    "pypdf",
    "sentence_transformers",
    "chromadb",
    "openai",
    "tiktoken",
    "PyPDF2",
    # Add more package names here

     # Import statements for additional modules
    "import torch",
    "import streamlit as st",
    "from PyPDF2 import PdfReader",
    "import transformers",
    "from transformers import AutoTokenizer, AutoModelForCausalLM",
    "from transformers import pipeline",
    "from transformers import AutoTokenizer, AutoModel",
    "from langchain import HuggingFacePipeline",
    "from langchain.chains import ConversationalRetrievalChain",
    "from langchain.text_splitter import CharacterTextSplitter",
    "from langchain.memory import ConversationBufferMemory",
    "from langchain.embeddings.openai import OpenAIEmbeddings",
    "from langchain.chat_models import ChatOpenAI",
    "import subprocess",
    "import os",
    "import sys",
    # Add more import statements here
]

# Function to install a package
def install_package(package_name):
    try:
        subprocess.check_call(["pip", "install", package_name, "-q"])
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")

# Install packages one by one
for package in packages_to_install:
    if not package.startswith("from ") and not package.startswith("import "):  # Skip import statements
        install_package(package)
        
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
