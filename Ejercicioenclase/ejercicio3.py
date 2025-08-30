#Sucio
def acceder_recurso(usuario):
    if not usuario['rol'] == 'admin':
        print("Permiso denegado")
    else:
        print("Acceso permitido")

usuario = {'nombre': 'Kevin', 'rol': 'admin'}
acceder_recurso(usuario)
#Limpio
def acceder_recurso(usuario):
    if usuario['rol'] == 'admin':
        print("Acceso permitido")
        return
    print("Permiso denegado")

usuario = {'nombre': 'Kevin', 'rol': 'admin'}
acceder_recurso(usuario)
