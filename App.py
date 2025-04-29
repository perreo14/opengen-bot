from transformers import pipeline
import gradio as gr

# Crear el modelo
chatbot = pipeline("text-generation", model="gpt2")

# Función para responder
def responder(texto):
    respuesta = chatbot(texto, max_length=50, num_return_sequences=1)
    return respuesta[0]['generated_text']

# Interfaz con Gradio
iface = gr.Interface(fn=responder,
                     inputs="text",
                     outputs="text",
                     title="Chatbot IA con GPT-2",
                     description="Escribe una pregunta y recibe una respuesta generada por IA.")

iface.launch()
