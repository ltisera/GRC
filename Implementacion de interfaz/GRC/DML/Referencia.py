class Referencia():
    def __init__(self, idReferencia=None, cita="", descripcion="", link="", fecha="", usuario="", grupo=""):
        self._idReferencia = idReferencia
        self._cita = cita
        self._descripcion = descripcion
        self._link = link
        self._fecha = fecha
        self._usuario = usuario
        self._grupo = grupo

    @property
    def idReferencia(self):
        return self._idReferencia
    
    @idReferencia.setter
    def idReferencia(self, idreferencia):
    	self._idReferencia = idreferencia

    @property
    def cita(self):
    	return self._cita
    @cita.setter
    def cita(self, cita):
    	self._cita = cita

    @property
    def descripcion(self):
    	return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
    	self._descripcion = descripcion

    @property
    def link(self):
    	return self._link

    @link.setter
    def link(self, link):
    	self._link = link

    @property
    def fecha(self):
    	return self._fecha
    
    @fecha.setter
    def fecha(self, fecha):
    	self._fecha = fecha

    @property
    def usuario(self):
    	return self._usuario
    
    @usuario.setter
    def usuario(self, usuario):
    	self._usuario = usuario

    @property
    def grupo(self):
   		return self._grupo

    @grupo.setter
    def grupo(self, grupo):
        self._grupo = grupo

    def __str__(self):
        return str("id: " + str(self.idReferencia) +
                   " Cita: " + str(self.cita) +
                   " Descripcion: " + str(self.descripcion) +
                   " link: " + str(self.link) +
                   " fecha: " + str(self.fecha) +
                   " usuario: " + str(self.usuario) +
                   " grupo: " + str(self.grupo))
