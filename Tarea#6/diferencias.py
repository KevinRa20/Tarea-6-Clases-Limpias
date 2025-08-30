#
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        return f"{self.nombre} está ladrando."

#
mi_perro = Perro("Firulais", "Labrador")

#
print(mi_perro.ladrar())
