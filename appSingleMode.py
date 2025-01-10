import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("KEY_HUGGING_FACE")
API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"

HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def ask_question(question, context):
    payload = {
        "inputs": {
            "question": question,
            "context": context
        }
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response_data = response.json()
    
    # Handle errors
    if response.status_code != 200:
        st.error(f"API Error {response.status_code}: {response_data.get('error', 'Unknown error')}")
        return "Error occurred. Please try again."
    
    # Extract answer
    return response_data.get("answer", "No answer found.")

st.title("Question Answering with Hugging Face")

question = st.text_input("Enter your question:")
context = st.text_area("Enter the context:")

if question and context:
    with st.spinner("Processing..."):
        answer = ask_question(question, context)
        st.write("Answer:")
        st.write(answer)
