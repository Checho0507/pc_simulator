import pandas as pd
import streamlit as st

def mostrar_registros(registers, registros):
        """
        Muestra todos los registros del RegisterBank en un DataFrame de Streamlit.
        """
        # Crear una lista con los nombres y valores de los registros
        registros_data = [(nombre, registro) for nombre, registro in registers.items()]

        # Crear un DataFrame a partir de los registros
        df_registros = pd.DataFrame(registros_data, columns=["Registro", "Valor"])

        # Estilizar y mostrar el DataFrame en Streamlit
        registros.dataframe(
            df_registros.style
            .set_properties(**{'text-align': 'center'})  # Centrar el texto
            .set_table_styles([
                {"selector": "thead th", "props": [("text-align", "center"), ("background-color", "#37580D"), ("color", "white")]}
            ])
            .highlight_max(subset=["Valor"], color="#37580D")  # Resaltar el valor máximo
            .hide(axis="index"),
            width=290
        )