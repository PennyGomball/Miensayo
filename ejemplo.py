from pygwalker.api.streamlit import StreamlitRenderer 
import pandas as pd 
import pygwalker as pyg
import streamlit as st

print("hola")

# se asigna a variable mfile la ruta de mi archivo local en este entorno
mfile = 'ventasejemplo.csv'

# Uso de la funcion read_csv para leer el archivo Misdatos seria una variable que contiene la matriz

# uso de 2 parametros separador
Misdatos = pd.read_csv(mfile, sep=';')

opcion = st.selectbox("elija",("Grafico de barras","Grafico de areas","Leer"))

st.write("Tu seleccion :", opcion)

if opcion == "Grafico de barras":


    st.bar_chart(Misdatos,x="Nombre del Producto",y="Cantidad Vendida")
 
if opcion == "Grafico de areas":
    st.area_chart(Misdatos,x="Nombre del Producto",y="Cantidad Vendida")
if opcion == "Leer":
    #pyg_app = StreamlitRenderer(mfile)
    #pyg_app.explorer()
     pyg.walk(Mfile,env="streamlit")

