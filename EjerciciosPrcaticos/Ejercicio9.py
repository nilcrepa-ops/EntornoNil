#Informatica cotidiana (MB a GB)

archivos = int(input("Numero de archivos: "))
tam_mb = float(input("Tamaño medio por archivo (MB): "))

total_mb = archivos*tam_mb

total_gb = total_mb/1024

print ("Tamaño total: ", round(total_gb, 2), " GB.")