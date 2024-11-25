import time


class DataBus:
    def __init__(self):
        self.data = "00000000000000000000000000000000"
        
    def getData(self):
        return self.data

    def sendData(self, data, source, destination):
        self.data = data
        print(f"DataBus: Sending {data} from {source} to {destination}")
        time.sleep(0)

    def receiveData(self, data, source, destination):
        print(f"DataBus: {destination} is receiving {data} from {source}")
        time.sleep(0)