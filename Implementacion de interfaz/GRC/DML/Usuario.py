class Usuario():
    def __init__(self, nombre="", apellido="",
                 email="", password="", idUsuario=None, adminGlobal="", usuarioValido=""):
        self._idUsuario = idUsuario
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._password = password
        self._adminGlobal = adminGlobal
        self._usuarioValido = usuarioValido
        

    @property
    def idUsuario(self):
        return self._idUsuario

    @idUsuario.setter
    def idUsuario(self, id):
        self._idUsuario = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = str(nombre)

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = str(apellido)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = str(email)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = str(password)

    @property
    def adminGlobal(self):
        return self._adminGlobal

    @adminGlobal.setter
    def adminGlobal(self, adminGlobal):
        self._adminGlobal = str(adminGlobal)

    @property
    def usuarioValido(self):
        return self._usuarioValido

    @usuarioValido.setter
    def usuarioValido(self, usuarioValido):
        self._usuarioValido = usuarioValido


    def __str__(self):
        return str("id: " + str(self.idUsuario) +
                   " Nombre: " + str(self.nombre) + " " +
                   str(self.apellido) + " Email: " +
                   str(self.email) + " Password: " +
                   str(self.password) + " adminGlobal: " +
                   str(self._adminGlobal) + " usuarioValido: " +
                   str(self._usuarioValido))

if __name__ == '__main__':
    usrtst = Usuario
    usrtst.nombre = "Nico"
    print(usrtst.nombre)
    print("Estoy en el main del ussr")
