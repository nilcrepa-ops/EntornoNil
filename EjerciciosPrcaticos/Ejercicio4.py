#Conversor acciones sencillo (compra estimada)

accion = input("Nombre de la accion/ETF: ")
euros = float(input("Cuantos euros quieres invertir? "))
precio = float (input("Precio actual de la accion: "))
cantidad = euros/precio
print ("Puedes comprar ", round(cantidad, 6), " acciones de ", accion)