import streamlit as st
import streamlit.components.v1 as components
import subprocess

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
    # Add more package names here

    # Import statements for additional modules
    "import torch",
    "import transformers",
    "from transformers import AutoTokenizer, AutoModelForCausalLM",
    "from transformers import pipeline",
    "from langchain import HuggingFacePipeline",
    "from langchain.chains import ConversationalRetrievalChain",
    "from langchain.memory import ConversationBufferMemory",
    "from langchain.embeddings.openai import OpenAIEmbeddings",
    "from langchain.chat_models import ChatOpenAI",
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

st.title("Quality Checker")
st.write("This application will allow you to upload your dataset and run a quality check on it.")
st.markdown("---")
