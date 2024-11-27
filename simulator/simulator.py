import pandas as pd
import streamlit as st
import time
from collections import deque
from frontend.show_memory import mostrar_memoria
from frontend.show_registers import mostrar_registros
from simulator.bus.address_bus import AddressBus
from simulator.bus.control_bus import ControlBus
from simulator.bus.data_bus import DataBus
from simulator.control_unit import ControlUnit
from simulator.memory import Memory
from simulator.register_bank import RegisterBank
from frontend.show_memory import mostrar_memoria
from frontend.show_registers import mostrar_registros

class Simulator:
    def __init__(self):
        self.pila = deque()
        # Crear buses
        self.dataBus = DataBus()
        self.addressBus = AddressBus()
        self.controlBus = ControlBus()

        # Crear componentes principales
        self.registerBank = RegisterBank()
        self.memory = Memory(64, self.dataBus, self.addressBus)
        self.controlUnit = ControlUnit(self.dataBus, self.addressBus, self.controlBus, 
                                       self.registerBank, self.memory)
        
    def executeProgram(self, programa, MESSAGE_placeholder, DIR_placeholder, DAT_placeholder, REG_placeholder, PC_placeholder, IR_placeholder, MBR_placeholder, 
                       MAR_placeholder, ALU_placeholder, CONTROL_UNIT_placeholder, DATA_placeholder, 
                       ADDRESS_placeholder, CONTROL_placeholder, BANK_REGISTER_placeholder, MEMORY_placeholder,
                       OUTPUT_placeholder):
        print("Loading zero-address instructions:")
        MESSAGE_placeholder.info("Cargando programa...")
        PC_placeholder.write(f"###### _PC_: {self.registerBank.PC.getValue()}")
        IR_placeholder.write(f"###### _IR_: {self.registerBank.IR.getValue()}")
        MBR_placeholder.write(f"###### _MBR_: {self.registerBank.MBR.getValue()}")
        MAR_placeholder.write(f"###### _MAR_: {self.registerBank.MAR.getValue()}")
        ALU_placeholder.write(f"###### _ALU_: {self.int_to_binary(self.controlUnit.alu.getResult(),32)}")
        DATA_placeholder.write(f"###### _Bus de Datos_: {self.memory.dataBus.getData()}")
        ADDRESS_placeholder.write(f"###### _Bus de Direcciones_: {self.memory.addressBus.getAddress()}")
        CONTROL_placeholder.write(f"###### _Bus de Control_: {self.controlUnit.controlBus.getControlSignal()}")
        CONTROL_UNIT_placeholder.write(f"###### _CONTROL UNIT_: {self.controlUnit.controlBus.getControlSignal()}")
        REG_placeholder.write(f"###### _REG_: {self.registerBank.PC.getValue()}")
        DAT_placeholder.write(f"###### _DAT_: {self.registerBank.PC.getValue()}")
        DIR_placeholder.write(f"###### _DIR_: {self.registerBank.PC.getValue()}")
        mostrar_registros(self.registerBank.registers, BANK_REGISTER_placeholder)
        mostrar_memoria(self.memory.memoryArray, MEMORY_placeholder)
        OUTPUT_placeholder.text_area("Salida respecto a la ejecución del programa", disabled=True)
        time.sleep(self.controlUnit.tiempo)
        count = self.add_asigns(programa, REG_placeholder, MESSAGE_placeholder, BANK_REGISTER_placeholder, CONTROL_UNIT_placeholder, DATA_placeholder)
        self.encode_instructions_zero(programa, MESSAGE_placeholder, CONTROL_UNIT_placeholder)
        self.load_program_zero(programa, REG_placeholder, DIR_placeholder, DAT_placeholder, MESSAGE_placeholder, PC_placeholder, MBR_placeholder, MAR_placeholder, ALU_placeholder, CONTROL_UNIT_placeholder, DATA_placeholder, ADDRESS_placeholder, MEMORY_placeholder)
        MESSAGE_placeholder.info("Reiniciando el contador del programa...")
        time.sleep(self.controlUnit.tiempo)
        self.registerBank.PC.setValue("00000000000000000000000000000000")
        PC_placeholder.write(f"###### _PC_: {self.registerBank.PC.getValue()}")
        MESSAGE_placeholder.info("Se reinició el contador del programa...")
        time.sleep(self.controlUnit.tiempo)
        
        self.pila.clear()
        for i in range(len(programa)-count):
            self.controlBus.sendControlSignal("11000000000000000000000000000011", MESSAGE_placeholder)
            CONTROL_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Control: {self.controlUnit.controlBus.getControlSignal()}</strong></p>""", unsafe_allow_html=True)    
            time.sleep(self.controlUnit.tiempo)
            CONTROL_placeholder.write(f"###### _Bus de Control_: {self.controlUnit.controlBus.getControlSignal()}")
            self.controlBus.receiveControlSignal(MESSAGE_placeholder)
            time.sleep(self.controlUnit.tiempo)
            self.controlUnit.fetch(MESSAGE_placeholder, DIR_placeholder, DAT_placeholder, PC_placeholder, IR_placeholder, MAR_placeholder, MBR_placeholder, ADDRESS_placeholder, DATA_placeholder)
        
            self.controlBus.sendControlSignal("11011000000000000000000000011011", MESSAGE_placeholder)
            CONTROL_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Control: {self.controlUnit.controlBus.getControlSignal()}</strong></p>""", unsafe_allow_html=True)   
            time.sleep(self.controlUnit.tiempo)
            CONTROL_placeholder.write(f"###### _Bus de Control_: {self.controlUnit.controlBus.getControlSignal()}")
            self.controlBus.receiveControlSignal(MESSAGE_placeholder)
            time.sleep(self.controlUnit.tiempo)
            codop, operand1, operand2 = self.controlUnit.decode(MESSAGE_placeholder)
            time.sleep(self.controlUnit.tiempo)
            CONTROL_UNIT_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>CONTROL UNIT: {self.registerBank.IR.getValue()}</strong></p>""", unsafe_allow_html=True)  
            MESSAGE_placeholder.success(f"Instrucción decodificada con éxito: \ncodop: {codop} - operando 1: {operand1} - operando 2: {operand2}")
            time.sleep(self.controlUnit.tiempo)
            CONTROL_UNIT_placeholder.write(f"###### _CONTROL UNIT_: {self.controlUnit.controlBus.getControlSignal()}")
            
            
            self.controlBus.sendControlSignal("11011011000000000000000011011011", MESSAGE_placeholder)
            CONTROL_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Control: {self.controlUnit.controlBus.getControlSignal()}</strong></p>""", unsafe_allow_html=True)   
            time.sleep(self.controlUnit.tiempo)
            CONTROL_placeholder.write(f"###### _Bus de Control_: {self.controlUnit.controlBus.getControlSignal()}")
            self.controlBus.receiveControlSignal(MESSAGE_placeholder)
            time.sleep(self.controlUnit.tiempo)
            self.execute(codop, operand1, operand2, REG_placeholder, BANK_REGISTER_placeholder, ALU_placeholder, MESSAGE_placeholder, DATA_placeholder, OUTPUT_placeholder)
            
            self.controlUnit.value_operation=self.int_to_binary(self.controlUnit.alu.getResult())
            self.controlUnit.alu.add(1,int(self.registerBank.PC.getValue(),2),1,1)
            
            self.registerBank.PC.setValue(self.int_to_binary(self.controlUnit.alu.getResult(),32))
        
    def add_asigns(self, programa, REG_placeholder, MESSAGE_placeholder, BANK_REGISTER_placeholder, CONTROL_UNIT_placeholder, DATA_placeholder):
        count = 0
        MESSAGE_placeholder.info("Agregando asignaciones al banco de registros...")
        time.sleep(self.controlUnit.tiempo)
        for instr in programa:
            if "=" in instr:  # Asignación al banco de registros
                count += 1
                var, val = instr.split(" = ")
                var2 = ""
                for i in var:
                    if i != " ":
                        var2+=i
                value = int(val.strip())
                MESSAGE_placeholder.info(f"Unidad de control decodificando la instrucción {var} = {val}")
                time.sleep(self.controlUnit.tiempo)
                encoded = self.encode_assignment(var2.strip(), value)
                MESSAGE_placeholder.success(f"Instrucción decodificada con éxito: {encoded}")
                CONTROL_UNIT_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>CONTROL UNIT: {encoded}</strong></p>""", unsafe_allow_html=True)
                time.sleep(self.controlUnit.tiempo)
                CONTROL_UNIT_placeholder.write(f"###### _CONTROL UNIT_: {encoded}")
                encoded_val = self.int_to_binary(value)
                MESSAGE_placeholder.info(f"Agregando la instrucción {var} = {val} al banco de registros")
                time.sleep(self.controlUnit.tiempo)
                self.memory.dataBus.sendData(encoded, "CONTROL UNIT", "REGISTERS", MESSAGE_placeholder)
                CONTROL_UNIT_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>CONTROL UNIT: {encoded}</strong></p>""", unsafe_allow_html=True)
                time.sleep(self.controlUnit.tiempo)
                CONTROL_UNIT_placeholder.write(f"###### _CONTROL UNIT_: {encoded}")
                DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)
                time.sleep(self.controlUnit.tiempo)
                DATA_placeholder.write(f"###### _Bus de Datos_: {self.memory.dataBus.getData()}")
                self.registerBank.addRegister(var2, encoded_val)  # Guardar en el banco de registros
                REG_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>REG: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)
                self.memory.dataBus.receiveData(encoded, "CONTROL UNIT", "REGISTERS", MESSAGE_placeholder)
                time.sleep(self.controlUnit.tiempo)
                REG_placeholder.write(f"###### _REG_: {self.memory.dataBus.getData()}")
                mostrar_registros(self.registerBank.registers, BANK_REGISTER_placeholder)
                MESSAGE_placeholder.success(f"Se ha agregado con éxito {instr} al banco de registros")
                time.sleep(self.controlUnit.tiempo)
        return count
    
    def encode_instructions_zero(self, programa, MESSAGE_placeholder, CONTROL_UNIT_placeholder):
        MESSAGE_placeholder.info("Decodificando instrucciones a nivel máquina...")
        time.sleep(self.controlUnit.tiempo)
        # Crear una pila para las instrucciones de cero direcciones
        pila = deque()
        for instr in programa:
            if "=" not in instr:  # Instrucciones a memoria
                parts = instr.split()
                operation = parts[0]
                if len(parts) > 1:
                    operands = parts[1]  # Operandos como strings
                else:
                    operands = None
                MESSAGE_placeholder.info(f"Unidad de control decodificando la instrucción {instr}")
                time.sleep(self.controlUnit.tiempo)
                encoded = self.controlUnit.encode_zero_address_instruction(operation, operands, pila)
                MESSAGE_placeholder.success(f"Instrucción decodificada con éxito {instr}: {encoded}")
                CONTROL_UNIT_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>CONTROL UNIT: {encoded}</strong></p>""", unsafe_allow_html=True)
                time.sleep(self.controlUnit.tiempo)
                CONTROL_UNIT_placeholder.write(f"###### _CONTROL UNIT_: {encoded}")
        
    def load_program_zero(self, programa, REG_placeholder, DIR_placeholder, DAT_placeholder, MESSAGE_placeholder, PC_placeholder, MBR_placeholder, MAR_placeholder, ALU_placeholder, CONTROL_UNIT_placeholder, DATA_placeholder, ADDRESS_placeholder, MEMORY_placeholder):
        """
        Procesa y carga las instrucciones y asignaciones en memoria.
        """
        
        MESSAGE_placeholder.info("Cargando el programa a la memoria...")
        time.sleep(self.controlUnit.tiempo)
        for instr in programa:
            if "=" not in instr:  # Instrucciones a memoria
                parts = instr.split()
                operation = parts[0]
                if len(parts) > 1:
                    operands = parts[1]  # Operandos como strings
                else:
                    operands = None
                encoded = self.controlUnit.encode_zero_address_instruction(operation, operands, self.pila)
                CONTROL_UNIT_placeholder.write(f"###### _CONTROL UNIT_: {encoded}")
                self.memory.addressBus.sendAddress(self.registerBank.PC.getValue(), "PC", "MAR", MESSAGE_placeholder)
                PC_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>PC: {self.registerBank.PC.getValue()}</strong></p>""", unsafe_allow_html=True)
                time.sleep(self.controlUnit.tiempo)
                PC_placeholder.write(f"###### _PC_: {self.registerBank.PC.getValue()}")
                ADDRESS_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Direcciones: {self.memory.addressBus.getAddress()}</strong></p>""", unsafe_allow_html=True)
                time.sleep(self.controlUnit.tiempo)
                ADDRESS_placeholder.write(f"###### _Bus de Direcciones_: {self.memory.addressBus.getAddress()}")
                self.registerBank.MAR.setValue(self.memory.addressBus.getAddress())
                MAR_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>MAR: {self.memory.addressBus.getAddress()}</strong></p>""", unsafe_allow_html=True)
                self.memory.addressBus.receiveAddress(self.registerBank.PC.getValue(), "PC", "MAR", MESSAGE_placeholder)
                time.sleep(self.controlUnit.tiempo)
                MAR_placeholder.write(f"###### _MAR_: {self.registerBank.MAR.getValue()}")
                
                if parts[0] == "PUSH":
                    if self.registerBank.getRegister(parts[1]):
                        self.memory.dataBus.sendData(encoded, "REGISTERS", "MBR", MESSAGE_placeholder)
                        REG_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>REG: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)
                        time.sleep(self.controlUnit.tiempo)
                        REG_placeholder.write(f"###### _REG_: {encoded}")
                        DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)
                        time.sleep(self.controlUnit.tiempo)
                        DATA_placeholder.write(f"###### _Bus de Datos_: {self.memory.dataBus.getData()}")
                        self.registerBank.MBR.setValue(self.memory.dataBus.getData())
                        MBR_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>MBR: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)
                        self.memory.dataBus.receiveData(encoded, "REGISTERS", "MBR", MESSAGE_placeholder)
                        time.sleep(self.controlUnit.tiempo)
                        MBR_placeholder.write(f"###### _MBR_: {self.registerBank.MBR.getValue()}")
                else:
                    self.memory.dataBus.sendData(encoded, "CONTROL UNIT", "MBR", MESSAGE_placeholder)
                    CONTROL_UNIT_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>CONTOL UNIT: {encoded}</strong></p>""", unsafe_allow_html=True)
                    time.sleep(self.controlUnit.tiempo)
                    CONTROL_UNIT_placeholder.write(f"###### _CONTROL UNIT_: {encoded}")
                    DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)
                    time.sleep(self.controlUnit.tiempo)
                    DATA_placeholder.write(f"###### _Bus de Datos_: {self.memory.dataBus.getData()}")
                    self.registerBank.MBR.setValue(self.memory.dataBus.getData())
                    MBR_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>MBR: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)
                    self.memory.dataBus.receiveData(encoded, "CONTROL UNIT", "MBR", MESSAGE_placeholder)
                    time.sleep(self.controlUnit.tiempo)
                    MBR_placeholder.write(f"###### _MBR_: {self.registerBank.MBR.getValue()}")
                    
                self.memory.addressBus.sendAddress(self.registerBank.MAR.getValue(), "MAR", "MEMORY", MESSAGE_placeholder)
                MAR_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>MAR: {self.memory.addressBus.getAddress()}</strong></p>""", unsafe_allow_html=True)
                time.sleep(self.controlUnit.tiempo)
                MAR_placeholder.write(f"###### _MAR_: {self.registerBank.MAR.getValue()}")
                ADDRESS_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Direcciones: {self.memory.addressBus.getAddress()}</strong></p>""", unsafe_allow_html=True)
                time.sleep(self.controlUnit.tiempo)
                ADDRESS_placeholder.write(f"###### _Bus de Direcciones_: {self.memory.addressBus.getAddress()}")
                DIR_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>DIR: {self.memory.addressBus.getAddress()}</strong></p>""", unsafe_allow_html=True)
                MAR = self.memory.addressBus.getAddress()
                self.memory.addressBus.receiveAddress(MAR, "MAR", "MEMORY", MESSAGE_placeholder)
                time.sleep(self.controlUnit.tiempo)
                DIR_placeholder.write(f"###### _DIR_: {self.registerBank.MAR.getValue()}")
                
                self.memory.dataBus.sendData(self.registerBank.MBR.getValue(), "MBR", "MEMORY", MESSAGE_placeholder)
                MBR_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>MBR: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)
                time.sleep(self.controlUnit.tiempo)
                MBR_placeholder.write(f"###### _MBR_: {self.registerBank.MBR.getValue()}")
                DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)
                time.sleep(self.controlUnit.tiempo)
                DATA_placeholder.write(f"###### _Bus de datos_: {self.registerBank.MBR.getValue()}")
                MBR = self.memory.dataBus.getData()
                DAT_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>DAT: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)
                self.memory.dataBus.receiveData(self.registerBank.MBR.getValue(), "MBR", "MEMORY", MESSAGE_placeholder)
                time.sleep(self.controlUnit.tiempo)
                DAT_placeholder.write(f"###### _DAT_: {self.registerBank.MBR.getValue()}")
                
                MESSAGE_placeholder.info(f"Escribiendo {MBR} en la posición de memoria {int(MAR, 2)}")
                time.sleep(self.controlUnit.tiempo)
                self.memory.write(int(MAR, 2), MBR)
                mostrar_memoria(self.memory.memoryArray, MEMORY_placeholder)
                MESSAGE_placeholder.success(f"Se ha escrito {MBR} en la posición de memoria {int(MAR, 2)} con éxito")
                time.sleep(self.controlUnit.tiempo)
                
                MESSAGE_placeholder.info("Aumentando el contador del programa para posicionar las instrucciones en memoria...")
                self.memory.dataBus.sendData(self.registerBank.PC.getValue(), "PC", "ALU", MESSAGE_placeholder)
                PC_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>PC: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)
                time.sleep(self.controlUnit.tiempo)
                PC_placeholder.write(f"###### _PC_: {self.registerBank.PC.getValue()}")
                DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)
                time.sleep(self.controlUnit.tiempo)
                DATA_placeholder.write(f"###### _Bus de Datos_: {self.memory.dataBus.getData()}")
                ALU_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>ALU: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)
                self.memory.dataBus.receiveData(self.registerBank.PC.getValue(), "PC", "ALU", MESSAGE_placeholder)
                time.sleep(self.controlUnit.tiempo)
                ALU_placeholder.write(f"###### _ALU_: {self.registerBank.PC.getValue()}")
                
                
                MESSAGE_placeholder.info("Realizando operación ADD en la ALU")
                time.sleep(self.controlUnit.tiempo)
                self.controlUnit.alu.add(1,int(self.registerBank.PC.getValue(),2),1,1)
                ALU_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>ALU: {self.int_to_binary(int(self.controlUnit.alu.getResult()),32)}</strong></p>""", unsafe_allow_html=True)
                MESSAGE_placeholder.success(f"Operación ADD realizada con éxito: {self.int_to_binary(int(self.controlUnit.alu.getResult()),32)}")
                time.sleep(self.controlUnit.tiempo)
                ALU_placeholder.write(f"###### _ALU_: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}")
                time.sleep(1)
                self.memory.dataBus.sendData(self.int_to_binary(self.controlUnit.alu.getResult(),32), "ALU", "PC", MESSAGE_placeholder)
                ALU_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>ALU: {self.int_to_binary(int(self.controlUnit.alu.getResult()),32)}</strong></p>""", unsafe_allow_html=True)
                time.sleep(self.controlUnit.tiempo)
                ALU_placeholder.write(f"###### _ALU_: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}")
                time.sleep(self.controlUnit.tiempo)
                DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {self.int_to_binary(int(self.controlUnit.alu.getResult()),32)}</strong></p>""", unsafe_allow_html=True)
                time.sleep(self.controlUnit.tiempo)
                DATA_placeholder.write(f"###### _Bus de Datos_: {self.memory.dataBus.getData()}")
                self.registerBank.PC.setValue(self.int_to_binary(int(self.controlUnit.alu.getResult()),32))
                time.sleep(self.controlUnit.tiempo)
                PC_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>PC: {self.int_to_binary(int(self.controlUnit.alu.getResult()),32)}</strong></p>""", unsafe_allow_html=True)
                self.memory.dataBus.receiveData(self.int_to_binary(self.controlUnit.alu.getResult(),32), "ALU", "PC", MESSAGE_placeholder)
                time.sleep(self.controlUnit.tiempo)
                PC_placeholder.write(f"###### _PC_: {self.registerBank.PC.getValue()}")
    
    def int_to_binary(self, value, bits=12):
        """
        Convierte un entero a su representación binaria con bit de signo.
        
        Parámetros:
        - value: El número entero a convertir.
        - bits: Número total de bits (incluido el bit de signo).
        
        Retorna:
        - Cadena binaria con la longitud especificada.
        
        Ejemplo:
        - int_to_binary(5, 12) -> '000000000101'  (Positivo)
        - int_to_binary(-5, 12) -> '100000000101' (Negativo)
        """
        if bits < 2:
            raise ValueError("La cantidad de bits debe ser al menos 2 para incluir el bit de signo.")

        # Determinar el signo y convertir el valor absoluto a binario
        sign_bit = '0' if value >= 0 else '1'
        abs_value = abs(int(value))

        # Convertir el valor absoluto a binario
        binary_value = f"{abs_value:0{bits-1}b}"  # bits-1 para dejar espacio al bit de signo

        # Validar que el valor cabe en el número de bits proporcionado
        if len(binary_value) > (bits - 1):
            raise ValueError(f"El valor {value} excede el rango permitido para {bits} bits.")

        # Combinar el bit de signo y el valor binario
        return sign_bit + binary_value

    def encode_assignment(self, variable, value):
        """
        Codifica una asignación en formato binario:
        - 8 bits para el codop (asignación)
        - 12 bits para la letra del registro
        - 1 bit para el signo
        - 11 bits para el número
        """
        codop = self.controlUnit.asignaciones.get(variable + " = ", "00000000")
        sign_bit = '0' if value >= 0 else '1'
        value_binary = f"{abs(value):011b}"
        return codop + self.controlUnit.registros_binarios[variable] + sign_bit + value_binary

    def execute(self, codop, operand1, operand2, REG_placeholder, REG_BANK_placeholder, ALU_placeholder, MESSAGE_placeholder, DATA_placeholder, OUTPUT_placeholder):
        direction = self.controlUnit.identify_directions(codop)
        if direction == 0:
            self.execute_zero(codop, operand1, operand2, REG_placeholder, REG_BANK_placeholder, ALU_placeholder, MESSAGE_placeholder, DATA_placeholder, OUTPUT_placeholder)
                
    def execute_zero(self, codop, operand1, operand2, REG_placeholder, REG_BANK_placeholder, ALU_placeholder, MESSAGE_placeholder, DATA_placeholder, OUTPUT_placeholder):
        
        if str(codop) == "00000001":
            for key, value in self.controlUnit.registros_binarios.items():
                if value == operand1:
                    self.pila.append(self.registerBank.getRegister(key))
        elif str(codop) == "00000010":
            sign1 = -1 if self.pila[0][0] == '1' else 1  # Determinar el signo del primer operando
            sign2 = -1 if self.pila[1][0] == '1' else 1  # Determinar el signo del segundo operando
            
            self.memory.dataBus.sendData(codop+self.pila[0][1:]+self.pila[1][1:], "REGISTER BANK", "ALU", MESSAGE_placeholder)
            REG_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>REG: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            REG_placeholder.write(f"###### _REG_: {self.memory.dataBus.getData()}")
            DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            DATA_placeholder.write(f"###### _Bus de Datos_: {self.memory.dataBus.getData()}")
            ALU_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>ALU: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)
            self.memory.dataBus.receiveData(codop+self.pila[0][1:]+self.pila[1][1:], "REGISTER BANK", "ALU", MESSAGE_placeholder)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _ALU_: {self.memory.dataBus.getData()}")
            operand01 = int(self.pila[0][1:], 2)  # Convertir el valor binario (sin bit de signo) a entero
            operand02 = int(self.pila[1][1:], 2)  # Convertir el segundo operando
            
            MESSAGE_placeholder.info("Procesando datos en la ALU")
            time.sleep(self.controlUnit.tiempo)
            self.controlUnit.alu.add(sign1, operand01, sign2, operand02)
            ALU_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>ALU: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}</strong></p>""", unsafe_allow_html=True)
            MESSAGE_placeholder.success("Datos procesados exitosamente")
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _ALU_: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}")
            
            self.pila.pop()
            self.pila.pop()
            self.pila.append(self.int_to_binary(int(self.controlUnit.alu.getResult())))
            
            self.memory.dataBus.sendData(codop+operand1+self.pila[0][1:], "ALU", "REGISTER BANK", MESSAGE_placeholder)
            ALU_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>ALU: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _ALU_: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}")
            DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _Bus de Datos_: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}")
            self.memory.dataBus.receiveData(codop+operand1+self.pila[0][1:], "ALU", "REGISTER BANK", MESSAGE_placeholder)
            REG_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>REG: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            REG_placeholder.write(f"###### _REG_: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}")
            time.sleep(1)
            
        elif str(codop) == "00000011":
            sign1 = -1 if self.pila[0][0] == '1' else 1  # Determinar el signo del primer operando
            sign2 = -1 if self.pila[1][0] == '1' else 1  # Determinar el signo del segundo operando
            
            self.memory.dataBus.sendData(codop+self.pila[0][1:]+self.pila[1][1:], "REGISTER BANK", "ALU", MESSAGE_placeholder)
            REG_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>REG: {codop+self.pila[0][1:]+self.pila[1][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            REG_placeholder.write(f"###### _REG_: {codop+self.pila[0][1:]+self.pila[1][1:]}")
            DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {codop+self.pila[0][1:]+self.pila[1][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _Bus de Datos_: {codop+self.pila[0][1:]+self.pila[1][1:]}")
            self.memory.dataBus.receiveData(codop+self.pila[0][1:]+self.pila[1][1:], "REGISTER BANK", "ALU", MESSAGE_placeholder)
            ALU_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>ALU: {codop+self.pila[0][1:]+self.pila[1][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _ALU_: {codop+self.pila[0][1:]+self.pila[1][1:]}")
            operand01 = int(self.pila[0][1:], 2)  # Convertir el valor binario (sin bit de signo) a entero
            operand02 = int(self.pila[1][1:], 2)  # Convertir el segundo operando
            
            MESSAGE_placeholder.info("Procesando datos en la ALU")
            time.sleep(self.controlUnit.tiempo)
            self.controlUnit.alu.sub(sign1, operand01, sign2, operand02)
            ALU_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>ALU: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}</strong></p>""", unsafe_allow_html=True)
            MESSAGE_placeholder.success("Datos procesados exitosamente")
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _ALU_: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}")
            
            self.pila.pop()
            self.pila.pop()
            self.pila.append(self.int_to_binary(int(self.controlUnit.alu.getResult())))
            
            self.memory.dataBus.sendData(codop+operand1+self.pila[0][1:], "ALU", "REGISTER BANK", MESSAGE_placeholder)
            ALU_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>ALU: {codop+operand1+self.pila[0][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _ALU_: {codop+operand1+self.pila[0][1:]}")
            DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {codop+operand1+self.pila[0][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _Bus de Datos_: {codop+operand1+self.pila[0][1:]}")
            self.memory.dataBus.receiveData(codop+operand1+self.pila[0][1:], "REGISTER BANK", "ALU", MESSAGE_placeholder)
            REG_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>REG: {codop+operand1+self.pila[0][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            REG_placeholder.write(f"###### _REG_: {codop+operand1+self.pila[0][1:]}")
            
            
        elif str(codop) == "00000100":
            sign1 = -1 if self.pila[0][0] == '1' else 1  # Determinar el signo del primer operando
            sign2 = -1 if self.pila[1][0] == '1' else 1  # Determinar el signo del segundo operando
            
            self.memory.dataBus.sendData(codop+self.pila[0][1:]+self.pila[1][1:], "REGISTER BANK", "ALU", MESSAGE_placeholder)
            REG_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>REG: {codop+self.pila[0][1:]+self.pila[1][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            REG_placeholder.write(f"###### _REG_: {codop+self.pila[0][1:]+self.pila[1][1:]}")
            DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {codop+self.pila[0][1:]+self.pila[1][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _Bus de Datos_: {codop+self.pila[0][1:]+self.pila[1][1:]}")
            self.memory.dataBus.receiveData(codop+self.pila[0][1:]+self.pila[1][1:], "REGISTER BANK", "ALU", MESSAGE_placeholder)
            ALU_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>ALU: {codop+self.pila[0][1:]+self.pila[1][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _ALU_: {codop+self.pila[0][1:]+self.pila[1][1:]}")
            operand01 = int(self.pila[0][1:], 2)  # Convertir el valor binario (sin bit de signo) a entero
            operand02 = int(self.pila[1][1:], 2)  # Convertir el segundo operando
            
            MESSAGE_placeholder.info("Procesando datos en la ALU")
            time.sleep(self.controlUnit.tiempo)
            self.controlUnit.alu.mul(sign1, operand01, sign2, operand02)
            ALU_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>ALU: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}</strong></p>""", unsafe_allow_html=True)
            MESSAGE_placeholder.success("Datos procesados exitosamente")
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _ALU_: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}")
            
            self.pila.pop()
            self.pila.pop()
            self.pila.append(self.int_to_binary(int(self.controlUnit.alu.getResult())))
            print(int(self.controlUnit.alu.getResult()))
            
            self.memory.dataBus.sendData(codop+operand1+self.pila[0][1:], "ALU", "REGISTER BANK", MESSAGE_placeholder)
            ALU_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>ALU: {codop+operand1+self.pila[0][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _ALU_: {codop+operand1+self.pila[0][1:]}")
            DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {codop+operand1+self.pila[0][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _Bus de Datos_: {codop+operand1+self.pila[0][1:]}")
            self.memory.dataBus.receiveData(codop+operand1+self.pila[0][1:], "REGISTER BANK", "ALU", MESSAGE_placeholder)
            REG_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>REG: {codop+operand1+self.pila[0][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            REG_placeholder.write(f"###### _REG_: {codop+operand1+self.pila[0][1:]}")
            
        elif str(codop) == "00000101":
            sign1 = -1 if self.pila[0][0] == '1' else 1  # Determinar el signo del primer operando
            sign2 = -1 if self.pila[1][0] == '1' else 1  # Determinar el signo del segundo operando

            self.memory.dataBus.sendData(codop+self.pila[0][1:]+self.pila[1][1:], "REGISTER BANK", "ALU", MESSAGE_placeholder)
            REG_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>REG: {codop+self.pila[0][1:]+self.pila[1][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            REG_placeholder.write(f"###### _REG_: {codop+self.pila[0][1:]+self.pila[1][1:]}")
            DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {codop+self.pila[0][1:]+self.pila[1][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _Bus de Datos_: {codop+self.pila[0][1:]+self.pila[1][1:]}")
            self.memory.dataBus.receiveData(codop+self.pila[0][1:]+self.pila[1][1:], "REGISTER BANK", "ALU", MESSAGE_placeholder)
            ALU_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>ALU: {codop+self.pila[0][1:]+self.pila[1][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _ALU_: {codop+self.pila[0][1:]+self.pila[1][1:]}")
            operand01 = int(self.pila[0][1:], 2)  # Convertir el valor binario (sin bit de signo) a entero
            operand02 = int(self.pila[1][1:], 2)  # Convertir el segundo operando
            
            MESSAGE_placeholder.info("Procesando datos en la ALU")
            time.sleep(self.controlUnit.tiempo)
            self.controlUnit.alu.div(sign1, operand01, sign2, operand02)
            ALU_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>ALU: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}</strong></p>""", unsafe_allow_html=True)
            MESSAGE_placeholder.success("Datos procesados exitosamente")
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _ALU_: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}")
            
            self.pila.pop()
            self.pila.pop()
            self.pila.append(self.int_to_binary(int(self.controlUnit.alu.getResult())))
            self.memory.dataBus.sendData(codop+operand1+self.pila[0][1:], "ALU", "REGISTER BANK", MESSAGE_placeholder)
            ALU_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>ALU: {codop+operand1+self.pila[0][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _ALU_: {codop+operand1+self.pila[0][1:]}")
            DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {codop+operand1+self.pila[0][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _Bus de Datos_: {codop+operand1+self.pila[0][1:]}")
            self.memory.dataBus.receiveData(codop+operand1+self.pila[0][1:], "REGISTER BANK", "ALU", MESSAGE_placeholder)
            REG_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>REG: {codop+operand1+self.pila[0][1:]}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            REG_placeholder.write(f"###### _REG_: {codop+operand1+self.pila[0][1:]}")
            
        elif str(codop) == "00000110":
            MESSAGE_placeholder.info(f"Agregando {self.pila[0]} al banco de registros")
            time.sleep(self.controlUnit.tiempo)
            
            self.memory.dataBus.sendData(self.int_to_binary(self.controlUnit.alu.getResult(), 32), "ALU", "REGISTER BANK", MESSAGE_placeholder)
            ALU_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>ALU: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _ALU_: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}")
            DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            ALU_placeholder.write(f"###### _Bus de Datos_: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}")
            self.memory.dataBus.receiveData(codop+operand1+self.pila[0][1:], "REGISTER BANK", "ALU", MESSAGE_placeholder)
            REG_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>REG: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}</strong></p>""", unsafe_allow_html=True)
            time.sleep(self.controlUnit.tiempo)
            REG_placeholder.write(f"###### _REG_: {self.int_to_binary(self.controlUnit.alu.getResult(), 32)}")
            self.registerBank.addRegister(self.controlUnit.identify_key(operand1), self.pila[0])
            mostrar_registros(self.registerBank.registers, REG_BANK_placeholder)
            print(self.registerBank.getRegister(self.controlUnit.identify_key(operand1)))
            self.pila.pop()
            
            salida = self.registerBank.registers[len(self.registerBank.registers)-1]
            OUTPUT_placeholder.text_area("Salida respecto a la ejecución del programa", self.controlUnit.identify_key(operand1) + " = " + self.pila[0], disabled=True)
            
        elif str(codop) == "11111111":
            self.registerBank.PC.setValue("00000000000000000000000000000000")
        
        print(self.pila)
        
    def float_a_binario_12bits(self, numero):
        """
        Convierte un número float a una representación binaria de 12 bits con signo.
        
        :param numero: Número float a convertir.
        :return: Cadena binaria de 12 bits.
        :raises ValueError: Si el número no puede representarse en 12 bits.
        """
        if numero < -2 or numero >= 2:
            raise ValueError(f"El número {numero} no puede representarse en 12 bits con esta lógica.")

        # Determinar el bit de signo
        signo = '1' if numero < 0 else '0'
        numero = abs(numero)

        # Separar parte entera y fraccionaria
        parte_entera = int(numero)
        parte_fraccionaria = numero - parte_entera

        # Convertir parte entera a binario
        bin_entera = bin(parte_entera)[2:]  # Quitar el prefijo '0b'

        # Convertir parte fraccionaria a binario (hasta completar 11 bits totales)
        bin_fraccionaria = ""
        while parte_fraccionaria > 0 and len(bin_entera + bin_fraccionaria) < 11:
            parte_fraccionaria *= 2
            bit = int(parte_fraccionaria)
            bin_fraccionaria += str(bit)
            parte_fraccionaria -= bit

        # Combinar parte entera y fraccionaria
        binario = bin_entera + bin_fraccionaria

        # Ajustar a 11 bits (completa con ceros si es necesario)
        if len(binario) < 11:
            binario = binario.ljust(11, '0')  # Completar con ceros a la derecha
        elif len(binario) > 11:
            binario = binario[:11]  # Truncar si es más largo

        # Agregar el bit de signo y retornar
        return signo + binario
