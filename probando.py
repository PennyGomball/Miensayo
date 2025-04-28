# Importo librerias necesarias
from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd 
import streamlit as st
from io import StringIO

uploaded_file2 = st.file_uploader("Choose a file")

    # Can be used wherever a "file-like" object is accepted:
mdataframe = pd.read_csv(uploaded_file2,sep=";")
datos_pyg = StreamlitRenderer(mdataframe)
datos_pyg.explorer()

    