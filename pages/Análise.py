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
Title("🔎 Processo de análise")
TextElement.write_caption("---")

# Page's content
# Loads data and trains the model
df = ApiConnection.get_data()

## Loads data
TextElement("# Conhecendo o conjunto de dados")
TextElement.write_caption("---")
TextElement("Primeiro, foi importante analisar o conjunto de dados a fim de saber que tipo de dado ele contém.")
st.dataframe(df)

## Dataset details
TextElement("É um conjunto de dados pequeno de duas colunas: 'diâmetro', 'preço'; contendo 50 linhas.")

## Confirming the connection between attributes
TextElement("## Confirmando a relação entre diâmetro e preço")
TextElement.write_caption("---")
TextElement("Conseguimos claramente estabelecer uma conexão entre diâmetro e preço, pois deveriam ser proporcionais, ou seja, à medida que o diâmetro aumenta, a pizza fica mais cara.")
TextElement("Para deixar essa conexão mais visual, podemos gerar um gráfico de dispersão:")

# Rendering scatterplot
x = df["diametro"].str.strip().dropna()
y = df["preco"].str.strip().dropna()
fig = px.scatter(df, x=x, y=y, title="Relação entre diâmetro e preço", color_discrete_sequence=["yellow"])
st.plotly_chart(fig)

## Detailing the plot
TextElement("Ao observarmos a linha gerada pelo gráfico, confirmamos que realmente há uma clara relação entre os dois atributos (colunas). Entretanto, alguns **outliers**, dados que se destacam porque estão muito distantes da maioria dos dados dentro de um conjunto, são identificados, o que pode ocasionar tendências no modelo.")
TextElement("Meu objetivo com esse projeto foi tentar construir um modelo que 'funcionasse', acima de tudo, além de ser capaz de fazer com que vocês usuários fossem capaz de interagir com ele. Então, iremos ignorar a alta probabilidade de tendências e aplicaremos regressão linear a fim de criar um modelo capaz de prever o preço da pizza com base no diâmetro.")

# Footer
Footer.footer()