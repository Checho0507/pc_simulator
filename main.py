from simulator.simulator import Simulator
from simulator.io_devices import UnidadDeIO
from simulator.register_bank import RegisterBank
from resources.instructions import instrucciones_binarias_cero
from resources.registers import registros_binarios_cero

def main():
    """
    Punto de entrada principal para ejecutar el simulador.
    Este archivo configura los componentes del sistema y ejecuta el ciclo de simulación.
    """
    
    # Crear el simulador
    simulador = Simulator()

    # Configurar el dispositivo de entrada/salida (si es necesario)
    io_device = UnidadDeIO(simulador.bus, simulador.memory)

    # Mostrar mensaje inicial al usuario
    print("Bienvenido al Simulador de Procesador de Bajo Nivel")

    # Solicitar al usuario que ingrese un programa en lenguaje de bajo nivel
    print("Ingrese su programa en lenguaje de bajo nivel (instrucciones separadas por comas):")
    print("Ejemplo de instrucciones: MOV A, 5, ADD A, B, C, HALT")

    # Leer las instrucciones del usuario
    programa_usuario = input("Instrucciones: ").strip()

    # Convertir el programa de texto en una lista de instrucciones
    instrucciones = programa_usuario.split(",")  # Separar por comas

    # Limpiar y formatear las instrucciones
    instrucciones = [instruccion.strip() for instruccion in instrucciones]
    
    #Paso a instrucciones en bits
    instrucciones2 = simulador.unidad_control.convertir_a_binario_cero(instrucciones, instrucciones_binarias_cero, registros_binarios_cero)

    # Cargar el programa en la memoria del simulador
    simulador.cargar_programa(instrucciones2)

    # Ejecutar el simulador
    simulador.ejecutar(instrucciones)

    # Si es necesario, aquí se podría manejar la entrada/salida adicional
    io_device.mostrar_resultado()

if __name__ == "__main__":
    main()
