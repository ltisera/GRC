from Referencia import Referencia
from Categoria import Categoria
from Comentario import Comentario
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
                    categoria = self.traerCategoria(i)
                    if(categoria == None):
                        self.crearCategoria(i)
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
                self._micur.execute('INSERT INTO tag(`etiqueta`) values("{0}")'.format(categoria))
        except Error as e:
            print("Error al conectar con la BD", e)      
      

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

    

    def traerReferenciasDeGrupo(self, idGrupo):
        self.crearConexion()
        try:
            lista = []
            if (self._bd.is_connected()):
                self._micur.execute("SELECT r.idReferencia, r.cita, r.descripcion, r.link, r.fechaHora, u.nombre, u.apellido FROM referencia as r inner join usuario as u on r.idUsuario = u.idUsuario where r.idGrupo = {0}".format(idGrupo))
                reg = self._micur.fetchall()
                if reg is not None:
                    for r in reg:
                        lista.append(Referencia(idReferencia=r[0], cita=r[1], descripcion=r[2], link=r[3], fecha=r[4], usuario=r[5] + " " + r[6]))
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
        return lista


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

    def eliminarReferencia(self, idReferencia):
        self.crearConexion()
        try:
            if (self._bd.is_connected()):
                self._micur.execute('DELETE FROM comentario WHERE idReferencia = "{0}"'.format(idReferencia))
                self._micur.execute ('DELETE FROM tag_has_referencia WHERE idReferencia = "{0}"'.format(idReferencia)) 
                self._micur.execute('DELETE FROM referencia WHERE idReferencia = "{0}"'.format(idReferencia))     
                self._bd.commit()
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()     

    #def buscarReferencias(self):

    


