from simulator.registers import Register

class RegisterBank:
    def __init__(self):
        self.registers = {}
        # Inicializar registros
        self.PC = Register()
        self.IR = Register()
        self.MAR = Register()
        self.MBR = Register()

    def addRegister(self, name, register):
        self.registers[name] = register

    def getRegister(self, name):
        return self.registers[name]
