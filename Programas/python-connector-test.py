# BIBLIOTECA
import mysql.connector

# PROGRAMA
print ("Conectandose a la base de datos")
cnx = mysql.connector.connect(user='OmarAb', password='kore', host='127.0.0.1', database='rfid')
print ("Conexión realizada")
cnx.close()
print ("Conexión cerrada")