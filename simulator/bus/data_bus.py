class DataBus:
    def __init__(self):
        self.data = "00000000000000000000000000000000"
        
    def getData(self):
        return self.data

    def sendData(self, data, source, destination, mensaje_placeholder):
        self.data = data
        mensaje_placeholder.info(f"Bus de datos: Sending {data} from {source} to {destination}")

    def receiveData(self, data, source, destination, mensaje_placeholder):
        mensaje_placeholder.info(f"DataBus: {destination} is receiving {data} from {source}")