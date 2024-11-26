import streamlit as st
from simulator.simulator import Simulator
from frontend.show_memory import mostrar_memoria
from frontend.show_registers import mostrar_registros

def init():
    st.set_page_config(layout="wide")
    simulator = Simulator()
    # Configuración inicial de la interfaz
    st.title("Simulador de un Computador")
    # Crear tres columnas
    col1, col2, col3 = st.columns(3)

    # Contenido de la primera columna
    with col1:
        st.write("#### _PROCESADOR_:")
        PC_placeholder = st.empty()
        PC_placeholder.write(f"###### _PC_: {simulator.controlUnit.registerBank.PC.getValue()}")
        IR_placeholder = st.empty()
        IR_placeholder.write(f"###### _IR_: {simulator.controlUnit.registerBank.IR.getValue()}")
        MBR_placeholder = st.empty()
        MBR_placeholder.write(f"###### _MBR_: {simulator.controlUnit.registerBank.MBR.getValue()}")
        MAR_placeholder = st.empty()
        MAR_placeholder.write(f"###### _MAR_: {simulator.controlUnit.registerBank.MAR.getValue()}")
        ALU_placeholder = st.empty()
        ALU_placeholder.write(f"###### _ALU_: {
            simulator.int_to_binary(simulator.controlUnit.alu.getResult(), 32)}")
        CONTROL_UNIT_placeholder = st.empty()
        CONTROL_UNIT_placeholder.write(f"###### _CONTROL UNIT_: {
            simulator.controlUnit.controlBus.getControlSignal()}")
        st.write("#### _Programa_:")
        programa = st.text_area("Escribe las instrucciones del programa separadas por punto y coma", 
                            "A = 1; B = 2; PUSH A; PUSH B; ADD; POP C; END")
        execute = False
        if st.button("Cargar Programa"):
            execute = True
        mensaje_placeholder = st.empty()
        if execute == True:
            simulator.executeProgram(
                programa.split(";"), mensaje_placeholder, PC_placeholder, IR_placeholder, MBR_placeholder, 
                MAR_placeholder, ALU_placeholder, CONTROL_UNIT_placeholder)
        mensaje_placeholder.info("Presione cargar programa para comenzar la ejecución")
        
        
        

    # Contenido de la segunda columna
    with col2:
        st.write("#### _Buses_:")
        DATA_placeholder = st.empty()
        DATA_placeholder.write(f"##### _Bus de Datos_: {simulator.memory.dataBus.getData()}")
        ADDRESS_placeholder = st.empty()
        ADDRESS_placeholder.write(f"##### _Bus de Direcciones_: {simulator.memory.addressBus.getAddress()}")
        CONTROL_placeholder = st.empty()
        CONTROL_placeholder.write(f"##### _Bus de Control_: {simulator.controlUnit.controlBus.getControlSignal()}")
        
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("#### _Salida del Programa_:")
        OUTPUT_placeholder = st.empty()
        OUTPUT_placeholder.text_area("Salida respecto a la ejecución del programa", disabled=True)

    # Contenido de la tercera columna
    with col3:
        st.write("#### _Banco de Registros:_:")
        mostrar_registros(simulator.registerBank.registers)
        st.write("#### _Memoria_:")
        mostrar_memoria(simulator.memory.memoryArray)
    
    