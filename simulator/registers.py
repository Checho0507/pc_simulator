class Register:
    def __init__(self):
        self.value = "00000000000000000000000000000000"

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value
