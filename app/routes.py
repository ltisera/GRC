# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, session, abort
from flaskext.mysql import MySQL
from flask_mail import Mail, Message
from app import app

app.config.from_pyfile('config.cfg')
mysql = MySQL(app)
mail = Mail(app)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    email = request.form['username']
    password = request.form['password']
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT COUNT(1) FROM usuario WHERE email = %s', (email))
    if cursor.fetchone()[0]:
        cursor.execute("SELECT password, confirm, idUsuario FROM usuario WHERE email = %s;", [email]) # FETCH THE HASHED PASSWORD
        pwd = cursor.fetchone()
        print pwd
        #para validar si me esta devolviendo bien
        if pwd[0] == password:
            if pwd[1] == 1:
                session['logged_in'] = True
                session['id_Usuario'] = pwd[2]
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

@app.route('/signupOK')
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

@app.route('/community')
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
        print data
        return render_template('community.html')

@app.route('/index')
def index():
    return render_template('prueba.html', title='Home')