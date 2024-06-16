import streamlit as st
from PIL import Image

# Función para cargar imágenes
def cargar_imagenes(variable):
    if variable == 'Variable Age ':
        return Image.open('assets/.images/4_KNN_Age.png')
    elif variable == 'Variable Name':
        return Image.open('assets/.images/6_titulos.png')
    elif variable == 'Tratamiento valores nulos':
        return Image.open('assets/.images/3_Heatmap_nulos.png')
    elif variable == 'Variable Embarked':
        return Image.open('assets/.images/16_Titanic_route.png')

def main():
    st.set_page_config(page_title='Análisis del Titanic - Página 2', layout='wide')

    st.sidebar.title('Página 2: Preprocesamiento de Datos 🗂️')
    seccion_elegida = st.sidebar.radio('Selecciona una variable:',['Tratamiento valores nulos', 'Variable Age ', 'Variable Embarked', 'Variable Name'])

    st.title(seccion_elegida)

    
    if seccion_elegida == 'Tratamiento valores nulos':
        st.write('A continuación se muestra el tratamiento de valores nulos utilizando un mapa de calor:')
        imagen = cargar_imagenes(seccion_elegida)
        st.image(imagen, caption=f'Imagen de {seccion_elegida}')  

    elif seccion_elegida == 'Variable Embarked':
        st.write('Utilizamos la moda para completar los valores nulos de la variable Embarked.')
        imagen = cargar_imagenes(seccion_elegida)
        st.image(imagen, caption=f'Imagen de {seccion_elegida}', use_column_width=True)

    else:
        
        imagen = cargar_imagenes(seccion_elegida)
        st.image(imagen, caption=f'Imagen de {seccion_elegida}')

if __name__ == "__main__":
    main()
