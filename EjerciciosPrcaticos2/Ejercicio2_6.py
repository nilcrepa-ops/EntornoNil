inventario = {
    "mancuernas": 3,
    "cintas": 16,
    "pinzas": 7
}

print(inventario)

objeto = str(input("Que objeto deseas ver?"))

if(objeto in inventario):
    cantidad = inventario[objeto]
    print("Hay", cantidad, "unidades de", objeto)
else:
    print("No hay stock")
