pesos = []

peso1 = float(input("Introduce el peso corporal del día 1: "))
peso2 = float(input("Introduce el peso corporal del día 2: "))
peso3 = float(input("Introduce el peso corporal del día 3: "))
peso4 = float(input("Introduce el peso corporal del día 4: "))
peso5 = float(input("Introduce el peso corporal del día 5: "))



pesos.append(peso1)
pesos.append(peso2)
pesos.append(peso3)
pesos.append(peso4)
pesos.append(peso5)

media = sum(pesos) / len(pesos)

print("La media semanal de tu peso corporal es: ", round(media, 2), " kg")