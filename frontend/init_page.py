import streamlit as st

def init():
    # Configuración inicial de la interfaz
    st.title("Simulador de un Computador")
    # Crear tres columnas
    col1, col2, col3 = st.columns(3)

    # Contenido de la primera columna
    with col1:
        st.write("#### _PROCESADOR_:")
        PC_placeholder = st.empty()
        IR_placeholder = st.empty()
        MBR_placeholder = st.empty()
        MAR_placeholder = st.empty()
        ALU_placeholder = st.empty()
        CONTROL_UNIT_placeholder = st.empty()
        programa = st.text_area("Escribe las instrucciones del programa separadas por punto y coma", 
                            "A = 1; B = 2; PUSH A; PUSH B; ADD; POP C; END")
        execute = False
        if st.button("Cargar Programa"):
            execute = True
        mensaje_placeholder = st.empty()
        
    # Contenido de la segunda columna
    with col2:
        st.write("#### _Buses_:")
        DATA_placeholder = st.empty()
        ADDRESS_placeholder = st.empty()
        CONTROL_placeholder = st.empty()
        
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("#### _Salida del Programa_:")
        OUTPUT_placeholder = st.empty()

    # Contenido de la tercera columna
    with col3:
        st.write("#### _Banco de Registros:_:")
        BANK_REGISTER_placeholder = st.empty()
        st.write("#### _Memoria_:")
        MEMORY_placeholder = st.empty()
    