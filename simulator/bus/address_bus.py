import time

class AddressBus:
    def __init__(self):
        self.address = "00000000000000000000000000000000"
    
    def getAddress(self):
        return self.address

    def sendAddress(self, address, source, destination):
        self.address = address
        print(f"AddressBus: Sending {address} from {source} to {destination}")
        time.sleep(0)

    def receiveAddress(self, address, source, destination):
        print(f"AddressBus: {destination} is receiving {address} from {source}")
        time.sleep(0)
