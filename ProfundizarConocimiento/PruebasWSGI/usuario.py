








class Usuario():
    def __init__(self, nombre="", apellido="", email="", password=""):
        self._idUsuario = None
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._password = password
        

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
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def aCadena(self):
        return ("id: " + str(self.idUsuario) +
                " Nombre: " + self.nombre + " " +
                self.apellido + "\nE-mail: " +
                self.email + " Password: "
                + self.password)

if __name__ == '__main__':
    usrtst = Usuario
    usrtst.nombre = "Nico"
    print(usrtst.nombre)
    print("Estoy en el main del ussr")
