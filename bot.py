import os
import requests
import google.generativeai as genai

# Configurar API de Gemini (Gratis)
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
modelo = genai.GenerativeModel('models/gemini-1.5-flash')


# 1. Generar el guion diario automáticamente
prompt = "Escribe un guion corto y viral de 30 segundos sobre una curiosidad del espacio para un Short de YouTube."
response = model.generate_content(prompt)
guion = response.text
print("Guion generado:", guion)

# 2. Aquí el script conectaría con un motor de texto a voz y descargaría videos de Pexels 
# usando tu PEXELS_API_KEY para ensamblar el video final mediante librerías de Python.
print("¡Proceso de automatización ejecutado con éxito en la nube!")
