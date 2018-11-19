from Grupo import Grupo
from Usuario import Usuario
from GrupoDAO import GrupoDAO
from UsuarioDAO import UsuarioDAO


grupoDao = GrupoDAO()
usuarioDao = UsuarioDAO()


usuario1 = usuarioDao.traerUsuarioXId(1)
usuario2 = usuarioDao.traerUsuarioXId(2)

print("Usuario 1: "+str(usuario1))
print("Usuario 2: " +str(usuario2))
grupoDao.crearGrupo("Grupo2", "descripcion de grupo 2", usuario1)

