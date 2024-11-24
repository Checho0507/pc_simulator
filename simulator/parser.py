class Parser:
    def __init__(self):
        self.instructionSet = {"LOAD": "0001", "STORE": "0010", "ADD": "0011"}

    def parseInstruction(self, instruction):
        return self.instructionSet.get(instruction, "UNKNOWN")
