#Sucio
def acceder_usuario(usuario):
    if not usuario['Usuario activo']:
        print("Acceso denegado")
    else:
        print("Bienvenido", usuario['nombre'])


usuario = {'nombre': 'Kevin', 'activo': True}
acceder_usuario(usuario)
# Limpio
def acceder_usuario(usuario):
    if usuario['Usuario activo']:
        print(f"Bienvenido {usuario['nombre']}")
        return
    print("Acceso denegado")


usuario = {'nombre': 'Kevin', 'Usuario activo': True}
acceder_usuario(usuario)