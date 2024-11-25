from simulator.alu import ALU

class ControlUnit:
    def __init__(self, dataBus, addressBus, controlBus, registerBank, memory):
        self.alu = ALU()
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
        }

        self.instrucciones_binarias_una = {
            'LOAD': '00000111',
            'ADD': '00001000',
            'SUB': '00001001',
            'MUL': '00001010',
            'DIV': '00001011',
            'STORE': '00001100',
        }

        self.instrucciones_binarias_dos = {
            'MOVE': '00001101',
            'ADD': '00001110',
            'SUB': '00001111',
            'MUL': '00010000',
            'DIV': '00010001',
        }

        self.instrucciones_binarias_tres = {
            'ADD': '00010010',
            'SUB': '00010011',
            'MUL': '00010100',
            'DIV': '00010101',
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
        
        self.registros_binarios_cero = {
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
        
    def fetch(self):
        print("Se inicia el fetch instruction:")
        self.memory.addressBus.sendAddress(self.registerBank.PC.getValue(), "PC", "MAR")
        self.registerBank.MAR.setValue(self.memory.addressBus.getAddress())
        self.memory.addressBus.receiveAddress(self.registerBank.PC.getValue(), "PC", "MAR")
        
        self.memory.addressBus.sendAddress(self.registerBank.MAR.getValue(), "MAR", "MEMORY")
        data = self.memory.read(int(self.memory.addressBus.address, 2))
        self.memory.addressBus.receiveAddress(self.registerBank.MAR.getValue(), "MAR", "MEMORY")
        
        self.memory.dataBus.sendData(data, "MEMORY", "MBR")
        self.registerBank.MBR.setValue(self.memory.dataBus.data)
        self.memory.dataBus.receiveData(data, "MEMORY", "MBR")
        
        self.memory.dataBus.sendData(self.registerBank.MBR.getValue(), "MBR", "IR")
        self.registerBank.IR.setValue(self.memory.dataBus.data)
        self.memory.dataBus.receiveData(self.registerBank.MBR.getValue(), "MBR", "IR")
        
    def decode(self):
        """
        Decodifica la instrucción almacenada en el IR (Instruction Register).
        """
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
        return {
            "codop": codop,
            "operand1": operand1,
            "operand2": operand2
        }
            
    def encode_zero_address_instruction(self, instruction, operand, pila):
        """
        Codifica una instrucción de cero direcciones:
        - 8 bits para el codop
        - 1 bit y 11 bits para cada operando (pueden ser 0 si no se usan)
        """
        codop = self.instrucciones_binarias_cero.get(instruction, "00000000")
        operands_binary = ""

        if operand in self.registros_binarios_cero:  # Es un registro
            reg_binary = self.registros_binarios_cero[operand]
            operands_binary += reg_binary
        else:  # Es un valor numérico
            if operand != None:
                sign_bit = '0' if int(operand) >= 0 else '1'
                value_binary = f"{abs(int(operand)):011b}"
                operands_binary += sign_bit + value_binary
        if operand != None:
            while len(operands_binary) < 23:  # Asegurar 23 bits para los tres operandos
                try: 
                    operands_binary += self.registerBank.getRegister(operand)
                    pila.append(self.registerBank.getRegister(operand))
                except:
                    self.registerBank.addRegister(operand, "000000000000")
        else:
            operands_binary = pila[0]+pila[-1]

        return codop + operands_binary[:24]

