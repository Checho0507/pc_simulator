from collections import deque
import time
from simulator.alu import ALU

class ControlUnit:
    def __init__(self, dataBus, addressBus, controlBus, registerBank, memory):
        self.tiempo = 0
        self.alu = ALU()
        self.pila = deque()
        self.value_operation = ""
        self.dataBus = dataBus
        self.addressBus = addressBus
        self.controlBus = controlBus
        self.registerBank = registerBank
        self.memory = memory

        # Diccionarios para instrucciones
        self.instrucciones_binarias_cero = {
            'PUSH': '00000001',
            'ADD': '00000010',
            'SUB': '00000011',
            'MUL': '00000100',
            'DIV': '00000101',
            'POP': '00000110',
            'END': '11111111'
        }

        self.instrucciones_binarias_una = {
            'LOAD': '00000111',
            'ADD': '00001000',
            'SUB': '00001001',
            'MUL': '00001010',
            'DIV': '00001011',
            'STORE': '00001100',
            'END': '11111111'
        }

        self.instrucciones_binarias_dos = {
            'MOVE': '00001101',
            'ADD': '00001110',
            'SUB': '00001111',
            'MUL': '00010000',
            'DIV': '00010001',
            'END': '11111111'
        }

        self.instrucciones_binarias_tres = {
            'ADD': '00010010',
            'SUB': '00010011',
            'MUL': '00010100',
            'DIV': '00010101',
            'END': '11111111'
        }

        self.asignaciones = {
            'A = ': '00010110',
            'B = ': '00010111',
            'C = ': '00011000',
            'D = ': '00011001',
            'E = ': '00011010',
            'F = ': '00011011',
            'G = ': '00011100',
            'H = ': '00011101',
            'I = ': '00011110',
            'J = ': '00011111',
            'K = ': '00100000',
            'L = ': '00100001',
            'M = ': '00100010',
            'N = ': '00100011',
            'O = ': '00100100',
            'P = ': '00100101',
            'Q = ': '00100110',
            'R = ': '00100111',
            'S = ': '00101000',
            'T = ': '00101001',
            'U = ': '00101010',
            'V = ': '00101011',
            'W = ': '00101100',
            'X = ': '00101101',
            'Y = ': '00101110',
            'Z = ': '00101111',
        }
        
        self.registros_binarios= {
            'A': '000000000001',
            'B': '000000000010',
            'C': '000000000011',
            'D': '000000000100',
            'E': '000000000101',
            'F': '000000000110',
            'G': '000000000111',
            'H': '000000001000',
            'I': '000000001001',
            'J': '000000001010',
            'K': '000000001011',
            'L': '000000001100',
            'M': '000000001101',
            'N': '000000001110',
            'O': '000000001111',
            'P': '000000010000',
            'Q': '000000010001',
            'R': '000000010010',
            'S': '000000010011',
            'T': '000000010100',
            'U': '000000010101',
            'V': '000000010110',
            'W': '000000010111',
            'X': '000000011000',
            'Y': '000000011001',
            'Z': '000000011010'
        }

    def decodeInstruction(self, instruction):
        """
        Decodifica una instrucción dada y determina su tipo.
        """
        print(f"ControlUnit: Decoding instruction: {instruction}")

        # Comprobar en qué grupo está la instrucción
        if instruction in self.instrucciones_binarias_cero:
            binary = self.instrucciones_binarias_cero[instruction]
            print(f"Instruction '{instruction}' (0 operands) -> {binary}")
            return binary

        elif instruction in self.instrucciones_binarias_una:
            binary = self.instrucciones_binarias_una[instruction]
            print(f"Instruction '{instruction}' (1 operand) -> {binary}")
            return binary

        elif instruction in self.instrucciones_binarias_dos:
            binary = self.instrucciones_binarias_dos[instruction]
            print(f"Instruction '{instruction}' (2 operands) -> {binary}")
            return binary

        elif instruction in self.instrucciones_binarias_tres:
            binary = self.instrucciones_binarias_tres[instruction]
            print(f"Instruction '{instruction}' (3 operands) -> {binary}")
            return binary

        else:
            raise ValueError(f"ControlUnit: Unknown instruction '{instruction}'")

    def executeInstruction(self, binaryInstruction):
        """
        Simula la ejecución de una instrucción en formato binario.
        """
        print(f"ControlUnit: Executing binary instruction: {binaryInstruction}")
        # Aquí se implementarían las acciones específicas para la instrucción.

    def controlSignal(self, signal):
        """
        Genera señales de control para coordinar los buses.
        """
        print("ControlUnit: Generating control signals")
        self.controlBus.sendControlSignal(signal)
        
    def fetch(self, MESSAGE_placeholder, DIR_placeholder, DAT_placeholder, PC_placeholder,  IR_placeholder, MAR_placeholder, MBR_placeholder, ADDRESS_placeholder, DATA_placeholder):
        MESSAGE_placeholder.info("Se inicia el fetch instruction...")
        time.sleep(self.tiempo)
        
        self.memory.addressBus.sendAddress(self.registerBank.PC.getValue(), "PC", "MAR", MESSAGE_placeholder)
        PC_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>PC: {self.memory.addressBus.getAddress()}</strong></p>""", unsafe_allow_html=True)   
        time.sleep(self.tiempo)
        PC_placeholder.write(f"###### _PC_: {self.registerBank.PC.getValue()}")
        ADDRESS_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Direcciones: {self.memory.addressBus.getAddress()}</strong></p>""", unsafe_allow_html=True)  
        time.sleep(self.tiempo)
        ADDRESS_placeholder.write(f"###### _Bus de Direcciones_: {self.memory.addressBus.getAddress()}")
        self.registerBank.MAR.setValue(self.memory.addressBus.getAddress())
        MAR_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>MAR: {self.memory.addressBus.getAddress()}</strong></p>""", unsafe_allow_html=True)  
        self.memory.addressBus.receiveAddress(self.registerBank.PC.getValue(), "PC", "MAR", MESSAGE_placeholder)
        time.sleep(self.tiempo)
        MAR_placeholder.write(f"###### _MAR_: {self.registerBank.MAR.getValue()}")
        time.sleep(1)
        
        self.memory.addressBus.sendAddress(self.registerBank.MAR.getValue(), "MAR", "MEMORY", MESSAGE_placeholder)
        MAR_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>MAR: {self.memory.addressBus.getAddress()}</strong></p>""", unsafe_allow_html=True)  
        time.sleep(self.tiempo)
        MAR_placeholder.write(f"###### _MAR_: {self.registerBank.MAR.getValue()}")
        ADDRESS_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Direcciones: {self.memory.addressBus.getAddress()}</strong></p>""", unsafe_allow_html=True)  
        time.sleep(self.tiempo)
        ADDRESS_placeholder.write(f"###### _Bus de Direcciones_: {self.memory.addressBus.getAddress()}")
        data = self.memory.read(int(self.memory.addressBus.getAddress(), 2))
        DIR_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>DIR: {self.memory.addressBus.getAddress()}</strong></p>""", unsafe_allow_html=True)  
        self.memory.addressBus.receiveAddress(self.registerBank.MAR.getValue(), "MAR", "MEMORY", MESSAGE_placeholder)
        time.sleep(self.tiempo)
        DIR_placeholder.write(f"###### _DIR_: {self.memory.addressBus.getAddress()}")
        
        self.memory.dataBus.sendData(data, "MEMORY", "MBR", MESSAGE_placeholder)
        DAT_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>DAT: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)  
        time.sleep(self.tiempo)
        DAT_placeholder.write(f"###### _DAT_: {self.memory.dataBus.getData()}")
        DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)  
        time.sleep(self.tiempo)
        DATA_placeholder.write(f"###### _Bus de Datos_: {self.memory.dataBus.getData()}")
        self.registerBank.MBR.setValue(self.memory.dataBus.data)
        MBR_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>MBR: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)  
        self.memory.dataBus.receiveData(data, "MEMORY", "MBR", MESSAGE_placeholder)
        time.sleep(self.tiempo)
        MBR_placeholder.write(f"###### _MBR_: {self.registerBank.MBR.getValue()}")
        time.sleep(1)
        
        self.memory.dataBus.sendData(self.registerBank.MBR.getValue(), "MBR", "IR", MESSAGE_placeholder)
        MBR_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>MBR: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)  
        time.sleep(self.tiempo)
        MBR_placeholder.write(f"###### _MBR_: {self.registerBank.MBR.getValue()}")
        DATA_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>Bus de Datos: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)  
        time.sleep(self.tiempo)
        DATA_placeholder.write(f"###### _Bus de Datos_: {self.memory.dataBus.getData()}")
        self.registerBank.IR.setValue(self.memory.dataBus.getData())
        IR_placeholder.markdown(f"""<style>.custom-text {{font-size: 15px;color: #37580D;}}</style><p class='custom-text'><strong>IR: {self.memory.dataBus.getData()}</strong></p>""", unsafe_allow_html=True)  
        self.memory.dataBus.receiveData(self.registerBank.MBR.getValue(), "MBR", "IR", MESSAGE_placeholder)
        time.sleep(self.tiempo)
        IR_placeholder.write(f"###### _IR_: {self.registerBank.IR.getValue()}")
        
    def decode(self, MESSAGE_placeholder):
        """
        Decodifica la instrucción almacenada en el IR (Instruction Register).
        """
        
        MESSAGE_placeholder.info("Se inicia el decode instruction...")
        # Obtener el valor del IR (Instruction Register)
        IR = self.registerBank.IR.getValue()

        # Verificar que el IR tenga 32 bits
        if len(IR) != 32:
            raise ValueError(f"Instrucción inválida en IR: {IR}. Se esperaban 32 bits.")

        # Extraer los campos de la instrucción
        codop = IR[:8]          # Los primeros 8 bits son el código de operación
        operand1 = IR[8:20]     # Los siguientes 12 bits son el primer operando
        operand2 = IR[20:32]    # Los últimos 12 bits son el segundo operando

        # Imprimir los valores extraídos (solo para depuración)
        print(f"Codop: {codop}")
        print(f"Operand1: {operand1}")
        print(f"Operand2: {operand2}")

        # Retornar los campos en un diccionario
        return codop, operand1, operand2
            
    def identify_key(self, operand1):
        for key, value in self.registros_binarios.items():
            if operand1 == value:
                return key
            
    def identify_directions(self, codop):
        """
        Identifica el tipo de direccionamiento basado en el codop.
        :param codop: Código de operación en binario (string de 8 bits).
        :return: Número indicando el tipo de direccionamiento (0, 1, 2, 3) o -1 si no se encuentra.
        """
        direccionamientos = {
            0: self.instrucciones_binarias_cero,
            1: self.instrucciones_binarias_una,
            2: self.instrucciones_binarias_dos,
            3: self.instrucciones_binarias_tres
        }

        for direccionamiento, instrucciones in direccionamientos.items():
            if codop in instrucciones.values():
                return direccionamiento

        # Si no se encuentra el codop, devuelve -1
        return -1
            
    def encode_zero_address_instruction(self, instruction, operand, pila):
        """
        Codifica una instrucción de cero direcciones:
        - 8 bits para el codop
        - 1 bit y 11 bits para cada operando (pueden ser 0 si no se usan)
        """
        codop = self.instrucciones_binarias_cero.get(instruction, "00000000")
        operands_binary = ""

        if operand in self.registros_binarios:  # Es un registro
            reg_binary = self.registros_binarios[operand]
            operands_binary += reg_binary
        else:  # Es un valor numérico
            if operand != None:
                sign_bit = '0' if int(operand) >= 0 else '1'
                value_binary = f"{abs(int(operand)):011b}"
                operands_binary += sign_bit + value_binary
        if operand != None:
            while len(operands_binary) < 24:  # Asegurar 23 bits para los tres operandos
                try: 
                    operands_binary += self.registerBank.getRegister(operand)
                    pila.append(self.registerBank.getRegister(operand))
                except:
                    self.registerBank.addRegister(operand, "000000000000")
        else:
            operands_binary = pila[0]+pila[-1]

        return codop + operands_binary[:24]
    
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
        binary_value = f"{abs_value:0{bits-1}}"  # bits-1 para dejar espacio al bit de signo

        # Validar que el valor cabe en el número de bits proporcionado
        if len(binary_value) > (bits - 1):
            raise ValueError(f"El valor {value} excede el rango permitido para {bits} bits.")

        # Combinar el bit de signo y el valor binario
        return sign_bit + binary_value