import streamlit as st
import requests
import json

# Cargar la API Key desde los secrets
TOGETHER_API_KEY = st.secrets["TOGETHER_API_KEY"]
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"

# Configuración de la app
st.set_page_config(page_title="Asistente de Tesis", layout="wide")
st.title("📘 Asistente de Tesis para Maestría")

# Entrada del usuario
st.sidebar.header("Información de la Tesis")
carrera = st.sidebar.text_input("Carrera o disciplina:")
titulo = st.sidebar.text_input("Título de la tesis:")

# Función para solicitar a la API de Together

def query_together(messages):
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct-Turbo",
        "messages": messages,
        "max_tokens": 2512,
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1,
        "stop": ["<|eot_id|>"]
    }
    response = requests.post(TOGETHER_API_URL, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Error en la generación de contenido."

# Opciones de herramientas en la barra lateral
tools = [
    "Generador de Pregunta de Investigación",
    "Marco Teórico Automatizado",
    "Generación de Hipótesis",
    "Revisión de Literatura",
    "Metodología Sugerida",
    "Análisis de Datos",
    "Formato de Citas APA",
    "Revisión Ortográfica y de Estilo",
    "Resumen Automático",
    "Generación de Conclusiones"
]

tool_selected = st.sidebar.selectbox("Selecciona una herramienta:", tools)

if carrera and titulo:
    if tool_selected == "Generador de Pregunta de Investigación":
        st.subheader("🎯 Pregunta de Investigación Sugerida")
        messages = [{"role": "system", "content": f"Genera una pregunta de investigación clara y concisa para una tesis de maestría en {carrera} titulada '{titulo}'."}]
        result = query_together(messages)
        st.write(result)
    
    elif tool_selected == "Marco Teórico Automatizado":
        st.subheader("📖 Marco Teórico Inicial")
        messages = [{"role": "system", "content": f"Escribe un breve marco teórico introductorio para una tesis en {carrera} titulada '{titulo}'."}]
        result = query_together(messages)
        st.write(result)
    
    elif tool_selected == "Generación de Hipótesis":
        st.subheader("🔎 Hipótesis de Investigación")
        messages = [{"role": "system", "content": f"Genera hipótesis plausibles para una tesis de maestría en {carrera} titulada '{titulo}'."}]
        result = query_together(messages)
        st.write(result)
    
    elif tool_selected == "Revisión de Literatura":
        st.subheader("📚 Resumen de Literatura")
        messages = [{"role": "system", "content": f"Escribe un resumen de literatura relevante para una tesis en {carrera} titulada '{titulo}'."}]
        result = query_together(messages)
        st.write(result)
    
    elif tool_selected == "Metodología Sugerida":
        st.subheader("🛠 Metodología Recomendada")
        messages = [{"role": "system", "content": f"Sugiere una metodología adecuada para una tesis de maestría en {carrera} titulada '{titulo}'."}]
        result = query_together(messages)
        st.write(result)
    
    elif tool_selected == "Análisis de Datos":
        st.subheader("📊 Estrategia de Análisis de Datos")
        messages = [{"role": "system", "content": f"Recomienda un análisis de datos apropiado para una tesis en {carrera} titulada '{titulo}'."}]
        result = query_together(messages)
        st.write(result)
    
    elif tool_selected == "Formato de Citas APA":
        st.subheader("📑 Formato de Citas en APA")
        messages = [{"role": "system", "content": f"Proporciona ejemplos de citas en formato APA para una tesis en {carrera} titulada '{titulo}'."}]
        result = query_together(messages)
        st.write(result)
    
    elif tool_selected == "Revisión Ortográfica y de Estilo":
        st.subheader("📝 Revisión Ortográfica y de Estilo")
        texto = st.text_area("Introduce tu texto para revisión:")
        if st.button("Revisar Texto"):
            messages = [{"role": "system", "content": f"Revisa el siguiente texto, corrigiendo errores ortográficos y mejorando el estilo: {texto}"}]
            result = query_together(messages)
            st.write(result)
    
    elif tool_selected == "Resumen Automático":
        st.subheader("📄 Resumen de la Tesis")
        messages = [{"role": "system", "content": f"Genera un resumen conciso para una tesis en {carrera} titulada '{titulo}'."}]
        result = query_together(messages)
        st.write(result)
    
    elif tool_selected == "Generación de Conclusiones":
        st.subheader("🔚 Conclusiones Sugeridas")
        messages = [{"role": "system", "content": f"Escribe conclusiones apropiadas para una tesis en {carrera} titulada '{titulo}'."}]
        result = query_together(messages)
        st.write(result)
else:
    st.warning("Por favor, introduce la carrera y el título de la tesis en la barra lateral para continuar.")

st.sidebar.markdown("---")
st.sidebar.markdown("[Correción de textos en 24 horas](https://hablemosbien.org)")
