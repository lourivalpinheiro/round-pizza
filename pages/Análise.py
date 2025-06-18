# Importing the necessary modules
from classes.ui.pages import Page
from classes.ui.textelements import TextElement
from classes.ui.title import Title
from classes.ui.header import Header
from classes.ui.footer import Footer
import pandas as pd
import streamlit as st
import plotly.express as px

# Page's main configuration
welcomePage = Page("Análise", icon="🔎", pageLayout="centered")
Header.hide_header()
Title("🔎 Processo de análise")
TextElement.write_caption("---")

# Page's content
# Loads data and trains the model
data = st.secrets["dataset"]["data"]
df = pd.read_csv(data)


## Loads data
TextElement("# Conhecendo o conjunto de dados")
TextElement.write_caption("---")
TextElement("Primeiro, foi importante analisar o conjunto de dados a fim de saber que tipo de dado ele contém.")
st.dataframe(df)

## Dataset details
TextElement("É um conjunto de dados pequeno de duas colunas: 'diâmetro', 'preço'; contendo 500 linhas.")

## Confirming the connection between attributes
TextElement("## Confirmando a relação entre diâmetro e preço")
TextElement.write_caption("---")
TextElement("Conseguimos claramente estabelecer uma conexão entre diâmetro e preço, pois são proporcionais, ou seja, à medida que o diâmetro aumenta, a pizza fica mais cara.")
TextElement("Para deixar essa conexão mais visual, podemos aplicar gerar um gráfico de dispersão:")

# Rendering scatterplot
fig = px.scatter(data, x="diâmetro", y="preço", title="Relação entre diâmetro e preço", color_discrete_sequence=["yellow"])
st.plotly_chart(fig)

## Detailing the plot
TextElement("Ao observarmos a linha gerada pelo gráfico, confirmamos que realmente há uma clara relação entre os dois atributos (colunas). Sendo assim, podemos aplicar regressão linear a fim de criar um modelo capaz de prever o preço da pizza com base no diâmetro.")

# Footer
Footer.footer()