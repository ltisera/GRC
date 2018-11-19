from Grupo import Grupo
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

class GrupoDAO():
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

    def crearGrupo(self, nombre, descripcion, usuarioCreador):
        self.crearConexion()
        grupoCreado = Grupo(nombre, descripcion, usuarioCreador)
        try:
            if (self._bd.is_connected()):
                consulta = 'INSERT INTO grupo (`nombre`, `descripcion`) values ("{0}", "{1}")'.format(nombre, descripcion)
                stat = self._micur.execute(consulta)
                self._micur.execute('SELECT * from grupo where idGrupo = (select max(idGrupo) from grupo)')
                idGrupo = self._micur.fetchone()[0]
                consulta = 'INSERT INTO grupo_has_usuario (`Grupo_idGrupo`, `Usuario_idUsuario`, `permisoUsuario`) values ("{0}", "{1}", "creador")'.format(idGrupo, usuarioCreador.idUsuario)
                self._micur.execute(consulta)
                self._bd.commit()
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
           

    def traerGrupos(self, idUsuario):
        self.crearConexion()
        try:
            lista = []
            if (self._bd.is_connected()):
                self._micur.execute("SELECT grupo.idGrupo, grupo.nombre, grupo.descripcion from grupo inner join grupo_has_usuario as gxu on grupo.idGrupo = gxu.Grupo_idGrupo where gxu.Usuario_idUsuario = {0}".format(idUsuario))
                reg = self._micur.fetchall()
                if reg is not None:
                    for g in reg:
                        lista.append(Grupo(idG=g[0], nombre=g[1], descripcion=g[2]))

        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
        return lista

    def agregarUsuarioAGrupo(self, usuario, permisoUsuario, grupo):
        self.crearConexion()
        try:
            if (self._bd.is_connected()):
                consulta = 'INSERT INTO grupo_has_usuario(`Grupo_idGrupo`, `Usuario_idUsuario`, `permisoUsuario`) values("{0}","{1}","{2}")'.format(grupo.idGrupo, usuario.idUsuario, permisoUsuario)
                self._micur.execute(consulta)
                self._bd.commit()
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
        

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