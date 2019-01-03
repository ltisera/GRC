from flask import Flask
import sys
path = '/home/grcunla'
if path not in sys.path:
    sys.path.insert(0, path)

app = Flask(__name__)


@app.route('/')
def hola():
    return "Hola Mundooo!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()
