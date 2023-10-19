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

# Keep adding more package names and import statements to the list and run the script to install them
st.set_page_config("Chat with Multiple PDFs")
    st.header("Chat with Multiple PDF 💬")
    user_question = st.text_input("Ask a Question from the PDF Files")
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
    if user_question:
        user_input(user_question)
    with st.sidebar:
        st.title("Settings")
        st.subheader("Upload your Documents")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Process Button", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                st.session_state.conversation = get_conversational_chain(vector_store)
                st.success("Done")



if __name__ == "__main__":
    main()
