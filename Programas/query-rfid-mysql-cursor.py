# BIBLIOTECAS
import mysql.connector

#Conexión
cnx = mysql.connector.connect(user='OmarAb', password='kore',
                              host='localhost',
                              database='codigoIoT')

# Cursor
cursor = cnx.cursor()


# Query
query = ("SELECT id,nombre,temperatura FROM clima WHERE nombre = 'OmarAb';")

# Ejecuta cursor


cursor.execute(query)

res = cursor.fetchall ()

for x in res:
    print (x)
