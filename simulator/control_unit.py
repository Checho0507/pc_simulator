
from simulator.registers import IR, MAR, MBR


class UnidadControl:
    """
    Unidad de Control (microprogramada o cableada).
    """
    def __init__(self):
        self.mar = MAR()
        self.mbr = MBR()
        self.ir = IR()
        self.contador_programa = 0  # Dirección de la próxima instrucción
        self.bandera_interrupcion = False

    def cargar_instruccion(self, instruccion):
        """
        Carga una instrucción en el registro IR.
        """
        self.ir.set_instruccion(instruccion)

    def ejecutar_instruccion(self):
        """
        Decodifica y ejecuta la instrucción actual.
        """
        instruccion = self.ir.get_instruccion()
        # Lógica para decodificar y ejecutar.
        pass