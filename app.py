import streamlit as st
import ipeadatapy 
import pandas as pd

"""# ***[IPEADATAPY](https://www.luanborelli.net/ipeadatapy/docs/index.html)***

É a API que fornece dados coletados pelo IPEA (Instituto de Pesquisa Econômica Aplicada) a fim de facilitar a acessibilidade aos dados utilizando a linguagem Python em formato de dataframes.

Um ***dataframe*** é uma tabela que pode conter mais de uma coluna, onde cada coluna é um array, sendo que estes ***dataframes*** podem ser manipulados facilmente utilizando a biblioteca pandas.

## ***Extração de dados com a API***

* ***ipeadatapy.list_series()***: fornece um dataframe contendo uma listagem de todas as series com apenas 2 colunas de dados: ***CODE*** e ***NAME***."""
df = ipeadatapy.list_series()
df

"""* ***ipeadatapy.metadata()***: fornece um dataframe contendo uma listagem de todas as series com 15 colunas de dados: ***BIG THEME***, ***SOURCE***, ***SOURCE ACRONYM***, ***SOURCE URL***, ***UNIT***, ***COUNTRY***, ***FREQUENCY***, ***LAST UPDATE***, ***CODE***, ***COMMENT***, ***NAME***, ***NUMERICA***, ***SERIES STATUS***, ***THEME CODE*** e ***MEASURE***."""

df = ipeadatapy.metadata()
df

"""A busca é feita com a passagem de parametros específicos para as funções ***list_series()*** e ***metadata()***"""

"\n"

"* ***ipeadatapy.describe(serieCode)***: fornece um dataframe com os dados ***BIG THEME***, ***SOURCE***, ***SOURCE ACRONYM***, ***SOURCE URL***, ***UNIT***, ***COUNTRY***, ***FREQUENCY***, ***LAST UPDATE***, ***CODE***, ***COMMENT***, ***NAME***, ***NUMERICA***, ***SERIES STATUS***, ***THEME CODE*** e ***MEASURE*** de uma serie especifica."

df = ipeadatapy.describe("ABATE_ABPEAV")
df

"* ***ipeadatapy.timeseries()***: fornece um dataframe da serie parametrada."

df = ipeadatapy.timeseries("ABATE_ABPEAV")
df

"* ***ipeadatapy.latest_updates()***: fornece um dataframe contendo as séries que foram atualizadas mais recentemente."

df = ipeadatapy.latest_updates()
df

"* ***ipeadatapy.sources()***: fornece um dataframe contendo as instituições disponiveis para consulta:"

df = ipeadatapy.sources()
df

"* ***ipeadatapy.themes()***: fornece um dataframe contendo os temas disponiveis para consulta:"

df = ipeadatapy.themes()
df

"* ***ipeadatapy.territories()***: fornece um dataframe contendo os territórios do Brasil com dados disponíveis para consulta:"

df = ipeadatapy.territories()
df

"* ***ipeadatapy.countries()***: fornece um dataframe contendo os países com dados disponíveis para consulta:"

df = ipeadatapy.countries()
df

"""## ***Plotagem dos dados com Streamlit e Pandas***

Adotando o seguinte dataframe:

```
dataframe = pd.DataFrame(dict(YEAR = ipeadatapy.timeseries("ABATE_ABPEAV").iloc[:, -1]))
```

Um dataframe pode ser facilmente plotado com auxilio do Streamlit com as funções:

***(gráficos baseados nas colunas DATE e VALUE da serie ABATE_ABPEAV)***"""

dataframe = pd.DataFrame(dict(VALUE = ipeadatapy.timeseries("ABATE_ABPEAV").iloc[:, -1]))

"* ***st.area_chart(dataframe)***: Gráfico de área"
st.area_chart(dataframe)
"* ***st.bar_chart(dataframe)***: Gráfico em barras"
st.bar_chart(dataframe)
"* ***st.line_chart(dataframe)***: Gráfico linear"
st.line_chart(dataframe)
"* ***st.scatter_chart(dataframe)***: Gráfico em pontos"
st.scatter_chart(dataframe) 

"E de diversas outras maneiras como é definido na [documentação do Streamlit](https://docs.streamlit.io/develop/api-reference/charts)."