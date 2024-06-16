import pandas as pd
import streamlit as st

@st.cache_resource
def cargar_datos():
    return pd.read_csv(r'Temario\Modulo1\00_Proyecto_modulo1\Titanic_project\titanic.csv')
