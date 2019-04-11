from DML.Usuario import Usuario
from DAO.UsuarioDAO import UsuarioDAO


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
                resp["mensaje"] = "Exploto al agregarUsuario"
        else:
            resp["status"] = 200
            resp["mensaje"] = "El mail ya esta registrado"

        return resp
