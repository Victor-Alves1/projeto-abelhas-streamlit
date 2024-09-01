import pandas as pd
#from IPython.display import display
#import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

#xl = pd.ExcelFile("c:/Users/Victor/Desktop/projeto salvo/abelhas/pam_pe_permanente.xlsx")
#xl2 = pd.ExcelFile("c:/Users/Victor/Desktop/projeto salvo/abelhas/pam_pe_temporario.xlsx")
xl = pd.ExcelFile("https://github.com/Victor-Alves1/projeto-abelhas-streamlit/blob/master/pam_pe_permanente.xlsx")
xl2 = pd.ExcelFile("https://github.com/Victor-Alves1/projeto-abelhas-streamlit/blob/master/pam_pe_temporario.xlsx")
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
#display(df_list[1])
dataset = pd.concat(df_list)
series = dataset[['cidade','producao','Quantidade produzida (Toneladas)']]
series = series[series['Quantidade produzida (Toneladas)'] > 0]#.head(10)
##display(series)
#series.plot.pie(figsize=(6, 6));
#df.groupby(['cidade']).sum()
#series.plot.bar(x = 'cidade' , y = 'Quantidade produzida (Toneladas)', index = 'producao', stacked=True)
wide_df = series

fig = px.bar(wide_df, x='cidade', y='Quantidade produzida (Toneladas)', color='producao', title="Produção agricola de Pernambuco" )

##fig.show()

st.title('Produção agricola em Pernambuco')

# Sidebar
#st.sidebar.header('User Input')
#symbol = st.sidebar.text_input('Escolha um ativo:', 'AAPL')

# Plot
st.plotly_chart(fig)
st.dataframe(dataset)