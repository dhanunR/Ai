import openai
import streamlit as st

# Retrieve OpenAI API key from Streamlit secrets
api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = api_key
response = openai.Completion.create(
    engine="davinci",
    prompt="Hello, this is a test.",
    max_tokens=20
)

generated_text = response.choices[0].text.strip()
st.write("Generated Text:")
st.write(generated_text)
