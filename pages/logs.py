import streamlit as st
import requests
from config import API_URL

def show():
    st.title("📜 Logs del Sistema")
    
    try:
        response = requests.get(f"{API_URL}/logs")
        logs = response.json()
        
        if logs:
            for log in logs:
                with st.expander(f"📌 {log['timestamp']} - {log['method']} {log['path']}"):
                    st.write(f"**Status:** {log['status_code']}")
                    st.write(f"**IP Cliente:** {log['client_ip']}")
        else:
            st.info("No hay logs registrados.")
    
    except Exception as e:
        st.error(f"Error al obtener logs: {e}")




# requests.get(f"{API_URL}/logs") → Consume la API de FastAPI para obtener logs.
# st.expander() → Permite colapsar los detalles de cada log.
# st.info() → Muestra un mensaje si no hay logs.