import streamlit as st
from PIL import Image

# Función para cargar imágenes
def cargar_imagenes(variable):
    if variable == 'Estudio correlación de variables':
        return [
            Image.open('assets/.images/5_matriz_correlacion.png'),
       
        ]
    elif variable == 'Supervivientes según género y edad':
        return [
            Image.open('assets/.images/7_supervivientes_genero.png'),
            Image.open('assets/.images/8_supervivientes_edad.png'),
            Image.open('assets/.images/9_supervivientes_genero_edad.png')
        ]
    elif variable == 'Supervivientes según clase social':
        return [
            Image.open('assets/.images/10_supervivientes_genero_clase.png'),
            Image.open('assets/.images/12_supervivientes_clase_fare.png')
        ]
    elif variable == 'Supervivientes según puerto de embarcación':
        return Image.open('assets/.images/11_supervivientes_embarked.png')
    elif variable == 'Supervivientes según tamaño de familia':
        return Image.open('assets/.images/13_supervivientes_familysize.png')
    elif variable == 'Variable Títulos':
        return Image.open('assets/.images/14_supervivientes_titulo.png')

def main():
    st.set_page_config(page_title='Análisis del Titanic - Página 3', layout='wide')

    st.sidebar.title('Página 3: Análisis de Variables📊')
    seccion_elegida = st.sidebar.radio('Selecciona una variable:', [
        'Estudio correlación de variables',
        'Supervivientes según género y edad',
        'Supervivientes según clase social',
        'Supervivientes según puerto de embarcación',
        'Supervivientes según tamaño de familia',
        'Variable Títulos'
    ])

    st.title(seccion_elegida)

    # Mostrar descripción y luego la imagen correspondiente
    if seccion_elegida == 'Estudio correlación de variables':
        st.write('Análisis de la correlación entre variables del conjunto de datos del Titanic:')
        imagenes = cargar_imagenes(seccion_elegida)
        st.image(imagenes[0], caption='Matriz de correlación')
        

    elif seccion_elegida == 'Supervivientes según género y edad':
        st.write('Análisis de los supervivientes a bordo del Titanic según género y edad:')
        imagenes = cargar_imagenes(seccion_elegida)
        st.image(imagenes[0], caption='Supervivientes por género' )
        st.image(imagenes[1], caption='Supervivientes por edad')
        st.image(imagenes[2], caption='Supervivientes por género y edad')

    elif seccion_elegida == 'Supervivientes según clase social':
        st.write('Análisis de los supervivientes según la clase social:')
        imagenes = cargar_imagenes(seccion_elegida)
        st.image(imagenes[0], caption='Supervivientes por género y clase')
        st.image(imagenes[1], caption='Supervivientes por clase y tarifa')

    elif seccion_elegida == 'Supervivientes según puerto de embarcación':
        st.write('Análisis del puerto de embarcación de los pasajeros del Titanic:')
        imagen = cargar_imagenes(seccion_elegida)
        st.image(imagen, caption='Supervivientes por puerto de embarcación')

    elif seccion_elegida == 'Supervivientes según tamaño de familia':
        st.write('Análisis del tamaño de la familia de los pasajeros del Titanic:')
        imagen = cargar_imagenes(seccion_elegida)
        st.image(imagen, caption='Supervivientes por tamaño de familia')

    elif seccion_elegida == 'Variable Títulos':
        st.write('Análisis del título de los pasajeros del Titanic:')
        imagen = cargar_imagenes(seccion_elegida)
        st.image(imagen, caption='Supervivientes por título')

if __name__ == "__main__":
    main()
