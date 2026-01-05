#Reglas simples para acciones (rangos con if/elif/else)

nombre = input("Nombre de la accion: ")
precio = float(input("Precio actual en euros: "))

if precio <= 550:
    print("Señal: precio bajo, recomendable invertir más de lo previsto.")
elif precio >= 550:
    print ("Señal: Precio habitual, recomendable invertir lo previsto.")
elif precio >=600:
    print ("Señal: Precio alto, recomendable holdear y esperar")
else: print ("Respuesta incorrecta")