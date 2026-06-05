import sqlite3

# Conectarse a la base de datos
# Si el archivo no existe, SQLite lo crea automáticamente
conexion = sqlite3.connect("rentas.db")
cursor = conexion.cursor()

# Crear la tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS rentas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        direccion TEXT,
        precio INTEGER,
        contacto TEXT
    )
""")

# Insertar datos de prueba
cursor.execute("""
    INSERT INTO rentas (titulo, direccion, precio, contacto)
    VALUES ('Cuarto en Zona Centro', 'Calle Morelos #45', 2500, '771-123-4567')
""")

cursor.execute("""
    INSERT INTO rentas (titulo, direccion, precio, contacto)
    VALUES ('Departamento cerca del Tec', 'Av. Universidad #12', 3800, '771-987-6543')
""")

cursor.execute("""
    INSERT INTO rentas (titulo, direccion, precio, contacto)
    VALUES ('Cuarto amueblado UAEH', 'Blvd. Juárez #89', 2000, '771-456-7890')
""")

# Guardar los cambios y cerrar
conexion.commit()
conexion.close()

print("Base de datos creada correctamente ✅")