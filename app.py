import streamlit as st

st.title("Hello, Kitty!")
st.write("Vamo a divertirno")


import streamlit as st

valor_slider = st.sidebar.slider("Dame un numerin", 0, 10)
checkbox_marcado = st.sidebar.checkbox("Marca si el valor es mayor que 5")

if valor_slider > 5:
    if checkbox_marcado:
        st.write("Mayor que 5")

import pandas as pd

df = pd.read_csv("big mac.csv")

st.write(df)

st.markdown("## Pais")

pais = st.sidebar.selectbox("Selecciona país", ("Argentina", "Brazil"))
st.write("Has seleccionado el pais:", pais)

df_pais = df[df['name'] == pais]

st.write(df_pais)

import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 1),
    columns=['Brazil'])

st.line_chart(chart_data)
