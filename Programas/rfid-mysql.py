# Bibliotecas
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import mysql.connector
import argparse

#Parser

parser = argparse.ArgumentParser()
parser.add_argument("status")
args = parser.parse_args()



# Inicar el sensor
reader = SimpleMFRC522()

# Conexión
cnx = mysql.connector.connect(user='OmarLAN', password='1234*', host='192.168.1.64', database='rfid')
# Cursor
cursor = cnx.cursor()

# Cuerpo del programa
try:
    # Leer el tag
    #while True:

    print("Acercar el tag al lector")
    id, text = reader.read()
    print("ID: %s\nText: %s" % (id,text))

    SeleccionDatos = text.split(",")
    sleep(1)


    query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('" + SeleccionDatos[0] + "','" + args.status + "'," + str (id) + ");"
    print (query_insert)
    
    # Ejecutar cursor
    
    cursor.execute (query_insert)
        # Asegurarse de realizar la operacion en BD
    cnx.commit()
    print ("Query Ok")

    sleep(1)
except KeyboardInterrupt:
    # Cerrar
    cursor.close()
    cnx.close()
    GPIO.cleanup()
    raise