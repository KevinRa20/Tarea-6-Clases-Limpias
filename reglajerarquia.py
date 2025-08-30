class Motor:
    pass

class Auto(Motor): 
    pass

class Vehiculo:
    def mover(self):
        pass

class Auto(Vehiculo):
    def mover(self):
        return "El auto se está moviendo."

class Moto(Vehiculo):
    def mover(self):
        return "La moto se está moviendo."
