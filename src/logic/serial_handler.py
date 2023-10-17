import serial


class serial_interface:

    def __init__(self):
        self.baud = 0
        self.interface = ""
        self.port = None

    def setup(self, baud, interface):
        self.baud = baud
        self.interface = interface
        self.port = serial.Serial(interface, baudrate=self.baud)

    def receive(self):
        return self.port.readline()

    def close(self):
        self.port.close()


serial_handler = serial_interface()
