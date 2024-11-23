from alu import ALU
from bus import Bus
from memory import Memory
from registers import MAR, MBR, IR, RegisterBank
from io_devices import IO
from parser import Parser

class Simulator:
    def __init__(self):
        # Componentes del simulador
        self.alu = ALU()
        self.bus = Bus()
        self.memory = Memory(size=1024)  # Memoria de 1024 direcciones
        self.mar = MAR()  # Registro de dirección de memoria
        self.mbr = MBR()  # Registro de búfer de memoria
        self.ir = IR()  # Registro de instrucción
        self.register_bank = RegisterBank()  # Banco de registros
        self.io_device = IO()  # Dispositivo de I/O
        self.parser = Parser()  # Analizador de instrucciones
        
        # Agregar registros al banco
        self.register_bank.agregar_registro("A")
        self.register_bank.agregar_registro("B")
        self.register_bank.agregar_registro("C")
        self.register_bank.agregar_registro("D")

    def cargar_programa(self, programa):
        """
        Carga un programa de instrucciones en la memoria.
        El programa es una lista de instrucciones de bajo nivel.
        """
        for i, instruccion in enumerate(programa):
            self.memory.write(i, instruccion)

    def ejecutar(self):
        """
        Ejecuta el ciclo de procesamiento del simulador.
        """
        while True:
            # Obtener la instrucción desde la memoria
            self.mar.set_valor(self.register_bank.obtener_valor("PC"))  # PC -> MAR
            instruccion = self.memory.read(self.mar.get_valor())  # Obtener la instrucción desde la memoria
            self.ir.set_valor(instruccion)  # Guardar la instrucción en IR

            # Analizar la instrucción
            decoded_instruction = self.parser.parse(self.ir.get_valor())  # Decodificar la instrucción

            # Procesar la instrucción
            self.procesar_instruccion(decoded_instruction)

            # Incrementar el contador de programa (PC)
            self.register_bank.asignar_valor("PC", self.register_bank.obtener_valor("PC") + 1)

            # Si la instrucción es "HALT", terminar la ejecución
            if decoded_instruction["operacion"] == "HALT":
                print("Simulación terminada.")
                break

    def procesar_instruccion(self, decoded_instruction):
        """
        Procesa una instrucción decodificada.
        """
        operacion = decoded_instruction["operacion"]
        if operacion == "ADD":
            self.procesar_suma(decoded_instruction)
        elif operacion == "SUB":
            self.procesar_resta(decoded_instruction)
        elif operacion == "MUL":
            self.procesar_multiplicacion(decoded_instruction)
        elif operacion == "DIV":
            self.procesar_division(decoded_instruction)
        elif operacion == "MOV":
            self.procesar_asignacion(decoded_instruction)
        elif operacion == "CMP":
            self.procesar_comparacion(decoded_instruction)
        elif operacion == "HALT":
            pass  # Termina la ejecución
        else:
            print(f"Operación {operacion} no soportada.")

    def procesar_suma(self, decoded_instruction):
        """
        Procesa la operación de suma.
        """
        reg1 = decoded_instruction["reg1"]
        reg2 = decoded_instruction["reg2"]
        resultado = self.alu.sumar(self.register_bank.obtener_valor(reg1), self.register_bank.obtener_valor(reg2))
        self.register_bank.asignar_valor(decoded_instruction["destino"], resultado)

    def procesar_resta(self, decoded_instruction):
        """
        Procesa la operación de resta.
        """
        reg1 = decoded_instruction["reg1"]
        reg2 = decoded_instruction["reg2"]
        resultado = self.alu.restar(self.register_bank.obtener_valor(reg1), self.register_bank.obtener_valor(reg2))
        self.register_bank.asignar_valor(decoded_instruction["destino"], resultado)

    def procesar_multiplicacion(self, decoded_instruction):
        """
        Procesa la operación de multiplicación.
        """
        reg1 = decoded_instruction["reg1"]
        reg2 = decoded_instruction["reg2"]
        resultado = self.alu.multiplicar(self.register_bank.obtener_valor(reg1), self.register_bank.obtener_valor(reg2))
        self.register_bank.asignar_valor(decoded_instruction["destino"], resultado)

    def procesar_division(self, decoded_instruction):
        """
        Procesa la operación de división.
        """
        reg1 = decoded_instruction["reg1"]
        reg2 = decoded_instruction["reg2"]
        resultado = self.alu.dividir(self.register_bank.obtener_valor(reg1), self.register_bank.obtener_valor(reg2))
        self.register_bank.asignar_valor(decoded_instruction["destino"], resultado)

    def procesar_asignacion(self, decoded_instruction):
        """
        Procesa una operación de asignación.
        """
        reg1 = decoded_instruction["reg1"]
        self.register_bank.asignar_valor(decoded_instruction["destino"], self.register_bank.obtener_valor(reg1))

    def procesar_comparacion(self, decoded_instruction):
        """
        Procesa una operación de comparación (ej., A == B).
        """
        reg1 = decoded_instruction["reg1"]
        reg2 = decoded_instruction["reg2"]
        resultado = self.alu.comparar(self.register_bank.obtener_valor(reg1), self.register_bank.obtener_valor(reg2))
        self.register_bank.asignar_valor(decoded_instruction["destino"], resultado)

