class Comentario():
    def __init__(self,idComentario=None, comentario="", idReferencia="", fecha="", usuario=""):
        self._idComentario = None
        self._Comentario = comentario
        self._idReferencia = idReferencia
        self._fecha = fecha
        self._usuario = usuario

	@property
	def idComentario(self):
		return self._idComentario
	
	@idComentario.setter
	def