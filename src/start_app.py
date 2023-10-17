from logic.logging_handler import logger
from logic.print_handler import print_handler
import serial

if __name__ == "__main__":
    logger.setup_logger()
    # serial_handler.setup(baud=115200, timeout=3.0, interface="COM8")
    ser = serial.Serial("COM8", baudrate=115200) # /dev/ttyUSB0
    print_handler.setup("ZTC-ZD421-203dpi-ZPL")

    try:
        data = ""
        while True:
            line = ser.readline()
            if line:
                logger.log(level="debug", handler="serial_handler", message={"event": "Serial Data", "data": line})
            try:
                data += line.decode("utf-8")
            except UnicodeDecodeError:
                data += line
            if "^XZ" in data:
                logger.log(level="info", handler="serial_handler", message={"event": "Label Received"})
                logger.log(level="debug", handler="serial_handler", message={"event": "Label Data", "data": data})
                print_handler.print(data)
                data = ""
        ser.close()

    except KeyboardInterrupt:
        ser.close()
        logger.log(level="info", handler="serial_handler", message={"event": "Service Stopped"})
        exit(0)
