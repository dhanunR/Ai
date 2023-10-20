import streamlit as st
from PyPDF2 import PdfFileReader
from langchain.text_splitter import CharacterTextSplitter
import subprocess
import os

# Retrieve the OpenAI API key from the environment variable
api_key = os.environ.get("OPENAI_API_KEY")

# Check if the API key is available
if api_key is None:
    st.warning("API key not found. Please set the OPENAI_API_KEY environment variable.")
else:
    st.title("Quality Checker")
    st.write("This application allows you to upload and process PDF documents.")
    st.markdown("---")

    # File Upload
    uploaded_files = st.file_uploader("Upload PDF Files", type=["pdf"], accept_multiple_files=True)

    if st.button("Process PDF"):
        if uploaded_files:
            for pdf_file in uploaded_files:
                with st.spinner(f"Processing {pdf_file.name}"):
                    # Your PDF processing code goes here
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

                    # For example, you can process the PDF using your OpenAI API key
                    # Make API requests using the `api_key` variable

                st.success(f"Processed: {pdf_file.name}")

    # You can continue building your Streamlit application here
