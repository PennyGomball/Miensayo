import pandas as pd 
import matplotlib.pyplot as plt
print("hola")

# se asigna a variable mfile la ruta de mi archivo local en este entorno
mfile = 'ventasejemplo.csv'

# Uso de la funcion read_csv para leer el archivo Misdatos seria una variable que contiene la matriz

# uso de 2 parametros separador
Misdatos = pd.read_csv(mfile, sep=';')

# Muestra los 5 primeros registros
Misdatos.head(3)





plt.bar(Misdatos["Nombre del Producto"],Misdatos["Cantidad Vendida"])
plt.show()
 
