from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def inicio():
    return('<p>Estas en la raiz</p>')

@app.route('/js/jquery-3.3.1.js')
def jsfile():
    return send_from_directory('static/js','jquery-3.3.1.js')


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/miajax')
def miajax():
    return ("<p>Devolveme la cadena</p>");


app.run(host='localhost')
