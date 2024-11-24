class AddressBus:
    def __init__(self):
        self.address = 0

    def sendAddress(self, source, destination):
        print(f"AddressBus: Sending address from {source} to {destination}")

    def receiveAddress(self, source):
        print(f"AddressBus: Receiving address from {source}")
