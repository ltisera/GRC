import sys

import mysql.connector
from mysql.connector import Error

from DML.Grupo import Grupo
from ConexionBD import ConexionBD


class GrupoDAO(ConexionBD):
    def crearGrupo(self, nombre, descripcion, usuarioCreador):
        self.crearConexion()
        # grupoCreado = Grupo(nombre, descripcion, usuarioCreador)
        resp = 0
        try:
            consulta = 'INSERT INTO grupo (`nombre`, `descripcion`) values ("{0}", "{1}")'.format(nombre, descripcion)
            stat = self._micur.execute(consulta)
            self._micur.execute('SELECT * from grupo where idGrupo = (select max(idGrupo) from grupo)')
            idGrupo = self._micur.fetchone()[0]
            consulta = 'INSERT INTO grupo_has_usuario (`Grupo_idGrupo`, `Usuario_idUsuario`, `permisoUsuario`) values ("{0}", "{1}", "creador")'.format(idGrupo, usuarioCreador)
            self._micur.execute(consulta)
            self._bd.commit()
            resp = 200
        except Error as e:
            print("Error al cargar grupo en la BD", e)
            resp = 500
        finally:
            self.cerrarConexion()
        return resp
    def traerGrupos(self):
        self.crearConexion()
        dctGrupos = None
        try:
            if (self._bd.is_connected()):
                consulta = 'SELECT * from grupo'
                self._micur.execute(consulta)
                dctGrupos = self._micur.fetchall()
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
        return dctGrupos

    def traerGruposDeUsuario(self, idUsuario):
        self.crearConexion()
        try:
            lista = []
            if (self._bd.is_connected()):
                self._micur.execute("SELECT grupo.idGrupo, grupo.nombre, grupo.descripcion, gxu.permisoUsuario from grupo inner join grupo_has_usuario as gxu on grupo.idGrupo = gxu.Grupo_idGrupo where gxu.Usuario_idUsuario = {0}".format(idUsuario))
                reg = self._micur.fetchall()
                """if reg is not None:
                    for g in reg:
                        lista.append(Grupo(idG=g[0], nombre=g[1], descripcion=g[2]))
                """
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
        return reg

    def agregarUsuarioAGrupo(self, idUsuario, permisoUsuario, idGrupo):
        self.crearConexion()
        resp = None
        try:
            if (self._bd.is_connected()):
                consulta = 'INSERT INTO grupo_has_usuario(`Grupo_idGrupo`, `Usuario_idUsuario`, `permisoUsuario`) values("{0}","{1}","{2}")'.format(idGrupo, idUsuario, permisoUsuario)
                self._micur.execute(consulta)
                self._bd.commit()
                resp = True
        except Error as e:
            resp = False
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
        
        return resp

    def traerGrupo(self, idGrupo):
        self.crearConexion()
        grupo = Grupo()
        try:
            if (self._bd.is_connected()):
                consulta = 'SELECT * from grupo where grupo.idGrupo = "{}"'.format(idGrupo)
                self._micur.execute(consulta)
                for i in self._micur:
                    grupo.idGrupo = i[0]
                    grupo.nombre = i[1]
                    grupo.descripcion = i[2]
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
        return grupo



    def consultarPermisos(self, usuario, grupo):
        self.crearConexion()
        permiso = None
        try:
            if (self._bd.is_connected()):
                consulta = 'SELECT permisoUsuario from grupo_has_usuario where Grupo_idGrupo = "{0}" and Usuario_idUsuario = "{1}"'.format(grupo.idGrupo, usuario.idUsuario)
                self._micur.execute(consulta)
                permiso = self._micur.fetchone()[0]
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
        return permiso

    def estaUsuarioEnGrupo(self, idUsuario, idGrupo):
        self.crearConexion()
        permiso = None
        try:
            if (self._bd.is_connected()):
                consulta = 'SELECT * from grupo_has_usuario where Grupo_idGrupo = "{0}" and Usuario_idUsuario = "{1}"'.format(idGrupo, idUsuario)
                self._micur.execute(consulta)
                if(self._micur.fetchone() is None):
                    permiso = False
                else:
                    permiso = True
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
        return permiso

    def eliminarUsuarioDelGrupo(self, usuario, grupo):
        self.crearConexion()
        try:
            if (self._bd.is_connected()):
                consulta = 'DELETE FROM grupo_has_usuario where Grupo_idGrupo = "{0}" and Usuario_idUsuario = "{1}"'.format(grupo.idGrupo, usuario.idUsuario)
                self._micur.execute(consulta)
                self._bd.commit()
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()

if __name__ == '__main__':
    print("Test de traerGrupo:")
    gdao = GrupoDAO()
    print(gdao.traerGrupos())