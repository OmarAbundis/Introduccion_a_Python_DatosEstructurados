# BIBLIOTECAS
import mysql.connector

#Conexión
cnx = mysql.connector.connect(user='OmarLAN', password='1234*', host='192.168.1.64', database='rfid')

# Query
query = ("SELECT id,nombre,temperatura FROM clima WHERE id > 21;")

# Ejecución


res = cnx.cmd_query(query)

# Imprimir resultado

print ("Respuesta")
print (res)

# Cerrar
# cursor.close()

cnx.close()