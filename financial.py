import pandas as pd

# Caminho para o arquivo Excel
df = r'C:\Users\Matheus.Rodrigues\Desktop\Me\Documentos\Finanças.xlsx'

# Carregar os dados da planilha "Pendentes" e selecionar as colunas necessárias
df_sheet1 = pd.read_excel(df, header=1, usecols=[
                          1, 2, 3, 4, 5, 6, 7], sheet_name="Pendentes")
df_sheet2 = pd.read_excel(df, header=1, usecols=[
                          1, 2, 3, 4, 5, 6, 7], sheet_name="Realizadas")
df_sheet3 = pd.read_excel(df, header=1, usecols=[
                          1, 2, 3, 4, 5, 6, 7], sheet_name="Recebidos")

# Concatenar sheet
df_combined = pd.concat([df_sheet1, df_sheet2, df_sheet3], ignore_index=True)

# Criar uma função para classificar os valores
def classificar_valor(valor):
    if valor > 500:
        return "Muito Alto"
    elif valor > 100:
        return "Médio"
    else:
        return "Baixo"

# Aplicar a função à coluna "Valor" para criar a coluna "Classificação"
df_combined["Classificação"] = df_combined["Valor"].apply(classificar_valor)

# Converter Data em datatype
df_combined["Data"] = pd.to_datetime(df_combined["Data"])

# Converter Data em nome mês
df_combined["Mês"] = df_combined["Data"].dt.month_name()

# Filtrar somente pelo mês de Janeiro
df_janeiro = df_combined[df_combined["Mês"] == "January"]

# Transformar o mês filtrado em df_month
df_month = df_janeiro

df_month = df_month.groupby(["Mês"])["Valor"].sum().reset_index()

# Exibir o DataFrame resultante
print(df_month)