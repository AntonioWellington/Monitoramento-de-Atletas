import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng


class Tela_inicial:
    def configuraco_da_pagina(self):
        st.set_page_config(layout="wide", page_icon="🦠")
        st.title("MONIORAMENTO DE ATLETAS", text_alignment = "center")
        st.divider()
    def area_principal(self):
        with st.container(horizontal = True):
            st.metric("Total de cadastros", "4 mph", "2 mph", border=True)
            st.metric("Total com Covid", "4 mph", "2 mph", border=True)
            st.metric("Total sem Covid", "4 mph", "2 mph", border=True)
        st.divider()
        df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

        st.area_chart(df, width="stretch")
        df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
        st.area_chart(df, width="stretch")
        st.divider()
        st.text("© 2025 MONITORAMENTO DE ATLETAS", text_alignment = "justify" )

    def barra_lateral(self):       
        with st.sidebar:
            st.title("menu", text_alignment = "center")
            st.divider()
            if st.button("CADASTRAR", width = "stretch", type="tertiary"):
                self.pop_up_cadastrar()
            st.button("RELATORIO", type = "primary", width = "stretch")
            st.divider()

    @st.dialog("CADASTRAR ATLETA", dismissible=False)
    def pop_up_cadastrar(self):
        st.text_input("CPF")
        st.text_input("IDADE")
        st.text("SEXO")
        with st.container(horizontal = True):
            st.checkbox("MASCULINO")
            st.space("small")
            st.checkbox("FEMININO")
        st.text("TEVE FEBRE?")
        with st.container(horizontal = True):
            st.checkbox("Sim")
            st.space("small")
            st.checkbox("NAO")
        st.text("TEVE OUTROS SINTOMAS?")
        with st.container(horizontal = True):
            st.checkbox("SIM")
            st.space("small")
            st.checkbox("NO")
        st.text("medalhas")
    def exibir_tabelas_sql(self):
        
        confusion_matrix = pd.DataFrame(
            {
                "Predicted Cat": [85, 3, 2, 1],
                "Predicted Dog": [2, 78, 4, 0],
                "Predicted Bird": [1, 5, 72, 3],
                "Predicted Fish": [0, 2, 1, 89],
            },
            index=["Actual Cat", "Actual Dog", "Actual Bird", "Actual Fish"],
        )
        st.table(confusion_matrix)
    

tela = Tela_inicial()
tela.configuraco_da_pagina()
tela.area_principal()
tela.barra_lateral()
st.title("TABELA COM CADASTROS DOS ATLETAS")
st.divider()
tela.exibir_tabelas_sql()
tela.exibir_tabelas_sql()
tela.exibir_tabelas_sql()
st.json(
    {
        "foo": "bar",
        "stuff": [
            "stuff 1",
            "stuff 2",
            "stuff 3",
        ],
        "level1": {"level2": {"level3": {"a": "b"}}},
    },
    expanded=5,
)