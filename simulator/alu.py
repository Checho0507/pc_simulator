class ALU:
    def __init__(self):
        self.operationType = None
        self.operand1 = 0
        self.operand2 = 0
        self.result = 0

    def executeOperation(self):
        if self.operationType == "add":
            self.result = self.operand1 + self.operand2
        elif self.operationType == "subtract":
            self.result = self.operand1 - self.operand2
        # Agregar más operaciones según sea necesario
        return self.result
