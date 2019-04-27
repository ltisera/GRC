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
        print(hacerDIC)
        laLista = []
        for i in hacerDIC:
            diccios = {}
            diccios["idComentario"] = i.idComentario
            diccios["comentario"] = i.comentario
            diccios["fecha"] = i.fecha
            diccios["idReferencia"] = i.idReferencia
            laLista.append(diccios)

        print(" HACEME EL DICCIONARIO PIBEEEEE")
        print(laLista)
        print("Hecho")

        return jsonify(laLista)

    def eliminarComentario(self, idComentario):
        comentarioDAO.eliminarComentario(idComentario)
