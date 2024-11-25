import streamlit as st
from simulator.simulator import Simulator
from frontend.show_memory import mostrar_memoria
from frontend.show_registers import mostrar_registros

def init():
    simulator = Simulator()
    st.set_page_config(layout="wide")

    # Configuración inicial de la interfaz
    st.title("Simulador de un Computador")
    # Crear tres columnas
    col1, col2, col3 = st.columns(3)

    # Contenido de la primera columna
    with col1:
        st.write("#### _PROCESADOR_:")
        st.write(f"###### _PC_: {simulator.controlUnit.registerBank.PC.getValue()}")
        st.write(f"###### _IR_: {simulator.controlUnit.registerBank.IR.getValue()}")
        st.write(f"###### _MBR_: {simulator.controlUnit.registerBank.MBR.getValue()}")
        st.write(f"###### _MAR_: {simulator.controlUnit.registerBank.MAR.getValue()}")
        st.write(f"###### _ALU_: {simulator.int_to_binary(simulator.controlUnit.alu.getResult(), 32)}")
        st.write(f"###### _CONTROL UNIT_: {simulator.controlUnit.controlBus.getControlSignal()}")
        st.write("#### _Programa_:")
        programa = st.text_area("Escribe las instrucciones del programa separadas por punto y coma", 
                            "A = 1; B = 2; PUSH A; PUSH B; ADD; POP C; END")
    
        if st.button("Cargar Programa"):
            pass

    # Contenido de la segunda columna
    with col2:
        st.write("#### _Buses_:")
        st.write(f"##### _Bus de Datos_: {simulator.memory.dataBus.getData()}")
        st.write(f"##### _Bus de Direcciones_: {simulator.memory.addressBus.getAddress()}")
        st.write(f"##### _Bus de Control_: {simulator.controlUnit.controlBus.getControlSignal()}")
        
        st.write("")
        st.write("#### _Salida del Programa_:")
        st.text_area("Salida respecto a la ejecución del programa","hhh", disabled=True)

    # Contenido de la tercera columna
    with col3:
        st.write("#### _Banco de Registros:_:")
        mostrar_registros(simulator.registerBank.registers)
        st.write("#### _Memoria_:")
        mostrar_memoria(simulator.memory.memoryArray)
    
    