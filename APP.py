import streamlit as st
import streamlit.components.v1 as components
import os

# Configuración de la página en modo ancho para aprovechar la pantalla del consultorio
st.set_page_config(
    page_title="Sistema de Morbilidad - Ecografías",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ocultar los elementos visuales por defecto de Streamlit
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding-top: 0rem; padding-bottom: 0rem; padding-left: 1rem; padding-right: 1rem;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Nombre exacto del archivo tal como aparece en tu captura de GitHub
html_filename = "CLEMENTE.html"

if os.path.exists(html_filename):
    # Leer el archivo de la planilla ecográfica
    with open(html_filename, "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # Renderizar el HTML interactivo ocupando toda la pantalla
    components.html(html_code, height=1400, scrolling=True)
else:
    st.error(f"No se encontró el archivo '{html_filename}' en el repositorio.")