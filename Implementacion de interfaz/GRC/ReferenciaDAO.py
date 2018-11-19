from Referencia import Referencia
from Categoria import Categoria
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

class ReferenciaDAO():
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


    def publicarReferencia(self, cita, descripcion, link, fecha, usuario, grupo, tags):
        self.crearConexion()
        try:
            if (self._bd.is_connected()):
                consulta = 'INSERT INTO referencia(`cita`, `descripcion`, `link`, `fechaHora`, `idUsuario`, `idGrupo`) values("{0}","{1}","{2}","{3}","{4}","{5}")'.format(cita, descripcion, link, fecha, usuario.idUsuario, grupo.idGrupo)
                self._micur.execute(consulta)
                self._micur.execute('SELECT * from referencia where idReferencia = (select max(idReferencia) from referencia)')
                idReferencia = self._micur.fetchone()[0]
                for i in tags:
                    categoria = self.traerCategoria(str(i))
                    print("I: "+str(i)+" categoria: "+str(categoria))
                    if(categoria == None):
                        self.crearCategoria(str(i))
                        categoria = self.traerCategoria(i)
                    self._micur.execute('INSERT INTO tag_has_referencia(`idTag`, `idReferencia`) values ("{0}", "{1}")'.format(categoria.idCategoria, idReferencia))
                self._bd.commit()
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()


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
                self._micur.execute('INSERT INTO tag(`etiqueta`) values("{0}")'.format(str(i)))
        except Error as e:
            print("Error al conectar con la BD", e)

    #def comentarReferencia(self):

    #def eliminarReferencia(self):

    #def traerReferenciasDeGrupo(self):

    #def buscarReferencias(self):
