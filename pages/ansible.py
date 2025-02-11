import streamlit as st
import requests
from config import API_URL

def show():
    st.title("🚀 Automatización con Ansible")

    playbook = st.selectbox("Selecciona un Playbook", ["deploy_app", "update_servers"])
    
    if st.button("Ejecutar Playbook"):
        response = requests.post(f"{API_URL}/run-playbook/{playbook}")

        if response.status_code == 200:
            st.success("✅ Playbook ejecutado con éxito")
            st.text_area("Salida del Playbook", response.json().get("output"), height=300)
        else:
            st.error(f"❌ Error: {response.json().get('detail')}")



# st.selectbox() → Permite seleccionar el playbook.
# requests.post(f"{API_URL}/run-playbook/{playbook}") → Ejecuta el playbook en FastAPI.
# st.text_area(response.json().get("output")) → Muestra la salida de la ejecución.