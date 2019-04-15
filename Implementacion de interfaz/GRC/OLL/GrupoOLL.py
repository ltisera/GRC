from DML.Grupo import Grupo
from DAO.GrupoDAO import GrupoDAO
from flask import jsonify

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
        respuesta = None
        lstGrupos = grupoDao.traerGruposDeUsuario(idUsuario)
        if(len(lstGrupos) != 0):
            print("ACA TENEMOS EL PRINT DE MMM GRUPOS?")
            print(lstGrupos)
            respuesta = lstGrupos
            num = 200
        else:
            print("ACA TENEMOS EL PRINT vacio")
            print(lstGrupos)
            num = 200
        return jsonify(respuesta, str(num))

    def agregarUsuarioAGrupo(self, usuario, permisoUsuario, grupo):
        if(usuario!=None and not (grupo in traerGruposDeUsuario(usuario))):
            grupoDao.agregarUsuarioAGrupo(usuario, permisoUsuario, grupo)

    def traerGrupo(self, idGrupo):
        return grupoDao.traerGrupo(idGrupo)

    def consultarPermisos(self, usuario, grupo):
        permiso = None
        if(usuario!=None and grupo in traerGruposDeUsuario(usuario)):
            permiso = grupoDao.consultarPermisos(usuario, grupo)
            print("rev PERMISO")
            print(jsonify(permiso))
        return jsonify(permiso)

    def eliminarUsuarioDelGrupo(self, usuario, grupo):
        if(usuario!=None and grupo in traerGruposDeUsuario(usuario)):
            grupoDao.eliminarUsuarioDelGrupo(usuario, grupo)