import re
class Parser:
    def __init__(self, unidad_control):
        """
        Inicializa el analizador sintáctico.
        :param registros: El banco de registros.
        :param alu: La unidad aritmético-lógica.
        :param memoria: La memoria del sistema.
        :param bus: El bus del sistema.
        :param unidad_control: La unidad de control que maneja el flujo.
        """
        self.unidad_control = unidad_control
        self.registros = self.unidad_control.registros
        self.alu = self.unidad_control.alu
        self.memoria = self.unidad_control.memoria
        self.bus = self.unidad_control.bus

    def parsear(self, instrucciones):
        """
        Parsea las instrucciones y las ejecuta.
        :param instrucciones: Lista de instrucciones en formato de texto.
        """
        for instruccion in instrucciones:
            print(f"Ejecutando: {instruccion}")
            # Parsear y ejecutar la instrucción
            self.ejecutar_instruccion(instruccion)

    def ejecutar_instruccion(self, instruccion):
        """
        Analiza la instrucción y la ejecuta.
        :param instruccion: Instrucción en formato de texto.
        """
        # Eliminar espacios en blanco innecesarios
        instruccion = instruccion.strip()

        # Asignación simple: A = 5
        asignacion_match = re.match(r'([A-Za-z]+)\s*=\s*(\d+)', instruccion)
        if asignacion_match:
            variable = asignacion_match.group(1)
            valor = int(asignacion_match.group(2))
            self.asignar(variable, valor)
            return

        # Suma: B = A + 3
        suma_match = re.match(r'([A-Za-z]+)\s*=\s*([A-Za-z]+)\s*\+\s*(\d+)', instruccion)
        if suma_match:
            variable = suma_match.group(1)
            operando1 = suma_match.group(2)
            operando2 = int(suma_match.group(3))
            self.sumar(variable, operando1, operando2)
            return

        # Resta: B = A - 3
        resta_match = re.match(r'([A-Za-z]+)\s*=\s*([A-Za-z]+)\s*-\s*(\d+)', instruccion)
        if resta_match:
            variable = resta_match.group(1)
            operando1 = resta_match.group(2)
            operando2 = int(resta_match.group(3))
            self.restar(variable, operando1, operando2)
            return

        # Multiplicación: B = A * 3
        multiplicacion_match = re.match(r'([A-Za-z]+)\s*=\s*([A-Za-z]+)\s*\*\s*(\d+)', instruccion)
        if multiplicacion_match:
            variable = multiplicacion_match.group(1)
            operando1 = multiplicacion_match.group(2)
            operando2 = int(multiplicacion_match.group(3))
            self.multiplicar(variable, operando1, operando2)
            return

        # División: B = A / 3
        division_match = re.match(r'([A-Za-z]+)\s*=\s*([A-Za-z]+)\s*/\s*(\d+)', instruccion)
        if division_match:
            variable = division_match.group(1)
            operando1 = division_match.group(2)
            operando2 = int(division_match.group(3))
            self.dividir(variable, operando1, operando2)
            return

        # Comparaciones booleanas (Ejemplo: A == 5)
        comparacion_match = re.match(r'([A-Za-z]+)\s*==\s*(\d+)', instruccion)
        if comparacion_match:
            variable = comparacion_match.group(1)
            valor = int(comparacion_match.group(2))
            self.comparar(variable, valor, '==')
            return

        comparacion_match = re.match(r'([A-Za-z]+)\s*!=\s*(\d+)', instruccion)
        if comparacion_match:
            variable = comparacion_match.group(1)
            valor = int(comparacion_match.group(2))
            self.comparar(variable, valor, '!=')
            return

        comparacion_match = re.match(r'([A-Za-z]+)\s*>\s*(\d+)', instruccion)
        if comparacion_match:
            variable = comparacion_match.group(1)
            valor = int(comparacion_match.group(2))
            self.comparar(variable, valor, '>')
            return

        comparacion_match = re.match(r'([A-Za-z]+)\s*<\s*(\d+)', instruccion)
        if comparacion_match:
            variable = comparacion_match.group(1)
            valor = int(comparacion_match.group(2))
            self.comparar(variable, valor, '<')
            return

        comparacion_match = re.match(r'([A-Za-z]+)\s*>=\s*(\d+)', instruccion)
        if comparacion_match:
            variable = comparacion_match.group(1)
            valor = int(comparacion_match.group(2))
            self.comparar(variable, valor, '>=')
            return

        comparacion_match = re.match(r'([A-Za-z]+)\s*<=\s*(\d+)', instruccion)
        if comparacion_match:
            variable = comparacion_match.group(1)
            valor = int(comparacion_match.group(2))
            self.comparar(variable, valor, '<=')
            return

        # Si la instrucción no coincide con ningún patrón, es inválida
        print(f"Error: Instrucción inválida '{instruccion}'")

    def asignar(self, variable, valor):
        """
        Asigna un valor a una variable.
        :param variable: Nombre de la variable.
        :param valor: Valor a asignar.
        """
        if variable in self.registros:
            self.registros[variable].valor = valor
        else:
            print(f"Error: La variable '{variable}' no está registrada.")

    def sumar(self, variable, operando1, operando2):
        """
        Realiza una suma y asigna el resultado a una variable.
        :param variable: Nombre de la variable.
        :param operando1: Operando 1 (puede ser una variable).
        :param operando2: Operando 2 (valor constante).
        """
        if operando1 in self.registros:
            resultado = self.alu.sumar(self.registros[operando1].valor, operando2)
            self.asignar(variable, resultado)
        else:
            print(f"Error: La variable '{operando1}' no está registrada.")

    def restar(self, variable, operando1, operando2):
        """
        Realiza una resta y asigna el resultado a una variable.
        :param variable: Nombre de la variable.
        :param operando1: Operando 1 (puede ser una variable).
        :param operando2: Operando 2 (valor constante).
        """
        if operando1 in self.registros:
            resultado = self.alu.restar(self.registros[operando1].valor, operando2)
            self.asignar(variable, resultado)
        else:
            print(f"Error: La variable '{operando1}' no está registrada.")

    def multiplicar(self, variable, operando1, operando2):
        """
        Realiza una multiplicación y asigna el resultado a una variable.
        :param variable: Nombre de la variable.
        :param operando1: Operando 1 (puede ser una variable).
        :param operando2: Operando 2 (valor constante).
        """
        if operando1 in self.registros:
            resultado = self.alu.multiplicar(self.registros[operando1].valor, operando2)
            self.asignar(variable, resultado)
        else:
            print(f"Error: La variable '{operando1}' no está registrada.")

    def dividir(self, variable, operando1, operando2):
        """
        Realiza una división y asigna el resultado a una variable.
        :param variable: Nombre de la variable.
        :param operando1: Operando 1 (puede ser una variable).
        :param operando2: Operando 2 (valor constante).
        """
        if operando1 in self.registros:
            resultado = self.alu.dividir(self.registros[operando1].valor, operando2)
            self.asignar(variable, resultado)
        else:
            print(f"Error: La variable '{operando1}' no está registrada.")

    def comparar(self, variable, valor, operador):
        """
        Realiza una comparación booleana.
        :param variable: Nombre de la variable.
        :param valor: Valor a comparar.
        :param operador: Operador de comparación (==, !=, >, <, >=, <=).
        """
        if variable in self.registros:
            resultado = False
            if operador == '==':
                resultado = self.registros[variable].valor == valor
            elif operador == '!=':
                resultado = self.registros[variable].valor != valor
            elif operador == '>':
                resultado = self.registros[variable].valor > valor
            elif operador == '<':
                resultado = self.registros[variable].valor < valor
            elif operador == '>=':
                resultado = self.registros[variable].valor >= valor
            elif operador == '<=':
                resultado = self.registros[variable].valor <= valor

            print(f"Comparación: {self.registros[variable].valor} {operador} {valor} = {resultado}")
        else:
            print(f"Error: La variable '{variable}' no está registrada.")
