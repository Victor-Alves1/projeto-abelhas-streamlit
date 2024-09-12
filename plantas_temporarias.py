import pandas as pd
import plotly.express as px
import streamlit as st
import folium
import streamlit_folium 
import json

def trata_planilha (xl2):
  df_list = []
  for i in xl2.sheet_names:
    df = pd.read_excel(xl2, sheet_name = i, skiprows=[0,1,2,3])
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