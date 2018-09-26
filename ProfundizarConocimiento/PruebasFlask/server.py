from flask import Flask, render_template, send_from_directory, request, jsonify
from UsuarioDAO import UsuarioDAO
import json

app = Flask(__name__)


@app.route('/')
def inicio():
    return('<p>Estas en la raiz</p>')


@app.route('/js/jquery-3.3.1.js')
def jsfile():
    return send_from_directory('static/js', 'jquery-3.3.1.js')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/miajax', methods=['GET', 'POST'])
def miajax():
    objUsuario = validarUsuario(request)
    print("Este es el usuario que voy a devolver JSONIFYCADO")
    print("Y ESTE ES EL return")

    if(objUsuario is not None):
        jResponse = jsonify(nombre=objUsuario.nombre,
                            id=objUsuario.idUsuario,
                            apellido=objUsuario.apellido,
                            email=objUsuario.email)
    else:
        jResponse = " NO EXISTIS"
    return jResponse

    """
    Este Metodo funciona Correctamente
    return ("{nombre=" + objUsuario.nombre + "," +
            "id=" + str(objUsuario.idUsuario) + "," +
            "apellido=" + objUsuario.apellido + "," +
            "email=" + objUsuario.email + "}")
    """


def validarUsuario(request):
    print("Printealo")
    print("Usuario: " + request.values["ussr"])
    print("Pass: " + request.values["psswd"])
    print("Intentando traer usuario")
    udao = UsuarioDAO()
    elusr = udao.traerUsuarioXMail(request.values["ussr"])
    print(elusr.aCadena())

    if(elusr.password == request.values["psswd"]):
        print("PIOLA LOCO, HABEMUS LOGIN")
    else:
        elusr = None
    return elusr


def traerUsuario(id):
    udao = UsuarioDAO()
    elusr = udao.traerUsuario(1)
    print("El usr es:" + elusr.password)
    return elusr


app.run(host='localhost', port="5000")
