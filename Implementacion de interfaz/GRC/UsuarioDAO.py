from Usuario import Usuario
import mysql.connector
from mysql.connector import Error
import sys

DBGI = False

connectionDict = {
    'host': 'localhost',
    'user': 'admingrc',
    'password': '1234',
    'database': 'bdgrc'
}

class UsuarioDAO():
    def __init__(self):
        pass

    def cerrarCursor(self):
        self._micur.close()

    def crearConexion(self):
        if(DBGI):
            print("DBGI: Conectando a BD")
        """
        self._bd = mysql.connector.connect(
            host="localhost",
            user="admingrc",
            passwd="1234",
            database="bdgrc")
        """
        self._bd = mysql.connector.connect(**connectionDict)

        if(DBGI):
            print("DBGI:Conectado")
        if(DBGI):
            print("DBGI: Creando Cursor")
        self._micur = self._bd.cursor()
        if(DBGI):
            print("DBGI: cursor creado")


    def cerrarConexion(self):
        if(self._bd.is_connected()):
            if(DBGI):
                print("DBGI: cerrando cursor y conexion")
            self._micur = self._bd.cursor()
            self._bd.close()

    def traerUsuarioXMail(self, mimail):
        """Seguir haciendolo"""
        self.crearConexion()
        utraido = Usuario()
        try:
            if (self._bd.is_connected()):
                print("la consulta es:::")
                consulta = 'SELECT * FROM Usuario WHERE email = "{0}"'.format(mimail)
                print(consulta)
                reg = self._micur.execute(consulta)
                for i in self._micur:
                    utraido.idUsuario = i[0]
                    utraido.nombre = i[1]
                    utraido.apellido = i[2]
                    utraido.email = i[3]
                    utraido.password = i[4]
                if(DBGI):
                    print("Se Leyeron los datos en la BD")

        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
            return utraido

    def traerUsuarioXId(self, id):
        """Seguir haciendolo"""
        self.crearConexion()
        utraido = Usuario()
        try:
            if (self._bd.is_connected()):
                reg = self._micur.execute("SELECT * FROM Usuario WHERE idUsuario = {0}".format(id))
                for i in self._micur:
                    utraido.idUsuario = i[0]
                    utraido.nombre = i[1]
                    utraido.apellido = i[2]
                    utraido.email = i[3]
                    utraido.password = i[4]
                if(DBGI):
                    print("Se Leyeron los datos en la BD")

        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
            return utraido

    def traerUsuario(self, arg):
        usuario = None
        if(isinstance(arg, str)):
            usuario = self.traerUsuarioXMail(arg)
        elif(isinstance(arg, str)):
            usuario = self.traerUsuarioXId(arg)
        return usuario

    def agregarUsuario(self, usser):
        self.crearConexion()
        stat = self._micur.execute("INSERT INTO Usuario(nombre, apellido, email, password) VALUES('{0}','{1}','{2}','{3}')".format(usser.nombre, usser.apellido, usser.email, usser.password))
        self._bd.commit()
        self.cerrarConexion()


if __name__ == '__main__':
    udao = UsuarioDAO()
    elusr = udao.traerUsuario(1)
    print("Nombre" + elusr.nombre)
    print(elusr.aCadena())