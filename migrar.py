import sqlite3

conexion = sqlite3.connect("rentas.db")
cursor = conexion.cursor()

cursor.execute("UPDATE rentas SET amueblado = 'Sí', bano = 'Compartido', estacionamiento = 'No', cocina = 'Individual', servicios = 'Agua, Luz' WHERE id = 1")
cursor.execute("UPDATE rentas SET amueblado = 'Sí', bano = 'Privado', estacionamiento = 'Sí', cocina = 'Individual', servicios = 'Agua, Luz, Internet' WHERE id = 2")
cursor.execute("UPDATE rentas SET amueblado = 'Sí', bano = 'Privado', estacionamiento = 'No', cocina = 'Compartida', servicios = 'Agua, Luz, Internet' WHERE id = 3")

conexion.commit()
conexion.close()

print("Cambios hechos!!")