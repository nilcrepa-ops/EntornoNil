altura = int(input("Que altura quiere para la piramide? "))
alturaDef = altura + 1

#Si usas 'altura' directamente, al empezar a contar desde 0 imprime una fila menos de las que ha escrito el usuario

for i in range(1, alturaDef):
    for j in range(i):
        print("*", end="")
    print()