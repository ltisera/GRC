from DML.Usuario import Usuario
import mysql.connector
from mysql.connector import Error
from ConexionBD import ConexionBD


class UsuarioDAO(ConexionBD):
    def __init__(self):
        pass

    def agregarUsuario(self, usser):
        """Agrega un usuario, validando que el mail contenga "@"
            :Parameters:
                -'usser': Usuario que desea agregarse
            :Return:
                (valido, str):
                    -"valido":
                        True si se agrego a la BD
                        False si no se agrego

                    -"mensaje" :
                        un mensaje de por que no se pudo agregar
            TO-DO: -Corregir mensajes de devolucion
        """
        valido = False
        try:
            self.crearConexion()

            consulta = "INSERT INTO Usuario(nombre, apellido, email, password) \
                        VALUES('{0}','{1}','{2}','{3}')".format(usser.nombre,
                                                                usser.apellido,
                                                                usser.email,
                                                                usser.password)
            mailValido = False
            for i in usser.email:
                if(i == "@"):
                    mailValido = True
            if(mailValido is True):
                self._micur.execute(consulta)
                self._bd.commit()
                valido = True
            else:
                valido = "No lo se rick, parece falso"

        except mysql.connector.errors.IntegrityError as e:
            valido = "Usuario Usuario Duplicado"

        finally:
            self.cerrarConexion()

        return valido

    """
    Chequear estos metodos
    """

    def traerUsuarioXMail(self, mimail):
        """Seguir haciendolo"""
        utraido = None
        try:
            self.crearConexion()
            if (self._bd.is_connected()):
                consulta = 'SELECT * FROM Usuario WHERE \
                            email = "{0}"'.format(mimail)

                self._micur.execute(consulta)
                resultado = self._micur.fetchone()
                i = resultado
                utraido = Usuario(i[1], i[2], i[3], i[4], i[0])

        except Error as e:
            print("Error al conectar con la BD", e)

        finally:
            self.cerrarConexion()
            return utraido

    def traerUsuarioXId(self, id):
        """Seguir haciendolo"""
        utraido = Usuario()
        try:
            self.crearConexion()
            if (self._bd.is_connected()):
                consulta = "SELECT * FROM Usuario WHERE \
                            idUsuario = {0}".format(id)

                self._micur.execute(consulta)
                for i in self._micur:
                    utraido.idUsuario = i[0]
                    utraido.nombre = i[1]
                    utraido.apellido = i[2]
                    utraido.email = i[3]
                    utraido.password = i[4]

        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
            return utraido

    def traerUsuario(self, arg):
        usuario = None
        if(isinstance(arg, str)):
            usuario = self.traerUsuarioXMail(arg)
        elif(isinstance(arg, int)):
            usuario = self.traerUsuarioXId(arg)
        return usuario

    """
        Implementar estos metodos
    """

    def modificarUsuario(self, id):
        pass

    def eliminarUsurio(self, id):
        pass


if __name__ == '__main__':
    print("iniciando la pruba unitaria para UsuarioDAO")
    udao = UsuarioDAO()
    nus = Usuario("nata", "lia", "sipu@contador.com", "1234")
    st = udao.agregarUsuario(nus)
    if(st is not True):
        print(st)

    us = udao.traerUsuario("mas")
    print("trajo el usuario:")

    print(us.__str__())

