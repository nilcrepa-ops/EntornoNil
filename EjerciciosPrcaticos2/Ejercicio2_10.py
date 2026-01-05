#Gestor de grupos musicales

artistas = [
    {"nombre": "Dua Lipa", "genero": "Heavy Metal"},
    {"nombre": "Taylor Swift", "genero": "Makina"},
    {"nombre": "Rihanna", "genero": "Blues"}
]

for artista in artistas:
    print ("Nombre: ", artista["nombre"])

generoBuscado = input("Introduce el genero para filtrar: (Heavy Metal, Makina, Blues)")
print("Artistas encontrados en el genero", generoBuscado)

artistasEncontrados = False
for artista in artistas:
    if artista["genero"] == generoBuscado:
        print("-",artista["nombre"])
        artistasEncontrados = True