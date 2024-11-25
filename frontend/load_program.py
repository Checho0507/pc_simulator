import streamlit as st

def load_program(simulator):
    opcion = st.selectbox("Cantidad de direcciones: ", ["Cero Direcciones", "Una dirección", "Dos direcciones", "Tres Direcciones"])
    if opcion == "Cero Direcciones":
        st.subheader("Carga de Programa")
        programa = st.text_area("Escribe las instrucciones del programa separadas por punto y coma", 
                        "A = 1; B = 2; PUSH A; PUSH B; ADD; POP C; END")
        if st.button("Cargar Programa"):
            # Dividir las instrucciones por comas
            instrucciones = [instr.strip() for instr in programa.split(";")]
            
            # Cargar el programa en el simulador
            simulator.executeProgram(instrucciones)
            
            st.success("Programa cargado correctamente.")
            st.write("Instrucciones cargadas:")
            st.code("\n".join(instrucciones))