import pandas as pd
import plotly.express as px
import streamlit as st
import folium
from streamlit_folium import st_folium
import json


xl = pd.ExcelFile("https://github.com/Victor-Alves1/projeto-abelhas-streamlit/raw/master/pam_pe_permanente.xlsx")
xl2 = pd.ExcelFile("https://github.com/Victor-Alves1/projeto-abelhas-streamlit/raw/master/pam_pe_temporario.xlsx")

df_list = []
for i in xl.sheet_names:
  df = pd.read_excel(xl, sheet_name = i, skiprows=[0,1,2,3])
  if len(df.columns) != 6:
    continue
  df.rename(columns={'Unnamed: 0':'cidade'}, inplace=True)
  df = df[df["cidade"].str.startswith('     ')]
  df.insert(1, "producao", i)
  df.insert(2, "temporaria/permanente", "Temporaria")
  #df['Área destinada à colheita (Hectares)'] = pd.to_numeric(df['Área destinada à colheita (Hectares)'], errors='coerce')
  #df['Área colhida (Hectares)'] = pd.to_numeric(df['Área colhida (Hectares)'], errors='coerce')
  #df['Quantidade produzida (Toneladas)'] = pd.to_numeric(df['Quantidade produzida (Toneladas)'], errors='coerce')
  #df['Rendimento médio da produção (Quilogramas por Hectare)'] = pd.to_numeric(df['Rendimento médio da produção (Quilogramas por Hectare)'], errors='coerce')
  #df['Valor da produção (Mil Reais)'] = pd.to_numeric(df['Valor da produção (Mil Reais)'], errors='coerce')
  df.loc[df["Área destinada à colheita (Hectares)"] ==  '-', "Área destinada à colheita (Hectares)"] = 0
  df.loc[df["Área destinada à colheita (Hectares)"] ==  '..', "Área destinada à colheita (Hectares)"] = 0
  df.loc[df["Área destinada à colheita (Hectares)"] ==  '...', "Área destinada à colheita (Hectares)"] = 0
  df.loc[df["Área colhida (Hectares)"] ==  '-', "Área colhida (Hectares)"] = 0
  df.loc[df["Área colhida (Hectares)"] ==  '..', "Área colhida (Hectares)"] = 0
  df.loc[df["Área colhida (Hectares)"] ==  '...', "Área colhida (Hectares)"] = 0
  df.loc[df["Quantidade produzida (Toneladas)"] ==  '-', "Quantidade produzida (Toneladas)"] = 0
  df.loc[df["Quantidade produzida (Toneladas)"] ==  '..', "Quantidade produzida (Toneladas)"] = 0
  df.loc[df["Quantidade produzida (Toneladas)"] ==  '...', "Quantidade produzida (Toneladas)"] = 0
  df.loc[df["Rendimento médio da produção (Quilogramas por Hectare)"] ==  '-', "Rendimento médio da produção (Quilogramas por Hectare)"] = 0
  df.loc[df["Rendimento médio da produção (Quilogramas por Hectare)"] ==  '..', "Rendimento médio da produção (Quilogramas por Hectare)"] = 0
  df.loc[df["Rendimento médio da produção (Quilogramas por Hectare)"] ==  '...', "Rendimento médio da produção (Quilogramas por Hectare)"] = 0
  df.loc[df["Valor da produção (Mil Reais)"] ==  '-', "Valor da produção (Mil Reais)"] = 0
  df.loc[df["Valor da produção (Mil Reais)"] ==  '..', "Valor da produção (Mil Reais)"] = 0
  df.loc[df["Valor da produção (Mil Reais)"] ==  '...', "Valor da produção (Mil Reais)"] = 0
  df['Área destinada à colheita (Hectares)'] = df['Área destinada à colheita (Hectares)'].astype(float)
  df['Área colhida (Hectares)'] = df['Área colhida (Hectares)'].astype(float)
  df['Quantidade produzida (Toneladas)'] = df['Quantidade produzida (Toneladas)'].astype(float)
  df['Rendimento médio da produção (Quilogramas por Hectare)'] = df['Rendimento médio da produção (Quilogramas por Hectare)'].astype(float)
  df['Valor da produção (Mil Reais)'] = df['Valor da produção (Mil Reais)'].astype(float)
  df_list.append(df)

for i in xl2.sheet_names:
  df = pd.read_excel(xl2, sheet_name = i, skiprows=[0,1,2,3])
  if len(df.columns) != 6:
    continue
  df.rename(columns={'Unnamed: 0':'cidade'}, inplace=True)
  df = df[df["cidade"].str.startswith('     ')]
  df.insert(1, "producao", i)
  df.insert(2, "temporaria/permanente", "permanente")
  #df['Área destinada à colheita (Hectares)'] = pd.to_numeric(df['Área destinada à colheita (Hectares)'], errors='coerce')
  #df['Área colhida (Hectares)'] = pd.to_numeric(df['Área colhida (Hectares)'], errors='coerce')
  #df['Quantidade produzida (Toneladas)'] = pd.to_numeric(df['Quantidade produzida (Toneladas)'], errors='coerce')
  #df['Rendimento médio da produção (Quilogramas por Hectare)'] = pd.to_numeric(df['Rendimento médio da produção (Quilogramas por Hectare)'], errors='coerce')
  #df['Valor da produção (Mil Reais)'] = pd.to_numeric(df['Valor da produção (Mil Reais)'], errors='coerce')
  df.loc[df["Área plantada (Hectares)"] ==  '-', "Área destinada à colheita (Hectares)"] = 0
  df.loc[df["Área plantada (Hectares)"] ==  '..', "Área destinada à colheita (Hectares)"] = 0
  df.loc[df["Área plantada (Hectares)"] ==  '...', "Área destinada à colheita (Hectares)"] = 0
  df.loc[df["Área colhida (Hectares)"] ==  '-', "Área colhida (Hectares)"] = 0
  df.loc[df["Área colhida (Hectares)"] ==  '..', "Área colhida (Hectares)"] = 0
  df.loc[df["Área colhida (Hectares)"] ==  '...', "Área colhida (Hectares)"] = 0
  df.loc[df["Quantidade produzida (Toneladas)"] ==  '-', "Quantidade produzida (Toneladas)"] = 0
  df.loc[df["Quantidade produzida (Toneladas)"] ==  '..', "Quantidade produzida (Toneladas)"] = 0
  df.loc[df["Quantidade produzida (Toneladas)"] ==  '...', "Quantidade produzida (Toneladas)"] = 0
  df.loc[df["Rendimento médio da produção (Quilogramas por Hectare)"] ==  '-', "Rendimento médio da produção (Quilogramas por Hectare)"] = 0
  df.loc[df["Rendimento médio da produção (Quilogramas por Hectare)"] ==  '..', "Rendimento médio da produção (Quilogramas por Hectare)"] = 0
  df.loc[df["Rendimento médio da produção (Quilogramas por Hectare)"] ==  '...', "Rendimento médio da produção (Quilogramas por Hectare)"] = 0
  df.loc[df["Valor da produção (Mil Reais)"] ==  '-', "Valor da produção (Mil Reais)"] = 0
  df.loc[df["Valor da produção (Mil Reais)"] ==  '..', "Valor da produção (Mil Reais)"] = 0
  df.loc[df["Valor da produção (Mil Reais)"] ==  '...', "Valor da produção (Mil Reais)"] = 0
  df['Área destinada à colheita (Hectares)'] = df['Área destinada à colheita (Hectares)'].astype(float)
  df['Área colhida (Hectares)'] = df['Área colhida (Hectares)'].astype(float)
  df['Quantidade produzida (Toneladas)'] = df['Quantidade produzida (Toneladas)'].astype(float)
  df['Rendimento médio da produção (Quilogramas por Hectare)'] = df['Rendimento médio da produção (Quilogramas por Hectare)'].astype(float)
  df['Valor da produção (Mil Reais)'] = df['Valor da produção (Mil Reais)'].astype(float)
  df_list.append(df)

dataset = pd.concat(df_list)

series = dataset[['cidade','producao','Quantidade produzida (Toneladas)']]
series = series[series['Quantidade produzida (Toneladas)'] > 0]#.head(10)
wide_df = series

excluding_sugar_cane = dataset[dataset["temporaria/permanente"] == 'Temporaria']#.head(10)
prod_per_city = excluding_sugar_cane[['cidade','Quantidade produzida (Toneladas)']]
sum_prod_per_city = prod_per_city.groupby('cidade').sum()
sum_prod_per_city = sum_prod_per_city.reset_index()
#series.plot.bar(x = 'cidade' , y = 'Quantidade produzida (Toneladas)', index = 'producao', stacked=True)


fig = px.bar(wide_df, x='cidade', y='Quantidade produzida (Toneladas)', color='producao', title="Produção agricola de Pernambuco" )

st.title('Produção agricola em Pernambuco')

# Sidebar
#st.sidebar.header('User Input')
#symbol = st.sidebar.text_input('Escolha um ativo:', 'AAPL')

#Criando mapas
brazil_data = open('pernambuco_geo_json.json', 'r')
#brazil_data = json.load(f)
m = folium.Map(location=(-8.36, -38.02), zoom_start=7, control_scale=True)
state_geo = json.load(brazil_data)

folium.Choropleth(
    geo_data=state_geo,
    #name="choropleth",
    data=prod_per_city,
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

st_folium(m, width=725, height =  600)
st.dataframe(sum_prod_per_city)

# Plot
st.plotly_chart(fig)

st.dataframe(dataset)