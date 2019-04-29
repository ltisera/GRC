from flask import Flask, render_template, send_from_directory, request, jsonify, Response
from DAO.UsuarioDAO import UsuarioDAO
from DAO.GrupoDAO import GrupoDAO

from DAO.ReferenciaDAO import ReferenciaDAO

from OLL.UsuarioOLL import UsuarioOLL
from OLL.GrupoOLL import GrupoOLL
from OLL.ComentarioOLL import ComentarioOLL
from OLL.ReferenciaOLL import ReferenciaOLL
from DML.Usuario import Usuario

from datetime import datetime

app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/banner-inicio.jpg')
def bannerInicio():
    return send_from_directory('static/img', 'banner-inicio.jpg')


@app.route('/banner-info.jpg')
def bannerInfo():
    return send_from_directory('static/img', 'banner-info.jpg')


@app.route('/team1.jpg')
def team1():
    return send_from_directory('static/img', 'team1.jpg')


@app.route('/team2.jpg')
def team2():
    return send_from_directory('static/img', 'team2.jpg')


@app.route('/team3.jpg')
def team3():
    return send_from_directory('static/img', 'team3.jpg')


@app.route('/menu.js')
def jsMenu():
    return send_from_directory('static/js', 'menu.js')


@app.route('/estilo.css')
def cssEstilo():
    return send_from_directory('static/css', 'estilo.css')


@app.route('/info.css')
def cssInfo():
    return send_from_directory('static/css', 'info.css')


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
    return send_from_directory('static/css', 'estilos.css')


@app.route('/static/recursos/icons/fontello-4ce1ed53/css/fontello.css')
def recFontello():
    print("despachame los iconos")
    return send_from_directory('static/recursos/icons/fontello-4ce1ed53/css', 'fontello.css')


@app.route('/js/grupos.js')
def jsgrupos():
    return send_from_directory('static/js', 'grupos.js')


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
    return render_template('grupos.html')


@app.route('/publicar')
def publicar():
    return render_template('publicar2.html')


@app.route('/traerTodosGrupos')
def traerTodosGrupos():
    gOll = GrupoOLL()
    return gOll.traerGrupos()


@app.route('/consultarPermiso')
def consultarPermiso():
    gOll = GrupoOLL()
    return gOll.consultarPermisos(request.values['idUsuario'],
                                  request.values['idUsuario'])


@app.route('/crearUsuario', methods=['GET', 'POST'])
def crearUsuarioPOST():
    usser = UsuarioOLL()
    return jsonify(usser.crearUsuario(request))


@app.route('/cargarListaGrupo', methods=['GET', 'POST'])
def cargarListaGrupo():
    gOll = GrupoOLL()
    return gOll.traerGruposDeUsuario(request.values["usuario"])

@app.route('/traerR')
def traerR():
    lista = rdao.traerReferenciasDeGrupo(request.values["grupo"])
    return jsonify(lista)

@app.route('/cargarListaReferencias', methods=['GET', 'POST'])
def cargarListaReferencias():
    print("Cargo lista de referencias")
    num = 200
    refoll = ReferenciaOLL()
    return refoll.traerReferenciasDeGrupo(request.values["grupo"])

@app.route('/cargarReferenciaTest', methods=['GET', 'POST'])
def cargarReferenciaTest():
    num = 200
    rdao = ReferenciaDAO()
    lista = rdao.traerReferenciasDeGrupo(request.values["grupo"])
    lstRefJson = []
    for i in lista:
        if(len(lista)>0):
            
            refJson = {}
            refJson["id"] = i.idReferencia
            refJson["cita"] = i.cita
            refJson["descripcion"] = i.descripcion
            refJson["link"] = i.link
            refJson["fecha"] = i.fecha
            refJson["usuario"] = i.usuario
            refJson["grupo"] = i.grupo

            lstRefJson.append(refJson)
    return jsonify(lstRefJson)

@app.route('/loguearUsuario', methods=['GET', 'POST'])
def loguearUsuario():
    objUsuario = validarUsuario(request)
    if(objUsuario is not None):
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
    stAgregarUsuario = udao.agregarUsuario(nuevoUsuario)
    if(stAgregarUsuario is True):
        print("Se agrego Correctamente")
    else:
        print("Error", stAgregarUsuario)
    return 200


def validarUsuario(request):
    udao = UsuarioDAO()
    elusr = udao.traerUsuarioXMail(request.values["usuario"])

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
    gOll = GrupoOLL()
    gOll.crearGrupo(request.values["nombreGrupo"],
                    request.values["descripcion"],
                    request.values["usuarioCredor"])
    jResponse = 200
    return jsonify(jResponse)


@app.route('/invitarUsuario', methods=['GET', 'POST'])
def invitarUsuario():
    udao = UsuarioDAO()
    gOll = GrupoOLL()
    user = udao.traerUsuarioXMail(request.values["mailDeUsuario"])
    if(user is not None):
        idUsuario = user.idUsuario
        idGrupo = gOll.traerGrupo(request.values["idDelGrupo"]).idGrupo
        status = 500
        return gOll.agregarUsuarioAGrupo(idUsuario, request.values["permisoUsuario"], idGrupo)
    return jsonify(200,"El usuario no Existe")


@app.route('/tstResponse', methods=['GET', 'POST'])
def tstResponse():
    return jsonify("Te respondo"), 200

@app.route('/publicarReferencia', methods=['GET', 'POST'])
def publicarReferencia():
    refoll = ReferenciaOLL()
    refoll.publicarReferencia(request.values["cita"], request.values["descripcion"], request.values["link"],
        datetime.now(), request.values["usuario"], request.values["grupo"], request.values["tags"])
    jResponse = 200
    return str(jResponse)


@app.route('/comentarReferencia', methods=['GET', 'POST'])
def comentarReferencia():
    comoll = ComentarioOLL()
    fecha = datetime.now()
    comoll.comentarReferencia(request.values["comentario"], request.values["idReferencia"], fecha, request.values["idUsuario"])
    jResponse = 200
    return jsonify(jResponse)


@app.route('/eliminarReferencia', methods=['GET', 'POST'])
def eliminarReferencia():
    refoll = ReferenciaOLL()
    refoll.eliminarReferencia(request.values["idReferencia"])
    jResponse = 200

    return str(jResponse)



@app.route('/buscarReferencia', methods=['GET', 'POST'])
def buscarReferencia():
    html = ""
    num = 404
    refoll = ReferenciaOLL()
    lista = refoll.buscarReferencia(request.values["idGrupo"], request.values["busqueda"])
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

@app.route('/cargarComentarios', methods=['GET', 'POST'])
def cargarComentarios():
    comoll = ComentarioOLL()

    return comoll.traerComentariosDeReferencia(request.values["idReferencia"])

@app.route('/eliminarComentario', methods=['GET', 'POST'])
def eliminarComentario():
    comoll = ComentarioOLL()
    return comoll.eliminarComentario(request.values["idComentario"])


@app.route('/recursos/icons/iconComentario.png')
def iconComentario():
    return send_from_directory('static/recursos/icons', 'iconComentario.png')

	
app.run(debug=True)
