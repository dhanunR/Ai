import openai
import streamlit as st
import os
import subprocess
import PyPDF2

# Check if a requirements.txt file exists
if not os.path.exists('requirements.txt'):
    st.error("The requirements.txt file is missing. Please make sure it's in the same directory as your app.")
else:
    # Use subprocess to install the required packages from requirements.txt
    try:
        st.write("Installing required packages...")
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        st.success("Required packages installed successfully.")
    except subprocess.CalledProcessError:
        st.error("Failed to install required packages. Please check your environment and dependencies.")

# Continue with the rest of your Streamlit app code

st.title("PDF Chatbot")

# Retrieve OpenAI API key from Streamlit secrets
api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = api_key

# Function to extract text from a PDF file using PyPDF2
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()
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
            
            # Debugging: Print the conversation
            st.write("Conversation:", conversation)
            
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=conversation,
                max_tokens=100,  # Increase the max tokens for longer responses
            )
            bot_response = response.choices[0].text.strip()
            
            # Debugging: Print the bot's response
            st.write("Bot Response:", bot_response)
            
            st.write("PDF Chatbot:", bot_response)

# Upload PDF file
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if pdf_file:
    st.write(f"Reading PDF file: {pdf_file.name}")
    pdf_text = extract_text_from_pdf(pdf_file)
    
    # Debugging: Print the extracted text
    st.write(f"Extracted Text:\n{pdf_text}")
    
st.markdown("---")
st.write("Start a conversation with the PDF Chatbot:")
chat_with_bot()
