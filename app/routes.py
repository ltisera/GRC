# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, session, abort
from flaskext.mysql import MySQL
from flask_mail import Mail, Message
from datetime import datetime
from app import app

app.config.from_pyfile('config.cfg')
mysql = MySQL(app)
mail = Mail(app)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect(url_for('community'))
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    email = request.form['username']
    password = request.form['password']
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT COUNT(1) FROM usuario WHERE email = %s', (email))
    if cursor.fetchone()[0]:
        cursor.execute("SELECT password, confirm, idUsuario, admin FROM usuario WHERE email = %s;", [email]) # FETCH THE HASHED PASSWORD
        pwd = cursor.fetchone()
        print pwd
        #para validar si me esta devolviendo bien
        if pwd[0] == password:
            if pwd[1] == 1:
                session['logged_in'] = True
                session['id_Usuario'] = pwd[2]
                session['admin'] = pwd[3]
                return redirect(url_for('community'))
            else:
                flash('Usuario no autorizado!')
        else:
            flash('Password incorrecto!')
    else:
        flash('Usuario incorrecto!')  
    return home()
 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route('/signup/#')
def signup():
    if not session.get('logged_in'):
        return render_template('signup.html')
    else:
        return "Hello Boss!  <a href='/index'>index</a>"

@app.route('/signup', methods=['POST'])
def add_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT email FROM usuario WHERE email = %s', (email))
        row = cursor.fetchone()
        if row is None: 
            cursor.execute("SELECT MAX(idUsuario) FROM usuario")
            maxid = cursor.fetchone()
            cursor.execute("INSERT INTO `usuario` (`idUsuario`, `nombre`, `apellido`, `email`, `password`, `admin`, `confirm`)" "VALUES (%s, %s, %s, %s, %s, %s, %s)", (maxid[0]+1, nombre, apellido, email, password, None, None))
            mysql.get_db().commit()
            #envio de email
            mensaje='&nbsp;Hola '+str(nombre)+'!<br>' \
                    '<p> &nbsp;&nbsp;&nbsp;Su registro fue enviado a un administrador para su aprobación. </p> <br>' \
                    '<p> &nbsp;&nbsp;&nbsp;Recibirá un email de confirmación cuando se apruebe el registro. </p> <br>' \
                    '<p> &nbsp;&nbsp;Saludos, muchas gracias! GRC.</p>'
            msg = Message('Reporte de Registro', sender = 'Gestor Referencias Colaborativas', recipients = [email], html=mensaje)
            mail.send(msg)
            flash('Pendiente de Confirmacion')
            return redirect(url_for('signup'))
        else:
            flash('Usuario existente')
            return redirect(url_for('signup'))

@app.route('/forgot')
def forgot():
    return render_template('forgot.html', title='forgot?')

@app.route('/community', methods = ['POST','GET'])
def community():
    if not session.get('logged_in'):
        return render_template(url_for('home'))
    else:
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT g.idGrupo, g.nombre, g.descripcion, gxu.nivelUsuario FROM usuario u \
        INNER JOIN grupoxusuario gxu ON u.idUsuario = gxu.idUsuario \
        INNER JOIN grupo g ON g.idGrupo = gxu.idGrupo \
        WHERE u.idUsuario= %s', session.get('id_Usuario')) 
        data = cursor.fetchall()
        return render_template('community.html', grupos = data)

@app.route('/crearGrupo', methods=['GET', 'POST'])
def crearGrupo():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('crearGrupo.html')

@app.route('/crearGrupoOK', methods=['POST'])
def addGrupo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT MAX(idGrupo) FROM grupo")
        maxid = cursor.fetchone()
        cursor.execute("INSERT INTO `grupo` (`idGrupo`, `nombre`, `descripcion`)" "VALUES (%s, %s, %s)", (maxid[0]+1, nombre, descripcion))
        mysql.get_db().commit()
        nivelUsuario='a'
        idUsuario=session.get('id_Usuario')
        cursor.execute("INSERT INTO `grupoxusuario` (`idGrupo`, `idUsuario`, `nivelUsuario`)" "VALUES (%s, %s, %s)", (maxid[0]+1, idUsuario, nivelUsuario))
        mysql.get_db().commit()
        flash('Grupo Creado')
        return redirect(url_for('community'))
    else:
            flash('ERROR')
            return redirect(url_for('home'))

@app.route('/grupo/<string:id>', methods = ['POST','GET'])
def grupo(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT gxu.nivelUsuario FROM grupo g \
        INNER JOIN grupoxusuario gxu ON g.idGrupo = gxu.idGrupo \
        WHERE g.idGrupo= %s', id)
    permiso = cursor.fetchone()
    session['permiso'] = permiso
    session['grupo'] = id
    cursor.execute('SELECT nombre FROM grupo WHERE idGrupo = %s', (id))
    session['nombregrupo'] = cursor.fetchone()
    cursor.execute('SELECT r.idReferencia, r.descripcion, r.link, r.cita, r.fechaHora, r.idUsuario FROM grupo g \
        INNER JOIN referencia r ON g.idGrupo = r.idGrupo \
        INNER JOIN usuario u ON u.idUsuario = r.idUsuario \
        WHERE g.idGrupo= %s', id)
    data = cursor.fetchall()
    print data
    return render_template('referencia.html', referencias = data)

@app.route('/grupo/<int:id>/agregarUsuario', methods=['GET', 'POST'])
def agregarUsuario(id):
    return render_template('agregarUsuario.html')

@app.route('/grupo/<int:id>/agregarUsuario2', methods=['GET', 'POST'])
def agregarUsuarioForm(id):
    email = request.form['email']
    nivelUsuario = request.form.get('nivelUsuario')
    nivelUsuario='b'
    print "fijate acaaaaaa"
    print nivelUsuario
    if nivelUsuario != 'c':
        nivelUsuario='b'
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT idUsuario FROM usuario WHERE email = %s', (email))
    idUsuario = cursor.fetchone()
    if idUsuario is not None:
        cursor.execute("INSERT INTO `grupoxusuario` (`idGrupo`, `idUsuario`, `nivelUsuario`)" "VALUES (%s, %s, %s)", (id, idUsuario, nivelUsuario))
        mysql.get_db().commit()
        flash('Usuario agregado al grupo')
    else: flash('No se agrego al grupo') 
    return redirect("/grupo/%s" % id )

@app.route('/grupo/<int:id>/listaUsuarios', methods=['GET', 'POST'])
def listaUsuarios(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT u.nombre, u.apellido, u.email FROM grupo g \
        INNER JOIN grupoxusuario gxu ON g.idGrupo = gxu.idGrupo \
        INNER JOIN usuario u ON u.idUsuario = gxu.idUsuario \
        WHERE g.idGrupo= %s', id)
    data = cursor.fetchall()
    print data
    #return redirect("/grupo/%s/listaUsuarios" % id , usuarios = data)
    return render_template('listaUsuarios.html', usuarios = data)

@app.route('/volverRef')
def volverRef():
    return redirect("/grupo/%s" % id )

@app.route('/grupo/<int:id>/crearReferencia', methods=['GET', 'POST'])
def crearReferencia(id):
    return render_template('crearReferencia.html')    

@app.route('/grupo/<int:id>/crearReferencia2', methods=['GET', 'POST'])
def crearReferenciaForm(id):
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        link = request.form['link']
        cita = request.form['cita']
        fechaHora = datetime.now()
        idUsuario = session['id_Usuario']
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT MAX(idReferencia) FROM referencia")
        maxid = cursor.fetchone()
        cursor.execute("INSERT INTO `referencia` (`idReferencia`, `descripcion`,`link`, `cita`, `fechaHora`,`idUsuario`, `idGrupo`)" "VALUES (%s, %s, %s, %s, %s, %s, %s)", (maxid[0]+1, descripcion, link, cita, fechaHora,idUsuario,id))
        mysql.get_db().commit()
        flash('Referencia agregada al grupo')
        return redirect("/grupo/%s" % id )

@app.route('/index')
def index():
    return render_template('prueba.html', title='Home')