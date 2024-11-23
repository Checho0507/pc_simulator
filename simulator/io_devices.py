class DispositivoEntrada:
    """
    Dispositivo de entrada para programación en bajo nivel.
    """
    def __init__(self):
        self.buffer = ""

    def recibir_instruccion(self, instruccion):
        """
        Recibe una instrucción del usuario.
        """
        pass
    
class DispositivoSalida:
    """
    Dispositivo de salida para mostrar resultados.
    """
    def __init__(self):
        self.salida = ""

    def mostrar_resultado(self, resultado):
        """
        Muestra resultados en pantalla.
        """
        pass
