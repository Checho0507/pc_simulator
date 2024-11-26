import time

class ControlBus:
    def __init__(self):
        self.controlSignal = "00000000000000000000000000000000"
        
    def getControlSignal(self):
        return self.controlSignal

    def sendControlSignal(self, signal, mensaje_placeholder):
        self.controlSignals = signal
        if signal == "11000000000000000000000000000011":
            signal = "FETCH"
        elif signal == "11011000000000000000000000011011":
            signal = "DECODE"
        elif signal == "11011011000000000000000011011011":
            signal = "EXECUTE"
        mensaje_placeholder.info(f"Bus de Control: Enviando señal de control '{signal}'")

    def receiveControlSignal(self, mensaje_placeholder):
        mensaje_placeholder.info(f"ControlBus: Reciviendo señal de control '{self.controlSignals}'")