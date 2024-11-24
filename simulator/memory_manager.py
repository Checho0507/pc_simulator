class MemoryManager:
    def __init__(self, controlUnit, memory, registerBank):
        self.controlUnit = controlUnit
        self.memory = memory
        self.registerBank = registerBank
        self.memoryPointer = 0  # Apunta a la siguiente posición libre en la memoria
        
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
        return codop + self.controlUnit.registros_binarios_cero[variable] + sign_bit + value_binary

    def encode_zero_address_instruction(self, instruction, operand):
        """
        Codifica una instrucción de cero direcciones:
        - 8 bits para el codop
        - 1 bit y 11 bits para cada operando (pueden ser 0 si no se usan)
        """
        codop = self.controlUnit.instrucciones_binarias_cero.get(instruction, "00000000")
        operands_binary = ""

        if operand in self.controlUnit.registros_binarios_cero:  # Es un registro
            reg_binary = self.controlUnit.registros_binarios_cero[operand]
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
                except:
                    self.registerBank.addRegister(operand, "000000000000")

        return codop + operands_binary[:24]


    def load_program(self, instructions):
        """
        Procesa y carga las instrucciones y asignaciones en memoria.
        """
        for instr in instructions:
            if "=" in instr:  # Asignación al banco de registros
                var, val = instr.split(" = ")
                value = int(val.strip())
                encoded = self.encode_assignment(var.strip(), value)
                print(f"Encoded assignment {instr}: {encoded}")
                encoded_val = self.int_to_binary(value)
                self.registerBank.addRegister(var, encoded_val)  # Guardar en el banco de registros
            else:  # Instrucciones a memoria
                parts = instr.split()
                operation = parts[0]
                if len(parts) > 1:
                    operands = parts[1]  # Operandos como strings
                else:
                    operands = None
                encoded = self.encode_zero_address_instruction(operation, operands)
                print(f"Encoded instruction {instr}: {encoded}")
                self.memory.write(self.memoryPointer, encoded)
                self.memoryPointer += 1
        print(self.registerBank.registers)
