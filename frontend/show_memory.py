import streamlit as st
import pandas as pd

def mostrar_memoria(memory_array, memory):
    """
    Muestra el contenido de un array de memoria en un DataFrame estilizado en Streamlit.
    :param memory_array: Array que representa la memoria (lista de valores).
    """
    # Crear un DataFrame desde el array, obteniendo el índice como dirección
    df_memoria = pd.DataFrame(enumerate(memory_array), columns=["Dirección", "Valor"])

    # Eliminar la columna de índice en la visualización
    memory.dataframe(
        df_memoria.drop(columns=["Dirección"]).style  # Elimina la columna "Dirección"
        .set_properties(**{'text-align': 'center'})  # Centrar el texto
        .set_table_styles([
            {"selector": "thead th", "props": [("text-align", "center"), ("background-color", "#37580D"), ("color", "white")]}
        ])
        .highlight_max(subset=["Valor"], color="#37580D")  # Resaltar máximo valor en "Valor"
        .hide(axis="index"),  # Ocultar el índice en el DataFrame
        height=245
        
    )
