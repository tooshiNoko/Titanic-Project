import os
from PIL import Image
import streamlit as st

def cargar_imagenes():
    current_dir = os.path.dirname(__file__)
    image_dir = os.path.join(current_dir, 'assets', '.images')
    
    imagen_categorica_path = os.path.join(image_dir, '1_Variables_numericas.png')
    imagen_numerica_path = os.path.join(image_dir, '2_Variables_categoricas.png')
    imagen_librerias_path = os.path.join(image_dir, '20_librerias.png')
    
    imagen_categorica = Image.open(imagen_categorica_path)
    imagen_numerica = Image.open(imagen_numerica_path)
    imagen_librerias = Image.open(imagen_librerias_path)
    
    return imagen_categorica, imagen_numerica, imagen_librerias

def mostrar_pagina_inicial():
    st.title('Project Titanic 🚢')
    st.header('Introducción al conjunto de datos')
    st.write('Contamos con un dataset de 891 registros y 12 variables. Usamos las siguientes librerías para el análisis:')
    
    st.subheader('Librerías utilizadas')
    _, _, imagen_librerias = cargar_imagenes()
    st.image(imagen_librerias, caption='Librerías utilizadas')
    
    st.subheader('Distribución de Variables Categóricas')
    imagen_categorica, _, _ = cargar_imagenes()
    st.image(imagen_categorica, caption='Gráfico de variables categóricas')

    st.subheader('Distribución de Variables Numéricas')
    _, imagen_numerica, _ = cargar_imagenes()
    st.image(imagen_numerica, caption='Gráfico de variables numéricas')

def main():
    st.set_page_config(page_title='Análisis del Titanic', page_icon='🚢', layout='wide')
    mostrar_pagina_inicial()

if __name__ == "__main__":
    main()
