from DML.Grupo import Grupo
from DAO.GrupoDAO import GrupoDAO
from flask import jsonify

grupoDao = GrupoDAO()


class GrupoOLL(object):
    def __init__(self):
        pass

    def crearGrupo(self, nombre, descripcion, usuarioCreador):
        return jsonify(grupoDao.crearGrupo(nombre, descripcion, usuarioCreador))

    def traerGrupos(self):
        return jsonify(grupoDao.traerGrupos())

    def traerGruposDeUsuario(self, idUsuario):
        html = ""
        num = 404
        respuesta = None
        lstGrupos = grupoDao.traerGruposDeUsuario(idUsuario)
        if(len(lstGrupos) != 0):
            respuesta = lstGrupos
            num = 200
        else:
            num = 200
        return jsonify(respuesta, str(num))

    def agregarUsuarioAGrupo(self, idUsuario, permisoUsuario, idGrupo):
        msg = None
        status = 200
        if(grupoDao.estaUsuarioEnGrupo(idUsuario, idGrupo) == False):
            if(grupoDao.agregarUsuarioAGrupo(idUsuario, permisoUsuario, idGrupo) is True):
                msg = "Usuario Agregado"
            else:
                msg = "Error al agregar el usuario"

        else:
            msg = "El usuario ya pertenence al grupo"

        return jsonify(status,msg)


    def traerGrupo(self, idGrupo):
        return grupoDao.traerGrupo(idGrupo)

    def consultarPermisos(self, usuario, grupo):
        permiso = None
        if(usuario!=None and grupo in traerGruposDeUsuario(usuario)):
            permiso = grupoDao.consultarPermisos(usuario, grupo)
        return jsonify(permiso)

    def eliminarUsuarioDelGrupo(self, usuario, grupo):
        if(usuario!=None and grupo in traerGruposDeUsuario(usuario)):
            grupoDao.eliminarUsuarioDelGrupo(usuario, grupo)