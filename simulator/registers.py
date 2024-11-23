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


class RegisterBank:
    """
    Clase que representa el banco de registros generales de propósito.
    Aquí se almacenan los registros como A, B, C, etc.
    """
    def __init__(self):
        self.registros = {}

    def agregar_registro(self, nombre):
        """
        Agrega un nuevo registro al banco.
        """
        if nombre not in self.registros:
            self.registros[nombre] = Registro(nombre)
        else:
            print(f"El registro '{nombre}' ya existe.")

    def obtener_registro(self, nombre):
        """
        Obtiene un registro del banco por su nombre.
        """
        if nombre in self.registros:
            return self.registros[nombre]
        else:
            print(f"Error: El registro '{nombre}' no existe.")
            return None

    def asignar_valor(self, nombre, valor):
        """
        Asigna un valor a un registro específico del banco.
        """
        registro = self.obtener_registro(nombre)
        if registro:
            registro.set_valor(valor)

    def obtener_valor(self, nombre):
        """
        Obtiene el valor de un registro específico del banco.
        """
        registro = self.obtener_registro(nombre)
        if registro:
            return registro.get_valor()
        return None


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
