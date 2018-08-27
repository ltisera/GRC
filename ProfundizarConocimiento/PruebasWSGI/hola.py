from wsgiref.simple_server import make_server
import mysql.connector

def hello_world(environ, start_response):
    status = '200 ok'

    print("levantando resp_archivo")
    resp_archivo = open('hola.htm', "r")
    print("levantado")
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return resp_archivo


def run():

    print("Levantando BD")
    bd = mysql.connector.connect(
        host="localhost",
        user="adminsuve",
        passwd="1234suve",
        database="usuario")
    micur = bd.cursor()
    micur.execute("SHOW COLUMNS FROM usuario")
    print("Los campos")
    for i in micur:
        print(i[0])
    micur.execute("SELECT * FROM usuario")
    print("Fin de los campos\n")
    for i in micur:
        print("Iteracion")

        print(i)
    print("insertando datos:")
    for n in range(10):
        nombre = "pepe" + str(n)
        print (nombre)
        micur.execute("INSERT INTO usuario(ussr,passwd,mail) VALUES ('{0}','123','buena')".format(nombre))
        bd.commit()
    httpd = make_server('', 8006, hello_world)
    print('Serving on port 8006...')
    httpd.serve_forever()



if __name__ == '__main__':
    run()
