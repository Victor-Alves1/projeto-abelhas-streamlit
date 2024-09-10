import pandas as pd
import plotly.express as px
import streamlit as st
import requests
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
  df = df[df["cidade"].str.startswith('      ')]
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
  df = df[df["cidade"].str.startswith('      ')]
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
print(sum_prod_per_city)
sum_prod_per_city = sum_prod_per_city.reset_index()
print(sum_prod_per_city)
#sum_prod_per_city['cidade'] = sum_prod_per_city['cidade'].astype("string")
sum_prod_per_city['cidade'] = sum_prod_per_city['cidade'].str.strip()

print(sum_prod_per_city)