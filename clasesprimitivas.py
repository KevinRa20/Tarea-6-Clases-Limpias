def crear_usuario(nombre, edad, correo):
    return {"nombre": nombre, "edad": edad, "correo": correo}

class Usuario:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

usuario = Usuario("Kevin", 25, "kevin@email.com")
