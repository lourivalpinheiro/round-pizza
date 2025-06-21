# Importing the necessary modules
from classes.data.apiconnection import ApiConnection
from classes.ui.pages import Page
from classes.ui.textelements import TextElement
from classes.ui.title import Title
from classes.ui.header import Header
from classes.ui.footer import Footer
import streamlit as st
import plotly.express as px

# Page's main configuration
welcomePage = Page("Análise", icon="🔎", pageLayout="centered")
Header.hide_header()
Title("🔎 Processo simples de análise")
TextElement.write_caption("---")

# Page's content
# Loads data and trains the model
df = ApiConnection.get_data()

## Loads data
TextElement("# Conhecendo o conjunto de dados")
TextElement.write_caption("---")
TextElement("Primeiro, gerei um conjunto de dados aleatório a fim de possuir dados para alimentar o modelo. Em seguida, segui para analisá-lo a fim de me familiarizar.")
st.dataframe(df)

## Dataset details
TextElement("É um conjunto de dados pequeno de duas colunas: 'diâmetro', 'preço'; contendo 50 linhas.")

## Confirming the connection between attributes
TextElement("## Confirmando a relação entre diâmetro e preço")
TextElement.write_caption("---")
TextElement("Conseguimos claramente estabelecer uma conexão entre diâmetro e preço, pois deveriam ser proporcionais, ou seja, à medida que o diâmetro aumenta, a pizza fica mais cara.")
TextElement("Para deixar essa conexão mais visual, podemos gerar um gráfico de dispersão:")

# Rendering scatterplot
x = df["diametro"].dropna()
y = df["preco"].dropna()
fig = px.scatter(df, x=x, y=y, title="Relação entre diâmetro e preço", color_discrete_sequence=["yellow"])
st.plotly_chart(fig)

## Detailing the plot
TextElement("Ao observarmos o gráfico, confirmamos que realmente há uma clara relação entre os dois atributos (colunas) e aplicaremos regressão linear a fim de criar um modelo capaz de prever o preço da pizza com base no diâmetro.")

# Footer
Footer.footer()