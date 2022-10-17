# BIBLIOTECAS
import mysql.connector

#Conexión
cnx = mysql.connector.connect(user='OmarLAN', password='1234*', host='127.0.0.1', database='rfid')

# Cursor
cursor = cnx.cursor()


# Query
query = ("SELECT * FROM rfid WHERE id = 3;")

# Ejecuta cursor


cursor.execute(query)

res = cursor.fetchall ()

for x in res:
    print (x)
