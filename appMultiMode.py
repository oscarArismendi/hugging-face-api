import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Clave de la API de Hugging Face
API_KEY = os.getenv("KEY_HUGGING_FACE")
if not API_KEY:
    st.error("Could not find the API. lookup for correct .env configuration .")
    st.stop()

# Encabezados para las solicitudes
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

class MultiModelHandler:
    def __init__(self):
        # URLs de los modelos
        self.models = {
            "qa": "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2",
            "text-generation": "https://api-inference.huggingface.co/models/gpt2"
        }
        self.active_model = "qa"

    def set_model(self, model_name):
        if model_name in self.models:
            self.active_model = model_name
        else:
            raise ValueError(f"Model '{model_name}' not available.")

    def execute(self, payload):
        # Realizar la solicitud a la API
        response = requests.post(self.models[self.active_model], headers=HEADERS, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error {response.status_code}: {response.text}")
            return None

# Crear la interfaz de Streamlit
st.title("Multi-Model Application with Hugging Face")
st.sidebar.title("Select the model")

# Instanciar el manejador de modelos
handler = MultiModelHandler()

# Selección del modelo
model_option = st.sidebar.radio("Select one", ["qa", "text-generation"])

# Cambiar el modelo activo
handler.set_model(model_option)

if model_option == "qa":
    st.header("Model of QA")
    question = st.text_input("Write your question:")
    context = st.text_area("Give context:")
    if st.button("Obtain your answer"):
        if question and context:
            payload = {"inputs": {"question": question, "context": context}}
            with st.spinner("Procesing..."):
                result = handler.execute(payload)
                if result:
                    st.write("Answer:")
                    st.write(result.get("answer", "Could not find an answer."))
        else:
            st.error("Please, give both question and answer.")

elif model_option == "text-generation":
    st.header("Generating text model")
    prompt = st.text_area("Write the initial text to generate:")
    max_length = st.slider("Maximum lenght of the generated text", 10, 100, 50)
    num_return_sequences = st.slider("How many text do you want to create?", 1, 5, 1)
    if st.button("Generate text"):
        if prompt:
            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_length": max_length,
                    "num_return_sequences": num_return_sequences
                }
            }
            with st.spinner("Processing..."):
                result = handler.execute(payload)
                if result:
                    st.write("Generated text:")
                    for i, text in enumerate(result, 1):
                        st.write(f"**Genereccion {i}:**")
                        st.write(text.get("generated_text", ""))
        else:
            st.error("Please, select a text to generated.")