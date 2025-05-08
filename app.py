import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

wage=pd.read_csv("salario_tabla.csv")

st.title("SALARIO")

tab1, tab2= st.tabs(["Tab1","Tab2"])

with tab1:
    st.header("Analisis Univariado")
    fig, ax=plt.subplots(1,4, figsize=(10,5))
    ax[0].hist(wage["educación"])
    conteo=wage["sexo"].value_counts()
    ax[1].bar(conteo.index,conteo.values)
    conteo=wage["estado civil"].value_counts()
    ax[2].bar(conteo.index,conteo.values)
    ax[3].hist(wage["salario"])

    st.pyplot(fig)



with tab2:
    st.header("Analisis Bivariado")
    
    fig, ax=plt.subplots(1,3, figsize=(10,5))
    sns.scatterplot(data=wage, y="salario", x="educación", ax=ax[0])
    sns.boxplot(data=wage, y="salario", x="sexo", ax=ax[1])
    sns.boxplot(data=wage, y="salario", x="estado civil", ax=ax[2])
    fig.tight_layout()
    
    st.pyplot(fig)