from .registers import Registro

class RegisterBank:
    def __init__(self):
        """
        Inicializa el banco de registros con registros por defecto (A, B, C, etc.)
        """
        self.registros = {}

    def agregar_registro(self, nombre):
        """
        Agrega un nuevo registro al banco.
        :param nombre: Nombre del registro a agregar.
        """
        if nombre not in self.registros:
            self.registros[nombre] = Registro(nombre)
        else:
            print(f"Error: El registro '{nombre}' ya existe.")

    def obtener_registro(self, nombre):
        """
        Obtiene el registro por su nombre.
        :param nombre: Nombre del registro.
        :return: El objeto Registro correspondiente.
        """
        if nombre in self.registros:
            return self.registros[nombre]
        else:
            print(f"Error: El registro '{nombre}' no existe.")
            return None

    def eliminar_registro(self, nombre):
        """
        Elimina un registro del banco de registros.
        :param nombre: Nombre del registro a eliminar.
        """
        if nombre in self.registros:
            del self.registros[nombre]
        else:
            print(f"Error: El registro '{nombre}' no existe.")

    def mostrar_registros(self):
        """
        Muestra todos los registros del banco de registros.
        """
        for registro in self.registros.values():
            print(registro)

    def asignar_valor(self, nombre, valor):
        """
        Asigna un valor a un registro específico.
        :param nombre: Nombre del registro.
        :param valor: Valor a asignar al registro.
        """
        registro = self.obtener_registro(nombre)
        if registro:
            registro.set_valor(valor)

    def obtener_valor(self, nombre):
        """
        Obtiene el valor de un registro.
        :param nombre: Nombre del registro.
        :return: El valor del registro.
        """
        registro = self.obtener_registro(nombre)
        if registro:
            return registro.get_valor()
        return None
