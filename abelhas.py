import pandas as pd
import plotly.express as px
import streamlit as st
import folium
import streamlit_folium 
import json
import plantas_permanentes  
import plantas_temporarias  

df_list = []
df_list_permanente = []
estados = ['al','ba', 'ce','ma','pb','pe', 'pi','rn','se']

############################# INPUT: Plantas permanentes ############################# 
for estado in estados:
    xl = pd.ExcelFile('https://github.com/Victor-Alves1/projeto-abelhas-streamlit/raw/test-env/data/producao_agricola_permanente/pam_'+estado+'_permanente.xlsx')
    df_list = df_list + df_list_permanente + plantas_permanentes.trata_planilha(xl)

############################# INPUT: Plantas temporarias #############################
#xl2 = pd.ExcelFile("https://github.com/Victor-Alves1/projeto-abelhas-streamlit/raw/master/pam_pe_temporario.xlsx")
#df_list_temporario = []
#df_list = df_list + plantas_temporarias + plantas_temporarias.trata_planilha(xl)

############################# UNION: Unindo em um unico dataframe #############################
dataset = pd.concat(df_list)

# Retirando espaço em branco a esquerda e a direita
dataset['cidade'] = dataset['cidade'].str.strip()

# Filtrando apenas estados com produção > 0
dataset = dataset[dataset['Quantidade produzida (Toneladas)'] > 0]

# Criando dataset
series = dataset[['cidade','producao','Quantidade produzida (Toneladas)']]

# Excluindo plantas temporarias
#excluding_sugar_cane = dataset[dataset["temporaria/permanente"] == 'Temporaria']

#############################  Transform: Tratando tabela de produção #############################
# Separando duas colunas para o mapa
prod_per_city = series[['cidade','Quantidade produzida (Toneladas)']]

# Somando produção das cidades
sum_prod_per_city = prod_per_city.groupby('cidade').sum()

# Reindexando após soma
sum_prod_per_city = sum_prod_per_city.reset_index()

#series.plot.bar(x = 'cidade' , y = 'Quantidade produzida (Toneladas)', index = 'producao', stacked=True)

#############################  Transform: Tratando tabela de eficiencia #############################
# Separando as três colunas para o mapa
somando_prod_e_area = dataset[['cidade','Quantidade produzida (Toneladas)', 'Área colhida (Hectares)']]

# somando_prod_e_area


# Somando produção das cidades
somando_prod_e_area = somando_prod_e_area.groupby('cidade').sum()

# Reindexando após soma
somando_prod_e_area = somando_prod_e_area.reset_index()

#############################  Transform: Tratando tabela de rendimento #############################
# Separando duas colunas para o mapa
rendimento_per_city = dataset[['cidade','Valor da produção (Mil Reais)']]

# Somando produção das cidades
sum_rendimento_per_city = rendimento_per_city.groupby('cidade').sum()

# Reindexando após soma
sum_rendimento_per_city = sum_rendimento_per_city.reset_index()

############################# CREATING: Criando gráfico de barras #############################
fig = px.bar(series, x='cidade', y='Quantidade produzida (Toneladas)', color='producao', title="Produção agricola de Pernambuco" )

############################# PLOTANDO: Título #############################
st.title('Produção agrícola em Pernambuco')

# Sidebar
#st.sidebar.header('User Input')
#symbol = st.sidebar.text_input('Escolha um ativo:', 'AAPL')

############################# PLOTING: Grafico de barras de produtividade #############################
st.plotly_chart(fig)

############################# PLOTING: Tabela de produtividade #############################
st.dataframe(dataset)

# Subindo dados do geo_json
# Origem dos dados https://github.com/tbrugz/geodata-br
brazil_data = open('data/geo_data/ne_geo_json.json', 'r')
state_geo = json.load(brazil_data)

tab1, tab2, tab3 = st.tabs(["🗺️ Produção (t)", " 🎍 Eficiencia (Kg/t)", "💸 Rendimento (1.000 reais)"])

with tab1:
    st.header("🗺️ Produção (t)")

    # Criando mapa
    m1 = folium.Map(location=(-8.36, -38.02), zoom_start=7, control_scale=True)

    # Populando mapa coropletico
    folium.Choropleth(
        geo_data=state_geo,
        #name="choropleth",
        data=sum_prod_per_city,
        columns=['cidade', 'Quantidade produzida (Toneladas)'],
        key_on="feature.properties.name",
        nan_fill_color = "white",
        fill_color="YlGn",
        fill_opacity=1,
        line_opacity=0.5,
        legend_name="Produção agricola em Pernambuco",
        highlight=True
    ).add_to(m1)

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
    m1.add_child(highlight)
    #folium.LayerControl().add_to(m)
    streamlit_folium.st_folium(m1)
    st.dataframe(sum_prod_per_city)

with tab2:
    st.header("🎍 Rendimento (Kg/t)")
    st.dataframe(somando_prod_e_area)

with tab3:
    st.header("💸 Rendimento (1.000 reais)")
    st.dataframe(sum_rendimento_per_city)



    

