from logic.logging_handler import logger
from logic.print_handler import print_handler
import serial

if __name__ == "__main__":
    logger.setup_logger()
    # serial_handler.setup(baud=115200, timeout=3.0, interface="COM8")
    ser = serial.Serial("COM8", baudrate=115200)

    try:
        data = ""
        while True:
            line = ser.readline()
            data += line.decode("utf-8")
            if "^XZ" in data:
                print_handler.print_label(data)
                data = ""
        ser.close()

    except KeyboardInterrupt:
        logger.log(level="info", handler="serial_handler", message={"event": "Service Stopped"})
        exit(0)
