class Pedido:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad


def calcular_total(pedido, precio):
    return pedido.cantidad * precio

class Pedido:
    def __init__(self, producto, cantidad, precio):
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio

    def calcular_total(self):
        return self.cantidad * self.precio
