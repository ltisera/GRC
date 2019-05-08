from OLL.DAO.DML.Categoria import Categoria
from OLL.DAO.CategoriaDAO import CategoriaDAO
from flask import jsonify

categoriaDAO = CategoriaDAO()


class CategoriaOLL(object):
    def __init__(self):
        pass

    def traerCategoria(self, nombreCategoria):
    	return categoriaDAO.traerCategoria(nombreCategoria)

    def crearCategoria(self, categoria):
    	categoriaDAO.crearCategoria(categoria)