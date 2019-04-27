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
                for categoria in tags:
                    self._micur.execute('INSERT INTO tag_has_referencia(`idTag`, `idReferencia`) values ("{0}", "{1}")'.format(categoria.idCategoria, idReferencia))
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
                self._micur.execute("SELECT r.idReferencia, r.cita, r.descripcion, r.link, r.fechaHora, u.nombre, u.apellido FROM referencia as r inner join usuario as u on r.idUsuario = u.idUsuario where r.idGrupo = {0} ORDER BY r.fechaHora DESC".format(idGrupo))
                reg = self._micur.fetchall()
                if reg is not None:
                    for r in reg:
                        lista.append(Referencia(idReferencia=r[0], cita=r[1], descripcion=r[2], link=r[3], fecha=r[4], usuario=r[5] + " " + r[6], grupo=idGrupo))
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
