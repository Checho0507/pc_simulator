import time

class ControlBus:
    def __init__(self):
        self.controlSignals = ""

    def sendControlSignal(self, signal):
        self.controlSignals = signal
        print(f"ControlBus: Sending control signal '{signal}'")
        time.sleep(0)

    def receiveControlSignal(self):
        print(f"ControlBus: Receiving control signal '{self.controlSignals}'")
        time.sleep(0)