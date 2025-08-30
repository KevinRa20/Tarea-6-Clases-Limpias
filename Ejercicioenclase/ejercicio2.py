#Sucio
def procesar_compra(stock):
    if not stock <= 0:
        print("Compra realizada")
    else:
        print("No hay un stock disponible")

procesar_compra(5)
#Limpio
def procesar_compra(stock):
    if stock > 0:
        print("Compra realizada")
        return
    print("No hay un stock disponible")

procesar_compra(5)
