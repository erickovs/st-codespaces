import streamlit as st

st.title("Hello, Kitty!")
st.write("Vamo a divertirno")


import streamlit as st

valor_slider = st.sidebar.slider("Dame un numerin", 0, 10)
checkbox_marcado = st.checkbox("Marca si el valor es mayor que 5")

if valor_slider > 5:
    if checkbox_marcado:
        st.write("Mayor que 5")
