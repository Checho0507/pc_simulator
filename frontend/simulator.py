from simulator.simulator import Simulator
from frontend.show_memory import mostrar_memoria
from frontend.show_registers import mostrar_registros

def init(programa, execute, MESSAGE_placeholder, PC_placeholder, IR_placeholder, MBR_placeholder, MAR_placeholder, ALU_placeholder, CONTROL_UNIT_placeholder, DATA_placeholder, ADDRESS_placeholder, CONTROL_placeholder, BANK_REGISTER_placeholder, REGISTER_placeholder, MEMORY_placeholder, MEM_DATA_placeholder, MEM_DIR_placeholder, OUTPUT_placeholder):
    simulator = Simulator()
    PC_placeholder.write(f"###### _PC_: {simulator.controlUnit.registerBank.PC.getValue()} ")
    IR_placeholder.write(f"###### _IR_: {simulator.controlUnit.registerBank.IR.getValue()}")
    MBR_placeholder.write(f"###### _MBR_: {simulator.controlUnit.registerBank.MBR.getValue()}")
    MAR_placeholder.write(f"###### _MAR_: {simulator.controlUnit.registerBank.MAR.getValue()}")
    ALU_placeholder.write(f"###### _ALU_: {simulator.int_to_binary(simulator.controlUnit.alu.getResult(), 32)}")
    CONTROL_UNIT_placeholder.write(f"###### _CONTROL UNIT_: {
            simulator.controlUnit.controlBus.getControlSignal()}")
    if execute == True:
        simulator.executeProgram(programa.split(";"), MESSAGE_placeholder, MEM_DIR_placeholder, MEM_DATA_placeholder, REGISTER_placeholder,  PC_placeholder, IR_placeholder, MBR_placeholder, MAR_placeholder, ALU_placeholder, CONTROL_UNIT_placeholder, DATA_placeholder, ADDRESS_placeholder, CONTROL_placeholder, BANK_REGISTER_placeholder, MEMORY_placeholder, OUTPUT_placeholder)
    MESSAGE_placeholder.info("Presione cargar programa para comenzar la ejecución")
    
    DATA_placeholder.write(f"###### _Bus de Datos_: {simulator.memory.dataBus.getData()}")
    CONTROL_placeholder.write(f"###### _Bus de Control_: {simulator.controlUnit.controlBus.getControlSignal()}")
    ADDRESS_placeholder.write(f"###### _Bus de Direcciones_: {simulator.memory.addressBus.getAddress()}")
       
    OUTPUT_placeholder.text_area("Salida respecto a la ejecución del programa", disabled=True)
    
    REGISTER_placeholder.write(f"###### _REG_: {simulator.memory.dataBus.getData()}")
    mostrar_registros(simulator.registerBank.registers, BANK_REGISTER_placeholder)
    MEM_DATA_placeholder.write(f"###### _DAT_: {simulator.memory.dataBus.getData()}")
    MEM_DIR_placeholder.write(f"###### _DIR_: {simulator.memory.dataBus.getData()}")
    mostrar_memoria(simulator.memory.memoryArray, MEMORY_placeholder)
    
    