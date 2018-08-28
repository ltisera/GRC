from wsgiref.simple_server import make_server
import mysql.connector

from UsuarioDAO import UsuarioDAO


def hello_world(environ, start_response):
    status = '200 ok'
    print("levantando resp_archivo")
    resp_archivo = open('hola.htm', "r")
    print("levantado")
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return resp_archivo


def run():
    udao = UsuarioDAO()
    elusr = udao.traerUsuario(0)
    print(elusr)
    httpd = make_server('', 8006, hello_world)
    print('Serving on port 8006...')
    httpd.serve_forever()



if __name__ == '__main__':
    run()
