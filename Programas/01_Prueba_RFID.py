# este ejemplo fue tomado de la URL
# https://pypi.org/project/mfrc522/
# Y es un breve ejemplo de funcionamiento de la RFID a 13.56 MHz

# Se importan la bibliotecas a utilizar

from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise