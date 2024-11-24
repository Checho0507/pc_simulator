from simulator.alu import ALU
from simulator.bus.address_bus import AddressBus
from simulator.bus.control_bus import ControlBus
from simulator.bus.data_bus import DataBus
from simulator.control_unit import ControlUnit
from simulator.memory import Memory
from simulator.memory_manager import MemoryManager
from simulator.register_bank import RegisterBank
from simulator.registers import Register


class Simulator:
    def __init__(self):
        # Crear buses
        self.dataBus = DataBus()
        self.addressBus = AddressBus()
        self.controlBus = ControlBus()

        # Crear componentes principales
        self.controlUnit = ControlUnit(self.dataBus, self.addressBus, self.controlBus)
        self.memory = Memory(256, self.dataBus, self.addressBus)
        self.alu = ALU()
        self.registerBank = RegisterBank()

        # Inicializar registros
        self.registerBank.addRegister("PC", Register())
        self.registerBank.addRegister("IR", Register())
        self.registerBank.addRegister("MAR", Register())
        self.registerBank.addRegister("MBR", Register())

    def executeProgram(self):
        # Crear buses y componentes principales
        dataBus = DataBus()
        addressBus = AddressBus()
        controlBus = ControlBus()
        controlUnit = ControlUnit(dataBus, addressBus, controlBus)
        memory = Memory(256, dataBus, addressBus)
        registerBank = RegisterBank()
        memoryManager = MemoryManager(controlUnit, memory, registerBank)

        # Ejemplo de programa para instrucciones de cero direcciones
        program_zero = [
            "A = -1", "C = 2", "D = 3", "E = 4", "PUSH D", "PUSH E", 
            "SUB", "PUSH A", "MUL", "POP X", "PUSH A", "PUSH C", 
            "MUL", "PUSH X", "DIV", "POP Z"
        ]

        print("Loading zero-address instructions:")
        memoryManager.load_program(program_zero)
