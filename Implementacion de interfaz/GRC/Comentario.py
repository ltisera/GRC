class Comentario():
    def __init__(self,idComentario=None, comentario="", idReferencia="", fecha="", idUsuario=""):
        self._idComentario = idComentario
        self._comentario = comentario
        self._idReferencia = idReferencia
        self._fecha = fecha
        self._idUsuario = idUsuario


    @property
    def idComentario(self):
        return self._idComentario
    
    @idComentario.setter
    def idComentario(self, idComentario):
        self._idComentario = idComentario

    @property
    def comentario(self):
        return self._comentario

    @comentario.setter
    def comentario(self, comentario):
        self._Comentario = comentario
    
    @property
    def idReferencia(self):
        return self._idReferencia
    
    @idReferencia.setter
    def idReferencia(self, idReferencia):
        self._idReferencia = idReferencia

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def idUsuario(self):
        return self._idUsuario

    def __str__(self):
        return str("idComentario: "+str(self.idComentario)+" comentario: "+str(self.comentario)+" fecha: "+str(self.fecha)+" idUsuario: "+str(self.idUsuario))