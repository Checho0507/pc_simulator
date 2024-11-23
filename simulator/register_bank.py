class BancoDeRegistros:
    """
    Banco de registros de propósito general.
    Administra los registros de uso general y especiales.
    """
    def __init__(self, cantidad_registros=8, tamaño_palabra=32):
        """
        Inicializa el banco de registros.
        
        Args:
            cantidad_registros (int): Número de registros en el banco.
            tamaño_palabra (int): Tamaño de cada registro en bits.
        """
        self.registros = [0] * cantidad_registros  # Registros inicializados en 0
        self.tamaño_palabra = tamaño_palabra

    def escribir_registro(self, indice, valor):
        """
        Escribe un valor en un registro específico.
        
        Args:
            indice (int): Índice del registro.
            valor (int): Valor a escribir.
        """
        if 0 <= indice < len(self.registros):
            self.registros[indice] = valor
        else:
            raise IndexError(f"Registro {indice} fuera de rango.")

    def leer_registro(self, indice):
        """
        Lee el valor de un registro específico.
        
        Args:
            indice (int): Índice del registro.

        Returns:
            int: Valor almacenado en el registro.
        """
        if 0 <= indice < len(self.registros):
            return self.registros[indice]
        else:
            raise IndexError(f"Registro {indice} fuera de rango.")

    def mostrar_registros(self):
        """
        Muestra el contenido de todos los registros.
        """
        for i, valor in enumerate(self.registros):
            print(f"R{i}: {valor}")