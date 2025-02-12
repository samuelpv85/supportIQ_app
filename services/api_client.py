import requests
from config import API_URL

# API_URL = "http://localhost:8000"

def create_task(data):
    """Envia datos a la API para iniciar una tarea."""
    response = requests.post(f"{API_URL}/tasks/", json=data)
    return response.json()

def get_task_status(task_id):
    """Consulta el estado de una tarea en la API."""
    response = requests.get(f"{API_URL}/tasks/{task_id}")
    return response.json()


# create_task(data) → Envía datos a FastAPI para iniciar una tarea.
# get_task_status(task_id) → Consulta el estado de la tarea en ejecución.