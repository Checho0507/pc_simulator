class RegisterBank:
    def __init__(self):
        self.registers = {}

    def addRegister(self, name, register):
        self.registers[name] = register

    def getRegister(self, name):
        return self.registers[name]
