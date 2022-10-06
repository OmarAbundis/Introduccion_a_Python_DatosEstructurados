# BIBLIOTECAS
import mysql.connector

#Conexión
cnx = mysql.connector.connect(user='OmarAb', password='kore',host='127.0.0.1',database='codigoIoT')

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