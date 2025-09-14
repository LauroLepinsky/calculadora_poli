# %%
import numpy as np
import streamlit as st

st.title("Cálculo de raízes de polinômios: ")

entrada_usuario = st.text_input(
    'Insira os coeficientes. Não precisa separá-los por vírgula. Em caso de números decimais, use " . ". Exemplo: 1 -5 6 '
)
lista = entrada_usuario.split()
try:
    coeficientes = [float(item) for item in lista]
    print(coeficientes)
except ValueError:
    print(
        'Insira apenas números, não precisa separá-los por vírgula. Em caso de números decimais, use "."'
    )
raizes_np = np.roots(coeficientes)
raizes = [round(item, 2) for item in raizes_np]
st.write(f"Raízes: {raizes}")
