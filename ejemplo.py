# Importo librerias necesarias
import pandas as pd 
import streamlit as st
from io import StringIO

col1,col2 = st.columns(2)

col1.header("Subir archivo de trabajo formato csv")


# se asigna a variable mfile archivo seleccionado
mfile1= col1.file_uploader("Subir Archivo",type="csv")

if mfile1 is not None:
    # Leer archivo como BYTES
    bytes_data = mfile1.getvalue()
    st.write(bytes_data)

    # Convertir a String basado en  IO:
    stringio = StringIO(mfile1.getvalue().decode("utf-8"))
    st.write(stringio)

# Uso de la funcion read_csv para leer el archivo Misdatos seria una variable que contiene la matriz
Misdatos = pd.read_csv(mfile1, sep=';')

st.dataframe(Misdatos)
#uso de 2 parametros separador


#La variable opcion toma el valor de la eleccion
#opcion = st.selectbox("Seleccione opción para procesar los datos:",("Grafico de barras","Grafico de areas","Leer"))

# Texto enviado por pantalla para mostrar la eleccion en forma de variable
#st.write("Tu seleccion :", opcion)

# Estructura de decisión segun opcion elegida 
#if opcion == "Grafico de barras":


    #st.bar_chart(Misdatos,x="Nombre del Producto",y="Cantidad Vendida")
 
#if opcion == "Grafico de areas":
    #st.area_chart(Misdatos,x="Nombre del Producto",y="Cantidad Vendida")
#if opcion == "Leer":

    # la funcion st.data necesita como parametro un argumento de pd, para este caso
    # es el dataframe asigando a la variable Misdatos
   # st.dataframe(Misdatos)


