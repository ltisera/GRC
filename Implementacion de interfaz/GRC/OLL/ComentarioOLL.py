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
    	return jsonify(comentarioDAO.traerComentariosDeReferencia(idReferencia))

    def eliminarComentario(self, idComentario):
    	rcomentarioDAO.eliminarComentario(idComentario)
