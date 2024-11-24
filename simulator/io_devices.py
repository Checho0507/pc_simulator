class IO_Devices:
    def __init__(self, deviceType):
        self.deviceType = deviceType
        self.status = "idle"

    def readData(self):
        print(f"Reading data from {self.deviceType}")

    def writeData(self):
        print(f"Writing data to {self.deviceType}")
