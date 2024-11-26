class AddressBus:
    def __init__(self):
        self.address = "00000000000000000000000000000000"
    
    def getAddress(self):
        return self.address

    def sendAddress(self, address, source, destination, mesanje_placeholder):
        self.address = address
        mesanje_placeholder.info(f"Bus de Direcciones: Enviando dirección {address} desde {source} hacia {destination}")

    def receiveAddress(self, address, source, destination, mensaje_placeholder):
        mensaje_placeholder.info(f"Bus de Direcciones: {destination} reciviendo {address} desde {source}")
