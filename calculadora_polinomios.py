import numpy as np
import streamlit as st

st.title("Cálculo de raízes de polinômios")

entrada_usuario = st.text_input(
    "Insira os coeficientes separados por espaço. Exemplo: 1 -5.5 6"
)

if entrada_usuario:

    coeficientes_str = entrada_usuario.split()
    try:
        coeficientes_float = [float(item) for item in coeficientes_str]

    except ValueError:
        st.error(
            'ERRO: Insira apenas números. Use "." para decimais e separe com espaço.'
        )
    else:
        raizes_np = np.roots(coeficientes_float)
        raizes_arredondadas = np.round(raizes_np, 5)
        st.subheader("Raízes Encontradas:")
        for i, raiz in enumerate(raizes_arredondadas):
            st.success(f"**Raiz {i+1}:** `{np.round(raiz, 5)}`")
