import time

class AddressBus:
    def __init__(self):
        self.address = 0

    def sendAddress(self, address, source, destination):
        print(f"AddressBus: Sending {address} from {source} to {destination}")
        time.sleep(0)

    def receiveAddress(self, address, source, destination):
        print(f"AddressBus: {destination} is receiving {address} from {source}")
        time.sleep(0)
