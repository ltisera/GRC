








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

    def aCadena(self):
        return str("id: " + str(self._idUsuario) +
                " Nombre: " + self._nombre + " " +
                self._apellido + "Email: " +
                self._email + " Password: "
                + self._password)
    
    def __str__(self):
        return str("id: " + str(self._idUsuario) +
                " Nombre: " + self._nombre + " " +
                self._apellido + "Email: " +
                self._email + " Password: "
                + self._password)

if __name__ == '__main__':
    usrtst = Usuario
    usrtst.nombre = "Nico"
    print(usrtst.nombre)
    print("Estoy en el main del ussr")
