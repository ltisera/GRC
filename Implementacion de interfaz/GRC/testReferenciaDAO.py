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
"""
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
"""
#tags = ["Programacion", "Quimica", "Mecanica", "Arte"]

#referenciaDao.publicarReferencia("otra cita","otra desc", "python.com", "2018-07-06 11:45:31", usuario1, grupo1, tags)



#referenciaDao.comentarReferencia("comentario 1", referenciaDao.traerReferenciasDeGrupo(1)[0], "2018-07-06 11:45:31", usuario1)

#idReferencia = referenciaDao.traerReferenciasDeGrupo(1)[0].idReferencia
#for i in referenciaDao.traerComentariosDeReferencia(idReferencia):
#	print(str(i))

referenciaDao.eliminarReferencia(27)




