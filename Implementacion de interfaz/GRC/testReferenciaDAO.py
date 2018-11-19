from Referencia import Referencia
from Categoria import Categoria
from ReferenciaDAO import ReferenciaDAO
from UsuarioDAO import UsuarioDAO
from GrupoDAO import GrupoDAO

referenciaDao = ReferenciaDAO()
usuarioDao = UsuarioDAO()
grupoDao = GrupoDAO()

usuario1 = usuarioDao.traerUsuarioXId(1)
grupo1 = grupoDao.traerGrupo(1)

#metodos que andan
referenciaDao.crearConexion()
print(referenciaDao.traerCategoria(str("ASDdadad")) == None)
referenciaDao.cerrarConexion()

referenciaDao.crearConexion()
print(referenciaDao.traerCategoria("ASDdadad"))
referenciaDao.cerrarConexion()

referenciaDao.crearConexion()
print(referenciaDao.traerCategoria("Quimica") == None)
referenciaDao.cerrarConexion()

referenciaDao.crearConexion()
print(referenciaDao.traerCategoria("Quimica"))
referenciaDao.cerrarConexion()

#tags = ["Fisica", "Quimica", "Matematica", "Mecanica"]

#referenciaDao.publicarReferencia("Esto es una cita","Esto es una descripcion", "google.com", "2018-07-06 11:45:31", usuario1, grupo1, tags)



