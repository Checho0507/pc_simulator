class Memoria:
    def __init__(self, tamaño, particion="física"):
        """
        Inicializa la memoria con un tamaño determinado y partición especificada.
        :param tamaño: El número de direcciones de memoria.
        :param particion: El tipo de partición ("física" o "lógica").
        """
        self.tamaño = tamaño
        self.particion = particion
        # Inicializamos la memoria con valores nulos
        self.memoria = [0] * tamaño
        print(f"Memoria de tamaño {tamaño} con partición {particion} inicializada.")

    def leer(self, direccion):
        """
        Lee el valor en la dirección de memoria especificada.
        :param direccion: La dirección de memoria desde donde leer.
        :return: El valor almacenado en la dirección de memoria.
        """
        if direccion < 0 or direccion >= self.tamaño:
            raise ValueError("Dirección fuera de rango.")
        return self.memoria[direccion]

    def escribir(self, direccion, valor):
        """
        Escribe un valor en la dirección de memoria especificada.
        :param direccion: La dirección de memoria donde se escribirá el valor.
        :param valor: El valor a escribir en la memoria.
        """
        if direccion < 0 or direccion >= self.tamaño:
            raise ValueError("Dirección fuera de rango.")
        self.memoria[direccion] = valor
        print(f"Escrito {valor} en la dirección {direccion}.")

    def particionar_memoria(self, tamaño_parte):
        """
        Crea particiones dentro de la memoria, útil si se tiene memoria lógica.
        :param tamaño_parte: Tamaño de las particiones.
        :return: Una lista de particiones.
        """
        if self.particion != "lógica":
            raise ValueError("Este método solo es aplicable a particiones lógicas.")
        particiones = [self.memoria[i:i + tamaño_parte] for i in range(0, len(self.memoria), tamaño_parte)]
        return particiones

    def mostrar_memoria(self):
        """
        Muestra el estado completo de la memoria.
        """
        print("Estado actual de la memoria:")
        for i, valor in enumerate(self.memoria):
            print(f"Dirección {i}: {valor}")

    def limpiar_memoria(self):
        """
        Limpia la memoria, reiniciando todas las direcciones a cero.
        """
        self.memoria = [0] * self.tamaño
        print("Memoria limpiada.")
