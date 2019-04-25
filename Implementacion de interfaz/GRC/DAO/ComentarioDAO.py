from DML.Comentario import Comentario
# import mysql.connector
from mysql.connector import Error
from ConexionBD import ConexionBD
import datetime
DBGI = False


class ComentarioDAO(ConexionBD):
    def __init__(self):
        pass

    def comentarReferencia(self, comentario, referencia, fecha, usuario):
        self.crearConexion()
        try:
            if (self._bd.is_connected()):
                consulta = 'INSERT INTO comentario(`comentario`, `fechaHora`, `idReferencia`, `idUsuario`) values("{0}","{1}","{2}","{3}")'.format(comentario, fecha, referencia.idReferencia, usuario.idUsuario)
                self._micur.execute(consulta)
                self._bd.commit()
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()

    def traerComentariosDeReferencia(self, idReferencia):
        self.crearConexion()
        try:
            lista = []
            if (self._bd.is_connected()):
                self._micur.execute('SELECT c.idComentario, c.comentario, c.fechaHora, c.idReferencia, c.idUsuario FROM comentario as c inner join usuario as u on c.idUsuario = u.idUsuario inner join referencia as r on c.idReferencia = r.idReferencia')
                reg = self._micur.fetchall()
                if reg is not None:
                    for c in reg:
                        lista.append(Comentario(idComentario=c[0], comentario=c[1], fecha=c[2], idReferencia=c[3], idUsuario=c[4]))
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
        return lista

 def eliminarComentario(self, idComentario):
        self.crearConexion()
        try:
            if (self._bd.is_connected()):
                self._micur.execute('DELETE FROM comentario WHERE idComentario = "{0}"'.format(idComentario))
                self._bd.commit()
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()