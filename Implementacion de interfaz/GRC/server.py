from flask import Flask, render_template, send_from_directory, request, jsonify
from UsuarioDAO import UsuarioDAO
from Usuario import Usuario
from GrupoDAO import GrupoDAO
import json


app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/js/jquery-3.3.1.js')
def jsfile():
    return send_from_directory('static/js', 'jquery-3.3.1.js')


@app.route('/js/bootstrap.min.js')
def jsbootstrapfile():
    return send_from_directory('static/js', 'bootstrap.min.js')


@app.route('/css/bootstrap.min.css')
def cssbootstrapfile():
    return send_from_directory('static/css', 'bootstrap.min.css')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index2.html')


@app.route('/header1')
def header1():
    return render_template('header1.html')


@app.route('/header2')
def header2():
    return render_template('header2.html')


@app.route('/inicio', methods=['GET', 'POST'])
def inicio():
    return render_template('inicio.html')


@app.route('/grupos')
def grupos():
    return render_template('grupos.html')


@app.route('/publicar')
def publicar():
    return render_template('publicar.html')


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/crearUsuario', methods=['GET', 'POST'])
def crearUsuarioPOST():
    respuesta = crearUsuario(request)
    return str(respuesta)


@app.route('/cargarListaGrupo', methods=['GET', 'POST'])
def cargarListaGrupo():
    html = ""
    num = 404
    gdao = GrupoDAO()
    lstGrupos = gdao.traerGrupos(request.values["usuario"])
    if(len(lstGrupos) != 0):
        for g in lstGrupos:
            html += """<div class="col-lg-4">
                    <img div="grupoFoto" class="img-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" width="140" height="140">
                    <h2 div="grupoNombre" class="fondoBlanco">""" + g.nombre + """</h2>
                    <p div="grupoDescripcion" class="fondoBlanco">""" + g.descripcion + """</p>
                    <p><div id="Grupo"""+str(g.idGrupo)+""""class="btn btn-default btnGrupos">Entrar</div></p>
                    </div>\n\n"""
        num = 200
    return html, str(num)


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
        jResponse = " NO EXISTIS" , 404
    return jResponse, 200

    """
    Este Metodo funciona Correctamente
    return ("{nombre=" + objUsuario.nombre + "," +
            "id=" + str(objUsuario.idUsuario) + "," +
            "apellido=" + objUsuario.apellido + "," +
            "email=" + objUsuario.email + "}")
    """


def crearUsuario(request):
    udao = UsuarioDAO()
    nuevoUsuario = Usuario(request.values["apellido"],
                           request.values["nombre"],
                           request.values["email"],
                           request.values["password"])
    print("Intentando cargar",nuevoUsuario.aCadena())
    print("Bien")
    udao.agregarUsuario(nuevoUsuario)
    return 200



def validarUsuario(request):
    print("Printealo")
    print("Estoy imprimiendo")
    print("Usuario: " + request.values["usuario"])
    print("Pass: " + request.values["password"])
    print("Intentando traer usuario")
    udao = UsuarioDAO()
    elusr = udao.traerUsuarioXMail(request.values["usuario"])
    print(str(elusr))

    if(elusr.password == request.values["password"]):
        print("PIOLA LOCO, HABEMUS LOGIN")
    else:
        print("que mal no hay login")
        elusr = None
    return elusr


def traerUsuario(id):
    udao = UsuarioDAO()
    elusr = udao.traerUsuario(1)
    print("El usr es:" + elusr.password)
    return elusr


app.run(host='localhost', port="5000")