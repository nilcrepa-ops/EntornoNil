#Gestor de carteras cripto

cartera ={
    "BTC": 0.01,
    "ETH": 0.5,
    "ADA": 50
}

moneda = input("Moneda a añadir: (BTC, ETH, ADA)")
cantidad = float(input("Cantidad a añadir: "))

if moneda in cartera:
    cartera[moneda] += cantidad
    print("Cartera actualizada:", cartera)
else:
    print("Moneda no encontrada")