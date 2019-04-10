from DML.Grupo import Grupo
from DAO.GrupoDAO import GrupoDAO
import json

grupoDao = GrupoDAO()


class GrupoOLL(object):
    def __init__(self):
        pass
        
    def crearGrupo(self, nombre, descripcion, usuarioCreador):
        grupoDao.crearGrupo(nombre, descripcion, usuarioCreador)

    def traerGrupos(self):
        return jsonify(grupoDao.traerGrupos())

    def traerGruposDeUsuario(self, idUsuario):
        html = ""
        num = 404
        lstGrupos = grupoDao.traerGruposDeUsuario(idUsuario)
        if(len(lstGrupos) != 0):
            print("ACA TENEMOS EL PRINT DE MMM GRUPOS?")
            print(lstGrupos)
            respuesta = jsonify(lstGrupos)    
            num = 200
        return respuesta, str(num)

    def agregarUsuarioAGrupo(self, usuario, permisoUsuario, grupo):
        if(usuario!=None and not (grupo in traerGruposDeUsuario(usuario))):
            grupoDao.agregarUsuarioAGrupo(usuario, permisoUsuario, grupo)

    def traerGrupo(self, idGrupo):
        return grupoDao.traerGrupo(idGrupo)

    def consultarPermisos(self, usuario, grupo):
        permiso = None
        if(usuario!=None and grupo in traerGruposDeUsuario(usuario)):
            permiso = grupoDao.consultarPermisos(usuario, grupo)
        return permiso

    def eliminarUsuarioDelGrupo(self, usuario, grupo):
        if(usuario!=None and grupo in traerGruposDeUsuario(usuario)):
            grupoDao.eliminarUsuarioDelGrupo(usuario, grupo)