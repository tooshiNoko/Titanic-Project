### 🚢 Análisis del Titanic

Bienvenido a mi proyecto de análisis del Titanic! 🌊 

Este proyecto tiene como objetivo explorar el famoso conjunto de datos del Titanic, descubrir patrones interesantes y visualizar los resultados con Streamlit.

 #### Descripción

Este proyecto consta de dos partes:

1. Análisis Exploratorio de Datos (EDA): Realizado en un Jupyter Notebook, donde se profundiza en el análisis de las variables del dataset y se generan visualizaciones iniciales.
2. Aplicación Interactiva: Construida con Streamlit, que permite una exploración interactiva de los datos y presenta las conclusiones del análisis de una manera intuitiva.

#### Características

- 📊 Gráficos interactivos: Visualizaciones de las variables categóricas y numéricas.
- 🔍 Exploración de datos: Una sección para observar las primeras filas del conjunto de datos.
- 📝 Conclusiones: Un resumen de las observaciones clave y factores influyentes en la supervivencia.
- 📔 Notebook Jupyter: Análisis detallado con visualizaciones y explicaciones.

#### Cómo ejecutar el proyecto

**Requisitos previos**
- Python 3.7 o superior
- Jupyter Notebook
- Streamlit

1. Clona este repositorio

```
git clone https://github.com/Mikiserra/titanic-project.git
cd titanic-analysis
```

2. Instala las dependencias

```
pip install -r requirements.txt
```

3. Ejecuta el Notebook

Para abrir el análisis exploratorio de datos en Jupyter Notebook:

```
jupyter notebook
```

Abre el archivo titanic.ipynb para ver y ejecutar el análisis.

4. Ejecuta la aplicación de Streamlit

```
 streamlit run titanic_app.py
```

Esto debería abrir automáticamente tu navegador con la aplicación de Streamlit.

### Estructura del Proyecto

```
titanic-analysis/
    │
    ├── assets/
    │   └── .images/
    │       ├── 1_Variables_numericas.png
    │       └── 2_Variables_categoricas.png
    │
    ├── utils/
    │   └── data_loading.py
    │
    ├── titanic_analysis.ipynb
    ├── titanic_app.py
    ├── requirements.txt
    └── README.md
```

- assets/.images/: Imágenes utilizadas en la aplicación.
- utils/data_loading.py: Script para cargar los datos del Titanic.
- titanic_analysis.ipynb: Análisis exploratorio de datos en Jupyter Notebook.
- titanic_app.py: El script principal de Streamlit.
- requirements.txt: Archivo de dependencias de Python.
- README.md: Este archivo.

### Despliegue

La aplicación está desplegada en Streamlit. Puedes verla en acción [aquí](link_de_la_aplicacion).


¡Gracias por visitar y espero que disfrutes explorando los datos del Titanic! 🚢✨
