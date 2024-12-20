import time

class Memory:
    def __init__(self, size, dataBus, addressBus):
        self.memoryArray = ["00000000000000000000000000000000"] * size
        self.size = size
        self.dataBus = dataBus
        self.addressBus = addressBus
        
    def getMemory(self):
        data = {}
        for i in range(len(self.memoryArray)):
            data[i] = self.memoryArray[i]
        return(data)

    def read(self, address):
        if 0 <= address < self.size:
            data = self.memoryArray[address]
            return data
        else:
            raise ValueError("Memory: Address out of range")

    def write(self, address, data):
        print(f"Escribiendo {data} en la dirección de memoria {address}")
        time.sleep(0)
        if 0 <= address < self.size:
            self.memoryArray[address] = data
        else:
            raise ValueError("Memory: Address out of range")
