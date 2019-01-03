import configs
import mysql.connector
from mysql.connector import Error

class ConexionBD:
    instance = None

    def __new__(cls):
        if(cls.instance is None):
            cls.instance = super(ConexionBD, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self._bd = None
        self._micur = None

    def crearConexion(self):
        connectionDict = configs.getConfigDB()
        self._bd = mysql.connector.connect(**connectionDict)
        self._micur = self._bd.cursor()

    def cerrarConexion(self):
        if(self._bd.is_connected()):
            self._micur = self._bd.cursor()
            self._bd.close()

    def cerrarCursor(self):
        self._micur.close()

if __name__ == '__main__':
    a = ConexionBD()
    b = ConexionBD()
    a.setCont(2)
    print(a.getCont())
    b.setCont(4)
    print(a.getCont())
    