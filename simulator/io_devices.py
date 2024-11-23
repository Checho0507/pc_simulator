class UnidadDeIO:
    def __init__(self, bus, memoria):
        self.bus = bus
        self.memoria = memoria
        self.dispositivos_entrada = {}
        self.dispositivos_salida = {}

    def conectar_dispositivo_entrada(self, dispositivo, direccion):
        """
        Conecta un dispositivo de entrada a una dirección específica en la memoria.
        """
        self.dispositivos_entrada[direccion] = dispositivo
        print(f"Dispositivo de entrada conectado a la dirección {direccion}: {dispositivo}")

    def conectar_dispositivo_salida(self, dispositivo, direccion):
        """
        Conecta un dispositivo de salida a una dirección específica en la memoria.
        """
        self.dispositivos_salida[direccion] = dispositivo
        print(f"Dispositivo de salida conectado a la dirección {direccion}: {dispositivo}")

    def leer_datos(self, direccion):
        """
        Lee los datos desde un dispositivo de entrada.
        """
        if direccion in self.dispositivos_entrada:
            dispositivo = self.dispositivos_entrada[direccion]
            print(f"Leendo datos desde el dispositivo de entrada en {direccion}: {dispositivo}")
            return dispositivo.leer()  # Simulamos la lectura del dispositivo
        else:
            print(f"No se encontró un dispositivo de entrada en la dirección {direccion}")
            return None

    def escribir_datos(self, direccion, datos):
        """
        Escribe los datos a un dispositivo de salida.
        """
        if direccion in self.dispositivos_salida:
            dispositivo = self.dispositivos_salida[direccion]
            print(f"Escribiendo datos al dispositivo de salida en {direccion}: {datos}")
            dispositivo.escribir(datos)  # Simulamos la escritura en el dispositivo
        else:
            print(f"No se encontró un dispositivo de salida en la dirección {direccion}")

class DispositivoEntrada:
    def __init__(self, nombre):
        self.nombre = nombre

    def leer(self):
        """
        Simula la lectura de datos desde el dispositivo de entrada.
        En un caso real, esto podría ser la lectura desde un archivo, teclado, etc.
        """
        return f"Datos leídos desde {self.nombre}"

class DispositivoSalida:
    def __init__(self, nombre):
        self.nombre = nombre

    def escribir(self, datos):
        """
        Simula la escritura de datos en el dispositivo de salida.
        En un caso real, esto podría ser la escritura en un archivo, pantalla, etc.
        """
        print(f"{datos} escritos en {self.nombre}")
