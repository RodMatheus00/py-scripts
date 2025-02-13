import pandas as pd

# Caminho para o arquivo Excel
df_path = r'C:\Users\Matheus.Rodrigues\Desktop\Me\Documentos\content\controles\financeiro.xlsx'

# Carregar as planilhas especificando os nomes das colunas
colunas = ['Data', 'Categoria', 'Descrição', 'Valor', 'Tipo', 'Forma de Pagamento', 'Observações']
df_sheet1 = pd.read_excel(df_path, sheet_name="Pendentes", usecols=colunas)
df_sheet2 = pd.read_excel(df_path, sheet_name="Realizadas", usecols=colunas)
df_sheet3 = pd.read_excel(df_path, sheet_name="Recebidos", usecols=colunas)

# Concatenar as planilhas
df_combined = pd.concat([df_sheet1, df_sheet2, df_sheet3], ignore_index=True)

# Função para classificar os valores
def classificar_valor(valor):
    if valor > 500:
        return "Muito Alto"
    elif valor > 100:
        return "Médio"
    else:
        return "Baixo"

# Aplicar a função à coluna "Valor" para criar a coluna "Classificação"
df_combined["Classificação"] = df_combined["Valor"].apply(classificar_valor)

# Converter a coluna "Data" para datetime e extrair o nome do mês em português
df_combined["Data"] = pd.to_datetime(df_combined["Data"])
df_combined["Mês"] = df_combined["Data"].dt.strftime('%B')

# Filtrar os dados para o mês de janeiro
df_janeiro = df_combined[df_combined["Mês"] == "janeiro"]

# Agrupar por mês e somar os valores
df_month = df_janeiro.groupby(["Mês", df_janeiro["Data"].dt.year])["Valor"].sum().reset_index()

# Exibir o DataFrame resultante
print(df_month)
