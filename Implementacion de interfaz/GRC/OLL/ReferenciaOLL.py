from DML.Referencia import Referencia
from DAO.ReferenciaDAO import ReferenciaDAO
from OLL.CategoriaOLL import CategoriaOLL
from flask import jsonify

referenciaDAO = ReferenciaDAO()
categoriaOLL = CategoriaOLL()


class ReferenciaOLL(object):
    def __init__(self):
        pass

    def publicarReferencia(self, cita, descripcion, link, fecha, usuario, grupo, tags):
        for i in tags:
            categoria = categoriaOLL.traerCategoria(i)
            if(categoria is None):
                categoriaOLL.crearCategoria(i)
    	referenciaDAO.publicarReferencia(cita, descripcion, link, fecha, usuario, grupo, tags)

    def traerReferenciasDeGrupo(self, idGrupo):
        resp = referenciaDAO.traerReferenciasDeGrupo(idGrupo)
        print("ACA TE LO PRINTEO ATENCIONNNNNNNNNNNN")
        print(resp)
    	return jsonify(resp)

    def eliminarReferencia(self, idReferencia):
    	referenciaDAO.eliminarReferencia(idReferencia)

    def buscarReferencias(self, idGrupo, busqueda):
    	return jsonify(referenciaDAO.buscarReferencias(idGrupo, busqueda))