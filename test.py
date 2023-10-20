import streamlit as st
import subprocess
import os

# Upgrade PyMuPDF to the latest version
subprocess.call(["pip", "install", "PyMuPDF", "--upgrade", "-q"])

# Check if PyMuPDF was successfully installed
try:
    import fitz
except ImportError:
    st.error("PyMuPDF (fitz) failed to install. Please check your installation or contact the system administrator.")

# Continue with the Streamlit app
st.title("Quality Checker")
st.write("This application will allow you to upload your dataset and run a quality check on it.")
st.markdown("---")

# Function to process PDFs
def process_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    total_pages = doc.page_count
    st.write(f"Total Pages: {total_pages}")
    
    for page_num in range(total_pages):
        page = doc.load_page(page_num)
        page_text = page.get_text()
        
        # Process the page_text as needed
        # Split the page_text into chunks or perform other text processing here
        
        st.subheader(f"Page {page_num + 1}")
        st.write(page_text)
        
# Upload PDF files
pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)

if st.button("Process"):
    if pdf_docs:
        with st.spinner("Processing"):
            for pdf_file in pdf_docs:
                process_pdf(pdf_file)
