from main import BancoRegistros
from simulator.alu import ALU
from simulator.bus import Bus
from simulator.control_unit import UnidadControl
from simulator.io_devices import DispositivoEntrada, DispositivoSalida
from simulator.memory import MemoriaPrincipal


class Simulator:
    """
    Clase principal que conecta todos los componentes.
    """
    def __init__(self):
        self.alu = ALU()
        self.unidad_control = UnidadControl()
        self.banco_registros = BancoRegistros(cantidad=16)
        self.memoria_principal = MemoriaPrincipal(tamano=256)
        self.dispositivo_entrada = DispositivoEntrada()
        self.dispositivo_salida = DispositivoSalida()
        self.bus = Bus()

    def ejecutar_programa(self, programa):
        """
        Ejecuta un conjunto de instrucciones.
        """
        pass