import streamlit as st
from frontend.simulator import init

def init_page():
    # Configuración inicial de la interfaz
    st.title("Simulador de un Computador")
    execute = False
    programa = ""
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
        st.write("")
        CONTROL_UNIT_placeholder = st.empty()
        st.write("#### _PROGRAMA_")
        programa = st.text_area("Escribe las instrucciones del programa separadas por punto y coma", 
                            "A = 1; B = 2; PUSH A; PUSH B; ADD; POP C; END")
        if st.button("Cargar Programa"):
            execute = True
        MESSAGE_placeholder = st.empty()
        
    # Contenido de la segunda columna
    with col2:
        st.write("#### _BUSES_:")
        DATA_placeholder = st.empty()
        CONTROL_placeholder = st.empty()
        ADDRESS_placeholder = st.empty()
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        
        st.write("#### _SALIDA DEL PROGRAMA_:")
        OUTPUT_placeholder = st.empty()

    # Contenido de la tercera columna
    with col3:
        st.write("#### _BANCO DE REGISTROS_:")
        REGISTER_placerholder = st.empty()
        BANK_REGISTER_placeholder = st.empty()
        
        st.write("#### _MEMORIA_:")
        MEM_DATA_placerholder = st.empty()
        MEM_DIR_placerholder = st.empty()
        MEMORY_placeholder = st.empty()
        # Mensaje adicional
        st.caption("Memoria representada en un formato de tabla con valores binarios de 32 bits.")

    init(programa, execute, MESSAGE_placeholder, PC_placeholder, IR_placeholder, MBR_placeholder, MAR_placeholder, ALU_placeholder, CONTROL_UNIT_placeholder, DATA_placeholder, ADDRESS_placeholder, CONTROL_placeholder, BANK_REGISTER_placeholder, REGISTER_placerholder, MEMORY_placeholder, MEM_DATA_placerholder, MEM_DIR_placerholder, OUTPUT_placeholder)