import pandas as pd 
#import numpy as np
#import matplotlib.pyplot as plt

#Carregar os dados da planilha

caminho = 'D:/TCE/Python_2_ para_Análise_de_Dados/210725-main/01_base_vendas.xlsx'

df1 = pd.read_excel(caminho, sheet_name='Relatório de Vendas')
df2 = pd.read_excel(caminho, sheet_name='Relatório de Vendas1')

#Exibir as primeiras linhas para conferir como estão os dados

print('---------- Primeiro Relatório ----------')

print(df1.head())

print('---------- Segundo Relatório ----------')

print(df2.head)

#Verificar se há duplicatas nas duas tabelas

print('Duplicatas no relatório 1: ') 
print(df1.duplicated().sum())     
print('Duplicatas no relatório 2: ')
print(df2.duplicated().sum())

# Agora vamos consolidar as duas tabelas
print('Dados Consolidados: ')
df_consolidado = pd.concat([df1,df2],ignore_index=True)
print (df_consolidado.head())

# Exibir o número de cliente por cidade

clientes_cidade = df_consolidado.groupby('Cidade')['Cliente'].nunique().sort_values(ascending=False)
print('Quantidade de clientes por cidade:')
print(clientes_cidade)

## Número de vendas por plano
vendas_plano = df_consolidado['Plano Vendido'].value_counts().sort_values(ascending=False)
print('Quantidade de vendas por plano:')
print(vendas_plano)

#Exibir as 3 primeiras cidades com mais clientes
top_3_cidades = clientes_cidade.head(3)
print('Top 3 cidades com mais clientes:')
print(top_3_cidades)

#Exibir o total de clientes 
total_clientes = df_consolidado['Cliente'].nunique()
print(f'\n Total de clientes: {total_clientes}')

#Adicionar uma coluna de Status  (exemplo ficticio de análise)
#Vamos classificar os planos como premiun se for enterprise, caso contrário será padrão

df_consolidado['Status'] = df_consolidado['Plano Vendido'].apply(lambda x: 'Premium' if x == 'Enterprise' else 'Padrao')

#Exibir as distribuição dos status

status = df_consolidado['Status'].value_counts().sort_values(ascending=False)
print('\n Distribuição dos status:')
print(status)

#Salvar a tabela dee um arquivo
#Primeiro em excel
df_consolidado.to_excel('dados_consolidados.xlsx', index=False)

#Depois em csv

df_consolidado.to_csv('dados_consolidados_texto.csv', index=False)

#Exibir a mensagem final!
print('\n Aquivos gerados com sucesso!')


