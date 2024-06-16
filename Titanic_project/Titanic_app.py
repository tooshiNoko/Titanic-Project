import streamlit as st
from PIL import Image

def cargar_imagenes():
    imagen_categorica = Image.open(r'assets\.images\1_Variables_numericas.png')
    imagen_numerica = Image.open(r'Titanic_project\assets\.images\2_Variables_categoricas.png')
    return imagen_categorica, imagen_numerica


def mostrar_pagina_inicial():
    st.title('Project Titanic 🚢')
    st.header('Introducción al conjunto de datos')
    st.write('En esta sección se proporciona una visión general del conjunto de datos del Titanic.')

    st.subheader('Distribución de Variables Categóricas')
    imagen_categorica, _ = cargar_imagenes()
    st.image(imagen_categorica, caption='Gráfico de variables categóricas')

    st.subheader('Distribución de Variables Numéricas')
    _, imagen_numerica = cargar_imagenes()
    st.image(imagen_numerica, caption='Gráfico de variables numéricas')

def main():
    st.set_page_config(page_title='Análisis del Titanic', layout='wide')
    mostrar_pagina_inicial()

if __name__ == "__main__":
    main()