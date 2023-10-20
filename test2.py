import streamlit as st
import PyPDF2
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

st.title("PDF Chatbot")

# Initialize a ChatterBot instance
chatbot = ChatBot("PDFBot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language
trainer.train("chatterbot.corpus.english")

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to interact with the chatbot
def chat_with_bot():
    user_input = st.text_input("You: ")
    if user_input:
        response = chatbot.get_response(user_input)
        st.write("PDFBot:", response)

# Upload PDF file
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if pdf_file:
    st.write(f"Reading PDF file: {pdf_file.name}")
    pdf_text = extract_text_from_pdf(pdf_file)
    st.write(f"Extracted Text:\n{pdf_text}")

st.markdown("---")
st.write("Start a conversation with the PDFBot:")
chat_with_bot()
