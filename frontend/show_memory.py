import streamlit as st
import pandas as pd

def mostrar_memoria(memory_array, memory):
    """
    Muestra el contenido de un array de memoria en un DataFrame estilizado en Streamlit.
    Resalta solo el último elemento agregado.
    :param memory_array: Array que representa la memoria (lista de valores).
    :param memory: Contenedor de Streamlit para mostrar el DataFrame.
    """
    # Crear un DataFrame desde el array, obteniendo el índice como dirección
    df_memoria = pd.DataFrame({
        "Dirección": range(len(memory_array)),
        "Valor": memory_array
    })

    # Función para aplicar estilos: Resaltar la última fila
    def resaltar_ultimo(x):
        is_last = x.index == len(x) - 1  # Detecta la última fila
        return ["background-color: #37580D; color: white;" if v else "" for v in is_last]

    # Aplicar estilos al DataFrame
    styled_df = df_memoria.style \
        .apply(resaltar_ultimo, axis=0) \
        .set_properties(**{'text-align': 'center'}) \
        .set_table_styles([
            {"selector": "thead th", "props": [("text-align", "center"), ("background-color", "#37580D"), ("color", "white")]}
        ]) \
        .hide(axis="index")  # Ocultar el índice en el DataFrame

    # Mostrar el DataFrame estilizado
    memory.dataframe(styled_df, height=500)
