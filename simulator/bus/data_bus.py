class DataBus:
    def __init__(self):
        self.data = []

    def sendData(self, source, destination):
        print(f"DataBus: Sending data from {source} to {destination}")

    def receiveData(self, source):
        print(f"DataBus: Receiving data from {source}")
