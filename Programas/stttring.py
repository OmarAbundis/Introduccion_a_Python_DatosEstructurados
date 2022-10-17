nombre = "Omar Abundis"
texto = "Texto del RFID"
rfid = 12345678

# INSERT INTO rfid (nombre,texto,rfid) VALUES ('Omar Ab','Test python 5',0123456);

query = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('" + nombre + "','" + texto + "'," + str(rfid) + ")"

print (query)
