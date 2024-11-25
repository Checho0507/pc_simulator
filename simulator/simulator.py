from collections import deque
import time
from simulator.bus.address_bus import AddressBus
from simulator.bus.control_bus import ControlBus
from simulator.bus.data_bus import DataBus
from simulator.control_unit import ControlUnit
from simulator.memory import Memory
from simulator.register_bank import RegisterBank

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
        self.controlUnit = ControlUnit(self.dataBus, self.addressBus, self.controlBus, self.registerBank, self.memory)

    def executeProgram(self):
        # Ejemplo de programa para instrucciones de cero direcciones
        programs = {
            0:[
            "A = -1", "C = 2", "D = 3", "E = 4", "PUSH D", "PUSH E", 
            "SUB", "PUSH A", "MUL", "POP X", "PUSH A", "PUSH C", 
            "MUL", "PUSH X", "DIV", "POP Z", "END"
            ]
        }

        print("Loading zero-address instructions:")
        count = self.add_asigns(programs[0])
        self.encode_instructions_zero(programs[0])
        self.load_program_zero(programs[0])
        self.registerBank.PC.setValue("00000000000000000000000000000000")
        self.pila.clear()
        for i in range(len(programs[0])-count):
            self.controlBus.sendControlSignal("FETCH")
            self.controlUnit.fetch()
            self.controlBus.receiveControlSignal()
            
            self.controlBus.sendControlSignal("DECODE")
            codop, operand1, operand2 = self.controlUnit.decode()
            self.controlBus.receiveControlSignal()
            
            self.controlBus.sendControlSignal("EXECUTE")
            self.execute(codop, operand1, operand2)
            self.controlBus.receiveControlSignal()
            
            self.controlUnit.value_operation=self.int_to_binary(self.controlUnit.alu.getResult())
            self.controlUnit.alu.add(1,int(self.registerBank.PC.getValue(),2),1,1)
            
            self.registerBank.PC.setValue(self.int_to_binary(self.controlUnit.alu.getResult(),32))
        
    def add_asigns(self, instructions):
        print("Agregando asignaciones al banco de registros")
        count = 0
        for instr in instructions:
            if "=" in instr:  # Asignación al banco de registros
                count += 1
                var, val = instr.split(" = ")
                value = int(val.strip())
                encoded = self.encode_assignment(var.strip(), value)
                print(f"Encoded assignment {instr}: {encoded}")
                encoded_val = self.int_to_binary(value)
                self.registerBank.addRegister(var, encoded_val)  # Guardar en el banco de registros
        return count
    
    def encode_instructions_zero(self, instructions):
        print("Codificando instrucción a nivel máquina:")
        # Crear una pila para las instrucciones de cero direcciones
        pila = deque()
        for instr in instructions:
            if "=" not in instr:  # Instrucciones a memoria
                parts = instr.split()
                operation = parts[0]
                if len(parts) > 1:
                    operands = parts[1]  # Operandos como strings
                else:
                    operands = None
                encoded = self.controlUnit.encode_zero_address_instruction(operation, operands, pila)
                print(f"Encoded instruction {instr}: {encoded}")
        
    def load_program_zero(self, instructions):
        """
        Procesa y carga las instrucciones y asignaciones en memoria.
        """
        
        print("Cargando el programa a la memoria:")
        for instr in instructions:
            if "=" not in instr:  # Instrucciones a memoria
                parts = instr.split()
                operation = parts[0]
                if len(parts) > 1:
                    operands = parts[1]  # Operandos como strings
                else:
                    operands = None
                encoded = self.controlUnit.encode_zero_address_instruction(operation, operands, self.pila)
                self.memory.addressBus.sendAddress(self.registerBank.PC.getValue(), "PC", "MAR")
                self.registerBank.MAR.setValue(self.memory.addressBus.getAddress())
                self.memory.addressBus.receiveAddress(self.registerBank.PC.getValue(), "PC", "MAR")
                
                self.memory.dataBus.sendData(encoded, "CONTROL UNIT", "MBR")
                self.registerBank.MBR.setValue(self.memory.dataBus.getData())
                self.memory.dataBus.receiveData(encoded, "CONTROL UNIT", "MBR")
                
                self.memory.addressBus.sendAddress(self.registerBank.MAR.getValue(), "MAR", "MEMORY")
                MAR = self.memory.addressBus.getAddress()
                self.memory.addressBus.receiveAddress(self.registerBank.MAR.getValue(), "MAR", "MEMORY")
                
                self.memory.dataBus.sendData(self.registerBank.MBR.getValue(), "MBR", "MEMORY")
                MBR = self.memory.dataBus.getData()
                self.memory.dataBus.receiveData(self.registerBank.MBR.getValue(), "MBR", "MEMORY")
                
                self.memory.write(int(MAR, 2), MBR)
                
                self.controlUnit.alu.add(1,int(self.registerBank.PC.getValue(),2),1,1)
                self.registerBank.PC.setValue(self.int_to_binary(int(self.controlUnit.alu.getResult()),32))
    
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
        abs_value = abs(value)

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

    def execute(self, codop, operand1, operand2):
        direction = self.controlUnit.identify_directions(codop)
        if direction == 0:
            self.execute_zero(codop, operand1, operand2)
                
    def execute_zero(self, codop, operand1, operand2):
        
        if str(codop) == "00000001":
            self.pila.append(operand2)
        elif str(codop) == "00000010":
            sign1 = -1 if self.pila[0][0] == '1' else 1  # Determinar el signo del primer operando
            sign2 = -1 if self.pila[1][0] == '1' else 1  # Determinar el signo del segundo operando

            operand1 = sign1 * int(self.pila[0][1:], 2)  # Convertir el valor binario (sin bit de signo) a entero
            operand2 = sign2 * int(self.pila[1][1:], 2)  # Convertir el segundo operando
            
            self.alu.add(sign1, operand1, sign2, operand2)
            self.pila.pop()
            self.pila.pop()
            self.pila.append(self.int_to_binary(int(self.alu.getResult())))
            
        elif str(codop) == "00000011":
            sign1 = -1 if self.pila[0][0] == '1' else 1  # Determinar el signo del primer operando
            sign2 = -1 if self.pila[1][0] == '1' else 1  # Determinar el signo del segundo operando

            operand1 = sign1 * int(self.pila[0][1:], 2)  # Convertir el valor binario (sin bit de signo) a entero
            operand2 = sign2 * int(self.pila[1][1:], 2)  # Convertir el segundo operando
            
            self.controlUnit.alu.sub(sign1, operand1, sign2, operand2)
            self.pila.pop()
            self.pila.pop()
            self.pila.append(self.int_to_binary(int(self.controlUnit.alu.getResult())))
        elif str(codop) == "00000100":
            sign1 = -1 if self.pila[0][0] == '1' else 1  # Determinar el signo del primer operando
            sign2 = -1 if self.pila[1][0] == '1' else 1  # Determinar el signo del segundo operando

            operand1 = sign1 * int(self.pila[0][1:], 2)  # Convertir el valor binario (sin bit de signo) a entero
            operand2 = sign2 * int(self.pila[1][1:], 2)  # Convertir el segundo operando
            
            self.controlUnit.alu.mul(sign1, operand1, sign2, operand2)
            self.pila.pop()
            self.pila.pop()
            self.pila.append(self.int_to_binary(int(self.controlUnit.alu.getResult())))
            print(int(self.controlUnit.alu.getResult()))
        elif str(codop) == "00000101":
            sign1 = -1 if self.pila[0][0] == '1' else 1  # Determinar el signo del primer operando
            sign2 = -1 if self.pila[1][0] == '1' else 1  # Determinar el signo del segundo operando

            operand1 = sign1 * int(self.pila[0][1:], 2)  # Convertir el valor binario (sin bit de signo) a entero
            operand2 = sign2 * int(self.pila[1][1:], 2)  # Convertir el segundo operando
            
            self.controlUnit.alu.div(sign1, operand1, sign2, operand2)
            self.pila.pop()
            self.pila.pop()
            self.pila.append(self.int_to_binary(int(self.controlUnit.alu.getResult())))
        elif str(codop) == "00000110":
            self.registerBank.addRegister(self.controlUnit.identify_key(operand1), self.pila[0])
            self.pila.pop()
        elif str(codop) == "11111111":
            self.registerBank.PC.setValue("00000000000000000000000000000000")
        
        print(self.pila)