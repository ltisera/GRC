from Grupo import Grupo
from Usuario import Usuario
from GrupoDAO import GrupoDAO
from UsuarioDAO import UsuarioDAO


grupoDao = GrupoDAO()
usuarioDao = UsuarioDAO()


usuario1 = usuarioDao.traerUsuarioXId(1)
usuario2 = usuarioDao.traerUsuarioXId(2)

grupo1 = grupoDao.traerGrupo(1)

#print("Usuario 1: "+str(usuario1))
#print("Usuario 2: " +str(usuario2))
#Metodos que andan
#grupoDao.crearGrupo("Grupo2", "descripcion de grupo 2", usuario1)
#print(str(grupoDao.traerGrupo(1)))
#print(grupoDao.consultarPermisos(usuario1, grupo1))
#grupoDao.agregarUsuarioAGrupo(usuario2, "lectura", grupo1)
#grupoDao.eliminarUsuarioDelGrupo(usuario2, grupo1)

lstGrupos = grupoDao.traerGrupos(usuario1)

for i in lstGrupos:
	print(str(i))
