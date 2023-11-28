import mysql.connector


class Usuario:
    def __init__(self, id, nombre, correo):
        self.id = id
        self.nombre = nombre
        self.correo = correo


class ORM:
    def __init__(self, host, user, password, database):
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if self.conexion.is_connected():
            print('Conexión exitosa')

    def obtener_usuarios(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall()

        usuarios = []
        for resultado in resultados:
            usuario = Usuario(resultado[0], resultado[1], resultado[2])
            usuarios.append(usuario)

        cursor.close()
        return usuarios

    def cerrar_conexion(self):
        self.conexion.close()


mi_orm = ORM('tu_host', 'tu_usuario', 'tu_contraseña',
             'nombre_de_tu_base_de_datos')

lista_usuarios = mi_orm.obtener_usuarios()

for usuario in lista_usuarios:
    print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Correo: {usuario.correo}")

mi_orm.cerrar_conexion()
