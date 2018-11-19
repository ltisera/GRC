class Categoria():
    def __init__(self, idCategoria=None,etiqueta=""):
        self._idCategoria = idCategoria
        self._etiqueta = etiqueta

    @property
    def etiqueta(self):
    	return self._etiqueta
    
    @etiqueta.setter
    def etiqueta(self, etiqueta):
    	self._etiqueta = etiqueta

    @property
    def idCategoria(self):
    	return self._idCategoria
    
    @idCategoria.setter
    def idCategoria(self, idCategoria):
    	self._idCategoria = idCategoria

    def __str__(self):
    	return str("idCategoria: "+str(self.idCategoria)+" etiqueta: "+self.etiqueta)