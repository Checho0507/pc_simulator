class ALU:
    def __init__(self):
        self.result = 0

    def add(self, sign1:1, operand1, sing2:1, operand2):
        self.result = sign1*operand1 + sing2*operand2
        
    def sub(self, sign1:1, operand1, sing2:1, operand2):
        self.result = sign1*operand1 - sing2*operand2
        
    def mul(self, sign1:1, operand1, sing2:1, operand2):
        self.result = sign1*operand1 * sing2*operand2
        
    def div(self, sign1:1, operand1, sing2:1, operand2):
        self.result = sign1*operand1 / sing2*operand2
        
    def getResult(self):
        return self.result    
