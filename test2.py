import streamlit as st
import PyPDF2
import os
import subprocess

st.title("PDF Chatbot")

# Use subprocess to install the 'openai' package
subprocess.run(["pip", "install", "openai"])

# Verify if the 'openai' package is installed and import it
try:
    import openai

    # Retrieve OpenAI API key from Streamlit secrets
    api_key = st.secrets["openai_api_key"]
    openai.api_key = api_key
except ImportError:
    st.error("The 'openai' package couldn't be imported. Please check your environment and dependencies.")

# Function to extract text from a PDF file using PyPDF2
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to interact with the chatbot
def chat_with_bot():
    pdf_text = None
    user_input = st.text_input("You: ")
    if user_input:
        if pdf_text is not None:
            # Start the conversation with "You: <User Input>" to make it clear
            # that the user is initiating the conversation.
            conversation = f"You: {user_input}\nPDF Text: {pdf_text}\nYou:"
            
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=conversation,
                max_tokens=100,  # Increase the max tokens for longer responses
            )
            bot_response = response.choices[0].text.strip()
            st.write("PDF Chatbot:", bot_response)


# Upload PDF file
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if pdf_file:
    st.write(f"Reading PDF file: {pdf_file.name}")
    pdf_text = extract_text_from_pdf(pdf_file)
    st.write(f"Extracted Text:\n{pdf_text}")

st.markdown("---")
st.write("Start a conversation with the PDF Chatbot:")
chat_with_bot()
