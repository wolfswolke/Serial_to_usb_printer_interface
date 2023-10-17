import time
from threading import Thread

from logic.logging_handler import logger
from logic.serial_handler import serial_handler
from logic.print_handler import print_handler


def keep_alive():
    try:
        t = Thread(target=run)
        t.daemon = True
        t.start()
        while True:
            time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        logger.log(level="info", handler="serial_handler", message={"event": "Service Stopped"})
        serial_handler.close()
        exit(0)


def run():
    data = ""
    while True:
        line = serial_handler.receive()
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


if __name__ == "__main__":
    logger.setup_logger()
    serial_handler.setup(baud=115200, interface="COM8")  # /dev/ttyUSB0
    print_handler.setup("ZDesigner ZD421-203dpi ZPL") # ZTC-ZD421-203dpi-ZPL
    keep_alive()
