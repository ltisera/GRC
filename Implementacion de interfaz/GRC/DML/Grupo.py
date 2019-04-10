class Grupo():
    def __init__(self, nombre="", descripcion="", usuarioCreador="", idG=None):
        self._idGrupo = idG
        self._nombre = nombre
        self._descripcion = descripcion
        self._usuarioCreador = usuarioCreador
       

    @property
    def idGrupo(self):
        return self._idGrupo

    @idGrupo.setter
    def idGrupo(self, id):
        self._idGrupo = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def usuarioCreador(self):
        return self._usuarioCreador

    @usuarioCreador.setter
    def usuarioCreador(self, usuarioCreador):
        self._usuarioCreador = usuarioCreador

    def __str__(self):
        return str("id: " + str(self.idGrupo) +
                " Nombre: " + self.nombre + " Descripcion: " +
                self.descripcion + " Usuario creador: [" +
                str(self.usuarioCreador) + "]")

