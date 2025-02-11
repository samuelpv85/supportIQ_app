import streamlit as st
from pages import home, logs, commands, ansible

st.set_page_config(page_title="Mi App Streamlit", layout="wide")

PAGES = {
    "🏠 Home": home,
    "📜 Logs": logs,
    "🖥️ Commands": commands,
    "🖥️ Ansible": ansible
}

st.sidebar.title("Navegación SupportIQ")
selection = st.sidebar.radio("Ir a", list(PAGES.keys()))
page = PAGES[selection]
page.show()
