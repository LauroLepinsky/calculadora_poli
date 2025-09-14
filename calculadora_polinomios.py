import numpy as np
import streamlit as st

st.title("Cálculo de raízes de polinômios: ")

entrada_usuario = st.text_input(
    'Insira os coeficientes. Não precisa separá-los por vírgula. Em caso de números decimais, use " . ". Exemplo: 1 -5 6 '
)
coeficientes = entrada_usuario.split()
try:
    coeficientes = [float(item) for item in coeficientes]
except (ValueError, NameError):
    st.write(
        'ERRO: Insira APENAS números, não precisa separá-los por vírgula. Em caso de números decimais, use "."'
    )
raizes_np = np.roots(coeficientes)
raizes = [round(item, 2) for item in raizes_np]
st.write(f"Raízes: {raizes}")
