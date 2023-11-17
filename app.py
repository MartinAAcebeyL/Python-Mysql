import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Establecer la conexión a la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password=os.getenv("DATABASE_PASSWORD"),
    database='BRENTA'
)

if conexion.is_connected():
    print('Conexión exitosa')

# Ejemplo de consulta
cursor = conexion.cursor()
cursor.execute("SELECT * FROM casa")

# Obtener los resultados de la consulta
resultados = cursor.fetchall()

# Mostrar los resultados
for fila in resultados:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
