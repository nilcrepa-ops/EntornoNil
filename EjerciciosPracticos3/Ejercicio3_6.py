contador = 0
vocales = "aeiou"

frase = input("Escribe una frase: ")

for caracter in frase.lower():
    if caracter in vocales:
        contador += 1

print(f"La frase tiene", {contador}, " vocales")