from DML.Referencia import Referencia
from DML.Categoria import Categoria
from DML.Comentario import Comentario
# import mysql.connector
from mysql.connector import Error
from ConexionBD import ConexionBD
import datetime
DBGI = False


class CategoriaDAO(ConexionBD):
    def __init__(self):
        pass

    def traerCategoria(self, nombreCategoria):
        categoria = None
        try:
            if (self._bd.is_connected()):
                consulta = 'SELECT * from tag where tag.etiqueta = "{0}"'.format(nombreCategoria)
                self._micur.execute(consulta)
                for i in self._micur:
                    categoria = Categoria(i[0], i[1])

        except Error as e:
            print("Error al conectar con la BD", e)
        return categoria

    def crearCategoria(self, categoria):
        try:
            if (self._bd.is_connected()):
                self._micur.execute('INSERT INTO tag(`etiqueta`) values("{0}")'.format(categoria))
        except Error as e:
            print("Error al conectar con la BD", e)