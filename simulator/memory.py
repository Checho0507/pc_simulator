class Memory:
    def __init__(self, size, dataBus, addressBus):
        self.memoryArray = [0] * size
        self.size = size
        self.dataBus = dataBus
        self.addressBus = addressBus

    def read(self, address):
        if 0 <= address < self.size:
            self.addressBus.sendAddress("Memory", address)
            data = self.memoryArray[address]
            self.dataBus.sendData("Memory", data)
            return data
        else:
            raise ValueError("Memory: Address out of range")

    def write(self, address, data):
        print(f"Escribiendo {data} en la dirección de memoria {address}")
        if 0 <= address < self.size:
            self.memoryArray[address] = data
        else:
            raise ValueError("Memory: Address out of range")
