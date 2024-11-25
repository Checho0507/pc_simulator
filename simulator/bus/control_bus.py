import time

class ControlBus:
    def __init__(self):
        self.controlSignal = "00000000000000000000000000000000"
        
    def getControlSignal(self):
        return self.controlSignal

    def sendControlSignal(self, signal):
        self.controlSignals = signal
        print(f"ControlBus: Sending control signal '{signal}'")
        time.sleep(0)

    def receiveControlSignal(self):
        print(f"ControlBus: Receiving control signal '{self.controlSignals}'")
        time.sleep(0)