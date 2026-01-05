menu = {
    "pollo": {
        "proteina": 27,
        "calorias": 120
    },
    "ensalada": {
        "proteinas": 3,
        "calorias": 39
    },
    "pizza":{
        "proteina": 12,
        "calorias": 650
    }
}

comida = input("Que comida quieres ver? (pollo, ensalada, pizza) ")

if comida in menu:
    info = menu[comida]

    print("Informacion nutricional de", comida)
    print("Proteina: ", info['proteina'])
    print("Calorias: ", info['calorias'])
    calorias_totales = info["calorias"]

    if calorias_totales > 500:
        print("Comida alta en calorias")
else:
    print("Esta comida no esta en el menu")


