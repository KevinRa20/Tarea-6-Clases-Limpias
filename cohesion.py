class ReporteVentas:
    def calcular_ventas(self):
        pass
    
    def conectar_base_datos(self):
        pass
    
    def enviar_email(self):
        pass

class CalculadoraVentas:
    def calcular(self, ventas):
        return sum(ventas)

class ServicioEmail:
    def enviar(self, destinatario, mensaje):
        print(f"Enviando email a {destinatario}: {mensaje}")
