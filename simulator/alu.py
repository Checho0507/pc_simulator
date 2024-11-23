class ALU:
    def __init__(self):
        self.resultado = 0

    def operar(self, operacion, operando1, operando2=None):
        """
        Ejecuta una operación aritmética o lógica en base a la instrucción recibida.
        :param operacion: Cadena que indica la operación a realizar.
        :param operando1: Primer operando para la operación (requerido en todas las operaciones).
        :param operando2: Segundo operando para la operación (solo necesario en operaciones binarias).
        :return: El resultado de la operación.
        """
        if operacion == "sumar":
            self.resultado = operando1 + operando2
        elif operacion == "restar":
            self.resultado = operando1 - operando2
        elif operacion == "multiplicar":
            self.resultado = operando1 * operando2
        elif operacion == "dividir":
            if operando2 == 0:
                raise ValueError("Error: División por cero")
            self.resultado = operando1 / operando2
        elif operacion == "igual":
            self.resultado = 1 if operando1 == operando2 else 0
        elif operacion == "mayor":
            self.resultado = 1 if operando1 > operando2 else 0
        elif operacion == "menor":
            self.resultado = 1 if operando1 < operando2 else 0
        elif operacion == "mayor_o_igual":
            self.resultado = 1 if operando1 >= operando2 else 0
        elif operacion == "menor_o_igual":
            self.resultado = 1 if operando1 <= operando2 else 0
        elif operacion == "negacion":
            self.resultado = 0 if operando1 != 0 else 1
        else:
            raise ValueError("Operación no válida")

        return self.resultado

    def __repr__(self):
        return f"Resultado de la operación: {self.resultado}"

