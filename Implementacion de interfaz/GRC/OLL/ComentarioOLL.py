from DML.Comentario import Comentario
from DAO.ComentarioDAO import ComentarioDAO
from flask import jsonify

comentarioDAO = ComentarioDAO()


class ComentarioOLL(object):
    def __init__(self):
        pass

    def comentarReferencia(self, comentario, referencia, fecha, usuario):
        comentarioDAO.comentarReferencia(comentario, referencia, fecha, usuario)

    def traerComentariosDeReferencia(self, idReferencia):
        hacerDIC = comentarioDAO.traerComentariosDeReferencia(idReferencia)
        laLista = []
        for i in hacerDIC:
            diccios = {}
            diccios["idComentario"] = i[0].idComentario
            diccios["comentario"] = i[0].comentario
            diccios["fecha"] = i[0].fecha
            diccios["idReferencia"] = i[0].idReferencia
            diccios["idUsuario"] = i[0].idUsuario
            diccios["nombreUsuario"] = i[1]
            laLista.append(diccios)


        return jsonify(laLista)

    def eliminarComentario(self, idComentario):
        comentarioDAO.eliminarComentario(idComentario)
