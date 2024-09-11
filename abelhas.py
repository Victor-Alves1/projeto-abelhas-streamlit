import pandas as pd
import plotly.express as px
import streamlit as st
import folium
import streamlit_folium 
import json
import plantas_permanentes  
import plantas_temporarias  

df_list = []

############################# INPUT: Plantas permanentes #############################
xl = pd.ExcelFile("https://github.com/Victor-Alves1/projeto-abelhas-streamlit/raw/master/pam_pe_permanente.xlsx")
df_list_permanente = []
df_list = df_list + df_list_permanente + plantas_permanentes.trata_planilha(xl)

############################# INPUT: Plantas temporarias #############################
#xl2 = pd.ExcelFile("https://github.com/Victor-Alves1/projeto-abelhas-streamlit/raw/master/pam_pe_temporario.xlsx")
#df_list_temporario = []
#df_list = df_list + plantas_temporarias + plantas_temporarias.trata_planilha(xl)

############################# UNION: Unindo em um unico dataframe #############################
dataset = pd.concat(df_list)
#dataset = pd.DataFrame(df_list)

#############################  Transform: Tratando tabela #############################
# Criando dataset
series = dataset[['cidade','producao','Quantidade produzida (Toneladas)']]

# Filtrando apenas estados com produção > 0
series = series[series['Quantidade produzida (Toneladas)'] > 0]

# Copiando dataset para criação do mapa
wide_df = series

# Excluindo plantas temporarias
excluding_sugar_cane = dataset[dataset["temporaria/permanente"] == 'Temporaria']

# Separando duas colunas para o mapa
prod_per_city = excluding_sugar_cane[['cidade','Quantidade produzida (Toneladas)']]

# Somando produção das cidades
sum_prod_per_city = prod_per_city.groupby('cidade').sum()

# Reindexando após soma
sum_prod_per_city = sum_prod_per_city.reset_index()

# Retirando espaço em branco a esquerda e a direita
sum_prod_per_city['cidade'] = sum_prod_per_city['cidade'].str.strip()

#series.plot.bar(x = 'cidade' , y = 'Quantidade produzida (Toneladas)', index = 'producao', stacked=True)

############################# CREATING: Criando gráfico de barras #############################
fig = px.bar(wide_df, x='cidade', y='Quantidade produzida (Toneladas)', color='producao', title="Produção agricola de Pernambuco" )

############################# PLOTANDO: Título #############################
st.title('Produção agrícola em Pernambuco')

# Sidebar
#st.sidebar.header('User Input')
#symbol = st.sidebar.text_input('Escolha um ativo:', 'AAPL')

# Subindo dados do geo_json
brazil_data = open('pernambuco_geo_json.json', 'r')
state_geo = json.load(brazil_data)

# Criando mapa
m = folium.Map(location=(-8.36, -38.02), zoom_start=7, control_scale=True)

# Populando mapa coropletico
folium.Choropleth(
    geo_data=state_geo,
    #name="choropleth",
    data=sum_prod_per_city,
    columns=['cidade', 'Quantidade produzida (Toneladas)'],
    key_on="feature.properties.name",
    nan_fill_color = "white"
    #fill_color="YlGn",
    #fill_opacity=0.4,
    #line_opacity=0.2,
    #legend_name="Produção agricola em Pernambuco"
    #highlight=True
).add_to(m)

#Adicionando a função de destaque
estilo = lambda x: {"fillColor": "white",
                   "color": "black",
                   "fillOpacity": 0.001,
                   "weight": 0.001}

estilo_destaque = lambda x: {"fillColor": "darkblue",
                            "color": "black",
                            "fillOpacity": 0.5,
                            "weight": 1}

highlight = folium.features.GeoJson(data = state_geo,
                                   style_function = estilo,
                                   highlight_function = estilo_destaque,
                                   name = "Destaque")

#Adicionando caixa de texto
folium.features.GeoJsonTooltip(fields = ["name"],
                              aliases = ["Cidade"],
                               labels = False,
                              style = ("background-color: white; color: black; font-family: arial; font-size: 16px; padding: 10px;")).add_to(highlight)

#Adicionando o destaque ao mapa
m.add_child(highlight)

#folium.LayerControl().add_to(m)

streamlit_folium.st_folium(m, width=800)
st.dataframe(sum_prod_per_city)

############################# PLOTING: Grafico de barras de produtividade #############################
st.plotly_chart(fig)

############################# PLOTING: Tabela de produtividade #############################
st.dataframe(dataset)