from .registers import Registro

class UnidadDeControl:
    def __init__(self, bus, alu, registros, memoria):
        self.bus = bus
        self.alu = alu
        self.registros = registros
        self.memoria = memoria
        self.pc = Registro("PC")  # Contador de programa, registro que guarda la dirección de la siguiente instrucción
        self.ir = Registro("IR")  # Registro de instrucción (IR), guarda la instrucción actual
        self.mar = Registro("MAR")  # Registro de dirección de memoria (MAR)
        self.mbr = Registro("MBR")  # Registro de buffer de memoria (MBR)
    
    def process_instruction(self, instruction):
        """
        Procesa una instrucción y ejecuta las acciones necesarias.
        La instrucción debe ser un string, por ejemplo: "MOV A, B", "ADD A, 5", etc.
        """
        print(f"Procesando instrucción: {instruction}")
        self.ir.set_value(instruction)  # Almacena la instrucción en el IR
        
        # Decodificar la instrucción (esto dependerá de la complejidad del conjunto de instrucciones)
        # Asumiremos una instrucción simple: "MOV A, B", "ADD A, 5", "SUB B, A", etc.
        
        parts = instruction.split()
        
        if parts[0] == "MOV":
            # MOV X, Y -> Mover el valor de Y a X
            src = parts[2]
            dest = parts[1]
            
            if src.isdigit():  # Si el valor fuente es un número
                value = int(src)
                self.registros.get(dest).set_value(value)
            else:
                value = self.registros.get(src).get_value()
                self.registros.get(dest).set_value(value)
        
        elif parts[0] == "ADD":
            # ADD X, Y -> Sumar el valor de Y a X
            dest = parts[1]
            value = int(parts[2]) if parts[2].isdigit() else self.registros.get(parts[2]).get_value()
            result = self.alu.add(self.registros.get(dest).get_value(), value)
            self.registros.get(dest).set_value(result)
        
        elif parts[0] == "SUB":
            # SUB X, Y -> Restar el valor de Y a X
            dest = parts[1]
            value = int(parts[2]) if parts[2].isdigit() else self.registros.get(parts[2]).get_value()
            result = self.alu.subtract(self.registros.get(dest).get_value(), value)
            self.registros.get(dest).set_value(result)
        
        elif parts[0] == "JMP":
            # JMP X -> Saltar a la dirección X (cambio del PC)
            address = int(parts[1])
            self.pc.set_value(address)
        
        # Continuar con otros tipos de instrucciones como multiplicaciones, divisiones, comparaciones, etc.
    
    def fetch(self):
        """
        Obtiene la instrucción del contador de programa (PC) y la pasa al bus de instrucciones.
        """
        instruction_address = self.pc.get_value()
        instruction = self.memoria.get_value(instruction_address)  # Obtiene la instrucción de la memoria
        self.bus.transfer_instruction(instruction, self)  # Transfiere la instrucción al bus de instrucciones
        print(f"Instrucción obtenida del PC ({instruction_address}): {instruction}")
    
    def update_pc(self):
        """
        Actualiza el contador de programa (PC) para que apunte a la siguiente instrucción.
        """
        self.pc.set_value(self.pc.get_value() + 1)  # Incrementa el PC para apuntar a la siguiente instrucción
        
    def convertir_a_binario_cero(self, instrucciones, instrucciones_binarias, registros_binarios):
        instrucciones_bin = []

        for instruccion in instrucciones:
            partes = instruccion.split()  # Dividimos la instrucción en partes
            operacion = partes[0]  # La primera parte es la operación
            if operacion in instrucciones_binarias:
                # Obtener el código binario de la operación (8 o 16 bits)
                instruccion_bin = instrucciones_binarias[operacion]

                # Procesar los operandos 
                if len(partes) == 2:  # Caso de 1 dirección (MOV A)
                    registro = partes[1]
                    if registro in registros_binarios:
                        # Si es un registro, concatenamos su valor binario
                        instruccion_bin += registros_binarios[registro]
                
                # Aseguramos que la instrucción tiene exactamente 32 bits
                instrucciones_bin.append(instruccion_bin)

        return instrucciones_bin
