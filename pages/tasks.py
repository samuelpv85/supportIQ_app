import streamlit as st
from services.api_client import create_task, get_task_status
import time


def show():
    st.title("Tareas en Segundo Plano con Celery")

    if st.button("Ejecutar Tarea"):
        task_data = {"message": "Procesar esta información"}
        task = create_task(task_data)
        st.session_state["task_id"] = task["task_id"]

    if "task_id" in st.session_state:
        task_id = st.session_state["task_id"]
        st.write(f"Tarea en proceso: {task_id}")
        
        with st.spinner("Procesando..."):
            while True:
                task_status = get_task_status(task_id)
                if task_status["status"] == "SUCCESS":
                    st.success("Tarea completada 🎉")
                    st.write(task_status["result"])
                    break
                elif task_status["status"] == "FAILURE":
                    st.error("Error en la tarea ❌")
                    break
                time.sleep(1)


# Botón "Ejecutar Tarea" → Inicia una tarea en la API.
# Muestra el estado de la tarea en tiempo real.
