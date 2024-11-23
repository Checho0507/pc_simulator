class MAR:
    """
    Memory Address Register: Contiene la dirección de memoria que se quiere acceder.
    """
    def __init__(self):
        self.direccion = None

    def set_direccion(self, direccion):
        """
        Establece la dirección de memoria.
        """
        self.direccion = direccion

    def get_direccion(self):
        """
        Retorna la dirección actual.
        """
        return self.direccion


class MBR:
    """
    Memory Buffer Register: Contiene el dato leído o a escribir en memoria.
    """
    def __init__(self):
        self.dato = None

    def set_dato(self, dato):
        """
        Establece el dato en el registro.
        """
        self.dato = dato

    def get_dato(self):
        """
        Retorna el dato actual.
        """
        return self.dato


class IR:
    """
    Instruction Register: Almacena la instrucción actual decodificada.
    """
    def __init__(self):
        self.instruccion = None

    def set_instruccion(self, instruccion):
        """
        Establece la instrucción en el registro.
        """
        self.instruccion = instruccion

    def get_instruccion(self):
        """
        Retorna la instrucción actual.
        """
        return self.instruccion