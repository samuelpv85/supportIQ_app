import streamlit as st
import requests
from config import API_URL

def show():
    st.title("💻 Ejecutar Comandos en Servidores Remotos")

    server_ip = st.text_input("Dirección IP del Servidor")
    username = st.text_input("Usuario SSH")
    password = st.text_input("Contraseña (opcional, si no usas llave)", type="password")
    command = st.text_area("Comando a ejecutar")

    if st.button("Ejecutar"):
        if server_ip and username and command:
            data = {"server_ip": server_ip, "username": username, "password": password, "command": command}
            # response = requests.post(f"{API_URL}/execute", json=data)
            response = requests.post(f"{API_URL}/ssh/execute", json=data)  # Agrega "/ssh"

            
            if response.status_code == 200:
                st.success("✅ Comando ejecutado con éxito")
                st.code(response.json().get("output"), language="bash")
            else:
                st.error(f"❌ Error: {response.json().get('detail')}")
        else:
            st.warning("Por favor, completa los campos requeridos.")


# st.text_input() → Permite ingresar la IP del servidor.
# st.text_area() → Campo para escribir el comando.
# requests.post(f"{API_URL}/execute", json=data) → Envía el comando a FastAPI.
# st.code() → Muestra la salida del comando en formato de terminal.


# st.text_input() → Recibe IP, usuario y contraseña SSH.
# requests.post(f"{API_URL}/execute", json=data) → Envía los datos a FastAPI.
# st.code(response.json().get("output")) → Muestra la salida en formato terminal.