import streamlit as st
from PIL import Image
import os

# Datos para las secciones
observaciones = [
    {"Categoría": "Género", "Detalles": ["La media de edad de las pasajeras era mayor que la de los pasajeros."]},
    {"Categoría": "Clase de pasajero", "Detalles": ["Los pasajeros más mayores son los de 1a clase. Y en general cada clase es más joven que la anterior."]},
    {"Categoría": "Tarifas", "Detalles": ["Se aplicaron descuentos por familias y grupos."]}
]

factores_supervivencia = [
    {"Categoría": "Género", "Detalles": ["Las mujeres tenían una tasa de supervivencia significativamente mayor que los hombres."]},
    {"Categoría": "Clase de pasajero", "Detalles": ["Los pasajeros de primera clase tuvieron una mayor tasa de supervivencia, lo que indica que el estatus socioeconómico influyó en las posibilidades de supervivencia."]},
    {"Categoría": "Puerto de embarque", "Detalles": ["El recuento de supervivencia varió según el puerto de embarque."]},
    {"Categoría": "Clase y supervivencia", "Detalles": ["Los pasajeros que viajaron en 1a clase tuvieron una tasa de supervivencia superior a la de las clases más bajas."]},
    {"Categoría": "Familiares", "Detalles": ["Los pasajeros que viajaban solos o con familia poco numerosa tenían mayor posibilidad de sobrevivir."]},
    {"Categoría": "Edad", "Detalles": ["Los pasajeros más jóvenes tuvieron una mayor tasa de supervivencia."]}
]

# Función para cargar imagen
def cargar_imagen():
    current_dir = os.path.dirname(__file__)
    assets_dir = os.path.join(current_dir, '..', 'assets', '.images')
    return Image.open(os.path.join(assets_dir, '18_estudio_cabieron.png'))

# Main function
def main():
    st.set_page_config(page_title='Análisis del Titanic - Página 4', layout='wide')

    st.sidebar.title('Página 4: Conclusiones📝')
    seccion_elegida = st.sidebar.radio('Selecciona una sección:', [
        'Observaciones',
        'Factores influyentes en la supervivencia',
        'Conclusión general'
    ])

    if seccion_elegida == 'Observaciones':
        st.title('Observaciones')
        for obs in observaciones:
            st.subheader(obs["Categoría"])
            for detalle in obs["Detalles"]:
                st.write(f"- {detalle}")
            st.write("---")
        
    elif seccion_elegida == 'Factores influyentes en la supervivencia':
        st.title('Factores Influyentes en la Supervivencia')
        st.write('### Factores que influyen en la supervivencia de los pasajeros del Titanic')

        col1, col2 = st.columns(2)
        
        for i, factor in enumerate(factores_supervivencia):
            with (col1 if i % 2 == 0 else col2):
                st.subheader(factor['Categoría'])
                for detalle in factor["Detalles"]:
                    st.write(f"- {detalle}")
                st.write("---")
                
    elif seccion_elegida == 'Conclusión general':
        st.title('Conclusión General')
        st.markdown("""
        <div style='color: goldenrod; font-size: 24px; font-weight: bold;'>Fórmula de la Supervivencia</div>
        """, unsafe_allow_html=True)
        st.write("""
        <div style='font-size: 20px;'>
        <p>Si por alguna razón del destino tuvieras que viajar al S.XX y abordar el Titanic, te recomendaría que si pudieses escoger:</p>
        <ul>
            <li>Fueses mujer.</li>
            <li>Fueses joven.</li>
            <li>Viajases en primera clase.</li>
            <li>Tuvieses el título de Mrs.</li>
            <li>Estuvieses acompañada de un número moderado de familiares.</li>
            <li>Embarcases en Cherbourg.</li>
        </ul>
        <p>Es claro que ningún algoritmo puede predecir con certeza del 100% la tasa de supervivencia basándose únicamente en la ubicación del pasajero en el barco o en su edad, ya que el factor humano y la inesperada emergencia también jugaron un papel crucial en el proceso de rescate.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button('Bonus Extra Conclusión'):
            imagen = cargar_imagen()
            st.image(imagen, caption='Imagen de Conclusión', use_column_width=True)

if __name__ == "__main__":
    main()
