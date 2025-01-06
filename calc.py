import streamlit as st

import pandas as pd

st.set_page_config("Calculadora",
                   page_icon="🧮",
                   layout="centered")
st.title("Bem-vindo(a) a calculadora 🤠")


n1 = st.number_input("Digite um numero",
                     step=1)

operador = st.text_input("""ESCOLHA A OPERAÇÃO MATEMATICA!
                        \nAdição:  +
                        \nsubtração:  -
                        \nmultiplicação:  * ou  x
                        \ndivisão:  /
                         """)

n2 = st.number_input("digite um numero", step=1)

def calcular():
    if operador == "+":
        return n1 + n2
    
    elif operador == "-":
        return n1 - n2
    
    elif operador == "*":
        return n1 * n2
    
    elif operador == "/":
        if n2 != 0:
            return n1 / n2
        else:
            return "Operação inválida, tente novamente!"
    else:
        return "Operação inválida, tente novamente!"


retorno = st.button("clique aqui para calcular!")

if retorno:
    st.header(f"Resultado:  {calcular()}")
    st.success("continue usando a calculadora!",icon="😊")
    



