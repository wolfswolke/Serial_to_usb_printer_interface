import serial


class serial_interface:

    def __init__(self):
        self.baud = 115200
        self.interface = "USB"
        self.port = serial.Serial("COM8", baudrate=self.baud)

    def setup(self, baud, interface):
        self.baud = baud
        self.interface = interface
        self.port = serial.Serial(interface, baudrate=self.baud)

    def receive(self):
        return self.port.read(10)


serial_handler = serial_interface()
