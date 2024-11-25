class ALU:
    def __init__(self):
        self.result = 0

    def add(self, operand1, operand2):
        self.result = int(operand1, 2) + int(operand2, 2)
    
    def getResult(self):
        return self.result    
