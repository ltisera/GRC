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
                print(consulta)
                stat = self._micur.execute(consulta)
                self._micur.execute('SELECT * from grupo where idGrupo = (select max(idGrupo) from grupo)')
                idGrupo = self._micur.fetchone()[0]
                print("ACA: "+str(idGrupo))
                consulta = 'INSERT INTO grupo_has_usuario (`Grupo_idGrupo`, `Usuario_idUsuario`, `permisoUsuario`) values ("{0}", "{1}", "creador")'.format(idGrupo, usuarioCreador.idUsuario)
                self._micur.execute(consulta)
                self._bd.commit()
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
           

    def traerGrupos(self, idUsuario):
        self.crearConexion()
        lstGrupos = None
        try:
            if (self._bd.is_connected()):
                consulta = 'SELECT * from grupo inner join grupo_has_usuario on grupo.idGrupo = grupo_has_usuario.Grupo_idGrupo where grupo_has_usuario.Usuario_idUsuario = "{0}"'.format(idUsuario)
                lstGrupos = (self._micur.execute(consulta))
                print("consulta" + str(self._micur.execute(consulta)))
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
        return lstGrupos

    def agregarUsuarioAGrupo(self, usuario, permisoUsuario, grupo):
        self.crearConexion()
        try:
            if (self._bd.is_connected()):
                consulta = "INSERT INTO grupo_has_usuario(`Grupo_idGrupo`, `Usuario_idUsuario`, `permisoUsuario`) values("+grupo.getIdGrupo+","+ usuario.idUsuario+","+ permisoUsuario+")"
                lstGrupos.extend(self._micur.execute(consulta))
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
        return lstGrupos

    def traerGrupo(self, idGrupo):
        self.crearConexion()
        grupo = None 
        try:
            if (self._bd.is_connected()):
                consulta = 'SELECT * from grupo where grupo.idGrupo = "{}'.format(idGrupo)
                grupo = self._micur.execute(consulta)
        except Error as e:
            print("Error al conectar con la BD", e)
        finally:
            self.cerrarConexion()
        return grupo


    #def eliminarUsuarioDelGrupo(self):