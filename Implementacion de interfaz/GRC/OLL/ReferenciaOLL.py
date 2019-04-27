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
        lstCategorias =[]
        for i in tags:
            categoria = categoriaOLL.traerCategoria(i)
            if(categoria is None):
                categoriaOLL.crearCategoria(i)
                categoria = categoriaOLL.traerCategoria(i)
            lstCategorias.append(categoria)
    	referenciaDAO.publicarReferencia(cita, descripcion, link, fecha, usuario, grupo, lstCategorias)

    def traerReferenciasDeGrupo(self, idGrupo):
        resp = referenciaDAO.traerReferenciasDeGrupo(idGrupo)
        print(resp)
        laLista = []
        for i in resp:
            diccios = {}
            diccios["idReferencia"] = i.idReferencia
            diccios["cita"] = i.cita
            diccios["link"] = i.link
            diccios["descripcion"] = i.descripcion
            diccios["fecha"] = i.fecha
            diccios["idUsuario"] = i.usuario
            diccios["idGrupo"] = i.grupo
            laLista.append(diccios)

        print(laLista)
        print("diccio referencia Hecho")
    	return jsonify(laLista)

    def eliminarReferencia(self, idReferencia):
    	referenciaDAO.eliminarReferencia(idReferencia)

    def buscarReferencias(self, idGrupo, busqueda):
    	return jsonify(referenciaDAO.buscarReferencias(idGrupo, busqueda))