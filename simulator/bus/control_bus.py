import time

class ControlBus:
    def __init__(self):
        self.controlSignals = []

    def sendControlSignal(self, signal):
        self.controlSignals.append(signal)
        print(f"ControlBus: Sending control signal '{signal}'")
        time.sleep(2)

    def receiveControlSignal(self):
        if self.controlSignals:
            signal = self.controlSignals.pop(0)
            print(f"ControlBus: Receiving control signal '{signal}'")
            time.spleep(2)
            return signal
        return None