from DML.Referencia import Referencia
from DML.Categoria import Categoria
from DML.Comentario import Comentario
# import mysql.connector
from mysql.connector import Error
from ConexionBD import ConexionBD
import datetime
DBGI = False


class ReferenciaDAO(ConexionBD):
    def __init__(self):
        pass

    def publicarReferencia(self, cita, descripcion, link, fecha, usuario, grupo, tags):
        self.crearConexion()
        try:
            if (self._bd.is_connected()):
                consulta = 'INSERT INTO referencia(`cita`, `descripcion`, `link`, `fechaHora`, `idUsuario`, `idGrupo`) values("{0}","{1}","{2}","{3}","{4}","{5}")'.format(cita, descripcion, link, fecha, usuario, grupo)
                self._micur.execute(consulta)
                self._micur.execute('SELECT * from referencia where idReferencia = (select max(idReferencia) from referencia)')
                idReferencia = self._micur.fetchone()[0]
                for i in tags:
                    categoria = self.traerCategoria(i)
                    if(categoria is None):
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
                        lista.append(Referencia(idReferencia=r[0], cita=r[1], descripcion=r[2], link=r[3], fecha=r[4], usuario=r[5] + " " + r[6], grupo=idGrupo))
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

    def buscarReferencias(self, idGrupo, busqueda):
        self.crearConexion()
        consulta = 'SELECT * FROM bdgrc.referencia as r inner join tag_has_referencia as tr on r.idReferencia = tr.idReferencia inner join tag as t on tr.idTag = t.idTag where (r.cita like "{0}" or r.descripcion like "{0}" or r.link like "{0}" or t.etiqueta like "{0}") and r.idGrupo = "{1}"'.format(("%"+busqueda+"%"), idGrupo)
        try:
            lista = []
            if (self._bd.is_connected()):
                self._micur.execute(consulta)
                reg = self._micur.fetchall()
                if reg is not None:
                    for r in reg:
                        lista.append(Referencia(idReferencia=r[0], cita=r[1], descripcion=r[2], link=r[3], fecha=r[4], usuario=r[5], grupo=r[6] ))
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
        return lista
