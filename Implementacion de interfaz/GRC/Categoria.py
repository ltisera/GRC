class Categoria():
    def __init__(self, etiqueta=""):
        self._idCategoria = None
        self._etiqueta = etiqueta

    @property
    def etiqueta(self):
    	return self._foo
    
    @etiqueta.setter
    def etiqueta(self, etiqueta):
    	self._etiqueta = etiqueta

    @property
    def idCategoria(self):
    	return self._idCategoria
    
    @idCategoria.setter
    def idCategoria(self, idCategoria):
    	self._idCategoria = idCategoria