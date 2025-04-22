import pandas as pd 
import pygwalker as pyg
import streamlit as st
print("hola")

# se asigna a variable mfile la ruta de mi archivo local en este entorno
mfile = 'ventasejemplo.csv'

# Uso de la funcion read_csv para leer el archivo Misdatos seria una variable que contiene la matriz

# uso de 2 parametros separador
Misdatos = pd.read_csv(mfile, sep=';')

opcion = st.selectbox("elija",("yo","tu","el"))

st.write("Tu seleccion :", opcion)

if opcion == "yo":


    st.bar_chart(Misdatos,x="Nombre del Producto",y="Cantidad Vendida")
 
if opcion == "tu":
    st.line_chart(Misdatos,x="Nombre del Producto",y="Cantidad Vendida")
