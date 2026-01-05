#Nutricion mediterranea básica (input y productos)

nombre = input("Tu nombre: ")
comidas = int(input("Cuantas comidas haces al dia? "))
cal_por_comida = float(input("Calorias aproximadas por comida: "))
total = comidas*cal_por_comida
print(nombre, ", tu consumo diario aproximado es de ", total, " calorias")

if (total > 2800):
    print ("Aumenta fruta, verdura y agua")
else: print ("Chupiguay")
