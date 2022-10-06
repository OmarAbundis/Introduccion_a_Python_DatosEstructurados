# BIBLIOTECAS

import mysql.connector

# Conexión

cnx = mysql.connector.connect(user='OmarAb', password='kore',
                              host='localhost',
                              database='codigoIoT')

# Cursor

cursor = cnx.cursor()
query_insert = "INSER INTO rfid (nombre, texto"

# Ejecutar cursor
cursor.execute (query_insert)

#Asergurarse de realizar la operación en DB

cnx.commit()
print ("Query ok")

# Cerrar
cursor.close()
cnx.close()


