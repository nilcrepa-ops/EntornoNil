#Generador de contraseñas seguras

import random
import string

letras = string.ascii_letters
nums = string.digits

caracteres = string.ascii_letters + string.digits
longitud = int(input("Que longitud debe tener la contraseña? "))

password = ''.join(random.choice(caracteres) for i in range(longitud))
#'' = String vacio
#.join(random.choice(caracteres) = Funcion de unir un randomizado de caracteres, que es una mezcla de ascii_letters i digits
#for i in range(longitud) = Bucle FOR para iterar i en el rango estipulado en longitud
print("Contraseña generada: ", password)