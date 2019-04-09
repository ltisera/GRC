from flask import Flask, render_template, send_from_directory, request, jsonify
from UsuarioDAO import UsuarioDAO
from Usuario import Usuario
from GrupoDAO import GrupoDAO
from ReferenciaDAO import ReferenciaDAO
import json


app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/js/jquery-3.3.1.js')
def jsfile():
    return send_from_directory('static/js', 'jquery-3.3.1.js')


@app.route('/js/bootstrap.min.js')
def jsbootstrapfile():
    return send_from_directory('static/js', 'bootstrap.min.js')

@app.route('/sumer/dist/summernote.js')
def sumernotejs():
    return send_from_directory('static/sumer/dist', 'summernote.js')


@app.route('/sumer/dist/summernote.css')
def csssumernote():
    return send_from_directory('static/sumer/dist', 'summernote.css')

@app.route('/css/bootstrap.min.css')
def cssbootstrapfile():
    return send_from_directory('static/css', 'bootstrap.min.css')

@app.route('/static/css/estilos.css')
def cssestilos():
    return send_from_directory('static/css','estilos.css')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


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
    print("Dale que va")
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


@app.route('/traerTodosGrupos')
def traerTodosGrupos():
    gdao = GrupoDAO()

    return jsonify(gdao.traerGrupos())


@app.route('/crearUsuario', methods=['GET', 'POST'])
def crearUsuarioPOST():
    respuesta = crearUsuario(request)
    return str(respuesta)


@app.route('/cargarListaGrupo', methods=['GET', 'POST'])
def cargarListaGrupo():
    html = ""
    num = 404
    gdao = GrupoDAO()
    lstGrupos = gdao.traerGruposDeUsuario(request.values["usuario"])
    if(len(lstGrupos) != 0):
        print("ACA TENEMOS EL PRINT DE MMM GRUPOS?")
        print(lstGrupos)
        respuesta = jsonify(lstGrupos)    
        num = 200
    return respuesta, str(num)


@app.route('/cargarListaReferencias', methods=['GET', 'POST'])
def cargarListaReferencias():
    html = ""
    num = 404
    rdao = ReferenciaDAO()
    lista = rdao.traerReferenciasDeGrupo(request.values["grupo"])
    if(len(lista) != 0):
        for r in lista:
            html += """ <div class="well">
                        <div class="media">
                        <div class="media-body">
                            <h2 class="media-heading">""" + r.link + """</h2>
                            <p class="text-right">Por""" + r.usuario + """</p>
                            <p class="text-left">""" + r.cita + """</p>
                            <p class="text-left">""" + r.descripcion + """</p>
                            <br>
                            <ul class="list-inline list-unstyled">
                                <li><span><i class="glyphicon glyphicon-calendar"></i>""" + str(r.fecha) + """</span></li>
                                <li><span><i class="glyphicon glyphicon-comment"></i> X comentarios</span></li>
                            </ul>
                        </div>
                        </div>
                        </div>\n\n"""
        num = 200
    return html, str(num)


@app.route('/loguearUsuario', methods=['GET', 'POST'])
def loguearUsuario():
    objUsuario = validarUsuario(request)
    print("Este es el usuario que voy a devolver JSONIFYCADO")
    print("Y ESTE ES EL return")

    if(objUsuario is not None):
        print("Tirand")
        jResponse = jsonify(nombre=objUsuario.nombre,
                            id=objUsuario.idUsuario,
                            apellido=objUsuario.apellido,
                            email=objUsuario.email)
        
    else:
        print("Errorr")
        jResponse = 404
    
    return jResponse

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
    print("Intentando cargar",nuevoUsuario.__str__())
    print("Bien")
    stAgregarUsuario = udao.agregarUsuario(nuevoUsuario)
    if(stAgregarUsuario is True):
        print("Se agrego Correctamente")
    else:
        print("Error", stAgregarUsuario)
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

@app.route('/crearGrupo', methods=['GET', 'POST'])
def crearGrupo():
    gdao = GrupoDAO()
    gdao.crearGrupo(request.values["nombreGrupo"], request.values["descripcion"], request.values["usuarioCredor"])
    jResponse = 200
    return jResponse

@app.route('/invitarUsuario', methods=['GET', 'POST'])
def invitarUsuario():
    udao = UsuarioDAO()
    gdao = GrupoDAO()
    user = udao.traerUsuarioXMail(request.values["usuario"])
    grupo = gdao.traerGrupo(request.values["grupoid"])

    if(user is not None):
        gdao.agregarUsuarioAGrupo(user,request.values["permisoUsuario"],grupo)
        jResponse = 200
        
    else:
        print("El usuario no existe")
        jResponse = 404

    return jResponse

@app.route('/publicarReferencia', methods=['GET', 'POST'])
def publicarReferencia():
    refdao = ReferenciaDAO()
    refdao.publicarReferencia(request.values["cita"], request.values["descripcion"], request.values["link"],
        request.values["fecha"], request.values["usuario"], request.values["grupo"], request.values["tags"])
    jResponse = 200
    return jResponse

@app.route('/comentarReferencia', methods=['GET', 'POST'])
def comentarReferencia():
    refdao = ReferenciaDAO()
    refdao.comentarReferencia(request.values["comentario"], request.values["referencia"], request.values["fecha"], request.values["usuario"])
    jResponse = 200
    return jResponse

@app.route('/eliminarReferencia', methods=['GET', 'POST'])
def eliminarReferencia():
    refdao = ReferenciaDAO()
    refdao.eliminarReferencia(request.values["idReferencia"])
    jResponse = 200
    return jResponse
       
@app.route('/buscarReferencia', methods=['GET', 'POST'])
def buscarReferencia():
    html = ""
    num = 404
    refdao = ReferenciaDAO()
    lista = refdao.buscarReferencia(request.values["idGrupo"], request.values["busqueda"])
    if(len(lista) != 0):
        for r in lista:
            html += """ <div class="well">
                        <div class="media">
                        <div class="media-body">
                            <h2 class="media-heading">""" + r.link + """</h2>
                            <p class="text-right">Por""" + r.usuario + """</p>
                            <p class="text-left">""" + r.cita + """</p>
                            <p class="text-left">""" + r.descripcion + """</p>
                            <br>
                            <ul class="list-inline list-unstyled">
                                <li><span><i class="glyphicon glyphicon-calendar"></i>""" + str(r.fecha) + """</span></li>
                                <li><span><i class="glyphicon glyphicon-comment"></i> X comentarios</span></li>
                            </ul>
                        </div>
                        </div>
                        </div>\n\n"""
        num = 200
    return html, str(num)
	
app.run(debug=True)
