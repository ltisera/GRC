from wsgiref.simple_server import make_server
import mysql.connector
from Usuario import Usuario
from UsuarioDAO import UsuarioDAO


def hello_world(environ, start_response):
    status = '200 ok'
    
    if(environ.get("PATH_INFO") == "/jason"):
        udao = UsuarioDAO()
        laca = udao.traerUsuario(1).aCadena()
        print(laca)
        resp_archivo = udao.traerUsuario(1).aCadena()
        headers = [('Content-type', 'text/html')]
    else:
        resp_archivo = open('hola.html', "r")
        headers = [('Content-type', 'text/html')]
    
    start_response(status, headers)
    return resp_archivo


def rtaJason(environ, start_response):
    print("Te mando el jason")
    udao = UsuarioDAO()
    return udao.traerUsuario(1).aCadena()

def run():
    httpd = make_server('', 8006, hello_world)
    print('Serving on port 8006...')
    httpd.serve_forever()



if __name__ == '__main__':
    run()
