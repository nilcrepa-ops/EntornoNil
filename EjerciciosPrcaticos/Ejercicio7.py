#Recomendador musical

estado = input("Como te sientes hoy? feliz/tranquilo/energico/triste: ")

if estado.lower() == "feliz":
    print ("Recomendacion: Taylor Swift")
elif estado.lower() == "energico":
    print ("Recomendacion: Rihana")
elif estado.lower() == "tranquilo":
    print ("Recomendacion: Sabrina Carpenter")
elif estado.lower() == "triste":
    print("Recomendacion: Lamb of God")
else: print ("Buscate la vida")