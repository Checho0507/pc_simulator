class MAR:
    """
    Clase que representa el Registro MAR (Memory Address Register).
    Es responsable de almacenar la dirección de memoria.
    """
    def __init__(self):
        self.valor = 0  # Dirección de memoria

    def set_valor(self, valor):
        """
        Asigna un valor al MAR, que debe ser una dirección de memoria.
        """
        self.valor = valor

    def get_valor(self):
        """
        Obtiene el valor (dirección) almacenado en el MAR.
        """
        return self.valor

class MBR:
    """
    Clase que representa el Registro MBR (Memory Buffer Register).
    Es responsable de almacenar los datos que se van a leer o escribir desde/hacia la memoria.
    """
    def __init__(self):
        self.valor = 0  # Contenido de la memoria

    def set_valor(self, valor):
        """
        Asigna un valor al MBR, que generalmente es el valor de datos leídos o a escribir en memoria.
        """
        self.valor = valor

    def get_valor(self):
        """
        Obtiene el valor almacenado en el MBR.
        """
        return self.valor

class IR:
    """
    Clase que representa el Registro IR (Instruction Register).
    Es responsable de almacenar la instrucción que está siendo ejecutada.
    """
    def __init__(self):
        self.valor = ""  # Instrucción en formato de cadena

    def set_valor(self, valor):
        """
        Asigna una instrucción al IR.
        """
        self.valor = valor

    def get_valor(self):
        """
        Obtiene la instrucción almacenada en el IR.
        """
        return self.valor

class Registro:
    """
    Clase que representa un registro general (por ejemplo, A, B, C).
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.valor = 0

    def set_valor(self, valor):
        """
        Asigna un valor al registro.
        """
        self.valor = valor

    def get_valor(self):
        """
        Obtiene el valor del registro.
        """
        return self.valor

    def __repr__(self):
        """
        Representación del registro.
        """
        return f"{self.nombre}: {self.valor}"
