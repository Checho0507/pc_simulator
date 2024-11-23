class Bus:
    def __init__(self):
        # Sub-buses del sistema
        self.data_bus = None  # Bus de datos (transporte de datos)
        self.address_bus = None  # Bus de direcciones (dirección de memoria)
        self.control_bus = None  # Bus de control (señales de control)
        self.instruction_bus = None  # Bus de instrucciones (instrucciones)
        
    def transfer_data(self, source, destination, data):
        """
        Transfiere datos entre dos componentes (como registros o memoria) a través del bus de datos.
        :param source: Componente de origen (puede ser un registro o memoria)
        :param destination: Componente de destino (puede ser un registro o memoria)
        :param data: Datos que se van a transferir
        """
        print(f"Transferencia de datos desde {source} hacia {destination}")
        destination.set_value(data)  # Establece el valor del destino
    
    def transfer_address(self, source, destination, address):
        """
        Transfiere una dirección de memoria a través del bus de direcciones.
        :param source: Componente que emite la dirección (registro o memoria)
        :param destination: Componente de destino (memoria)
        :param address: Dirección de memoria
        """
        print(f"Transferencia de dirección {address} desde {source} hacia {destination}")
        destination.set_address(address)  # Establece la dirección de destino
    
    def transfer_control_signal(self, control_signal):
        """
        Envía una señal de control a través del bus de control para activar la operación deseada.
        :param control_signal: Señal de control (lectura, escritura, etc.)
        """
        print(f"Enviando señal de control: {control_signal}")
    
    def transfer_instruction(self, instruction, control_unit):
        """
        Transfiere una instrucción al bus de instrucciones para ser procesada por la unidad de control.
        :param instruction: Instrucción que será procesada
        :param control_unit: Unidad de control que procesa la instrucción
        """
        print(f"Transfiriendo instrucción: {instruction} a la unidad de control")
        control_unit.process_instruction(instruction)


# Sub-buses: Implementación de los sub-buses para la transferencia de datos
class DataBus:
    def __init__(self):
        self.data = None

    def set_value(self, value):
        self.data = value

    def get_value(self):
        return self.data

    def __repr__(self):
        return f"Data: {self.data}"


class AddressBus:
    def __init__(self):
        self.address = None

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def __repr__(self):
        return f"Address: {self.address}"


class ControlBus:
    def __init__(self):
        self.signal = None

    def set_signal(self, signal):
        self.signal = signal

    def get_signal(self):
        return self.signal

    def __repr__(self):
        return f"Control Signal: {self.signal}"


class InstructionBus:
    def __init__(self):
        self.instruction = None

    def set_instruction(self, instruction):
        self.instruction = instruction

    def get_instruction(self):
        return self.instruction

    def __repr__(self):
        return f"Instruction: {self.instruction}"
