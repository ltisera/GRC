from DML.Usuario import Usuario
from DAO.UsuarioDAO import UsuarioDAO
from flask import jsonify

class UsuarioOLL():
    """docstring for UsuarioOLL"""

    def __init__(self):
        pass

    def crearUsuario(self, request):
        udao = UsuarioDAO()

        nuevoUsuario = Usuario(request.values["apellido"],
                               request.values["nombre"],
                               request.values["email"],
                               request.values["password"])

        resp = {}
        resp["status"] = 300
        resp["mensaje"] = "Nada por hacer"
        if(udao.traerUsuarioXMail(request.values["email"]) is None):
            stAgregarUsuario = udao.agregarUsuario(nuevoUsuario)

            if(stAgregarUsuario is True):
                resp["status"] = 200
                resp["mensaje"] = "Se agrego Correctamente"
            else:
                resp["status"] = 400
                resp["mensaje"] = str(stAgregarUsuario)
        else:
            resp["status"] = 200
            resp["mensaje"] = "El mail ya esta registrado"

        return resp

    def validarUsuario(self, request):
        udao = UsuarioDAO()
        usuarioTraido = udao.traerUsuarioXMail(request.values["usuario"])
        resp = jsonify(error="Usuario o password incorrectos")
        status = 400

        if usuarioTraido is not None:
            print("usuario traido: ", usuarioTraido)
            if(usuarioTraido.usuarioValido == 0):
                print("usuario invalido")
                status = 400
                resp = jsonify(error="El usuario no fue validado.")
            elif(usuarioTraido.password == request.values["password"]):
                status = 200
                resp = jsonify(nombre=usuarioTraido.nombre,
                            id=usuarioTraido.idUsuario,
                            apellido=usuarioTraido.apellido,
                            email=usuarioTraido.email)

        return (resp, status)
