import pandas as pd
from google.colab import drive
drive.mount('/content/drive')
df = pd.read_csv("/content/drive/MyDrive/Uninter/Python_atividade_pratica/Stores.csv")

#Renomeando as colunas do DataFrame
df.columns=['Loja', 'Area', 'Itens', 'Visitantes', 'Vendas']

#Valores máximos e mínimos das colunas Itens, Visitantes e Vendas
max_itens = df['Itens'].max()
max_visitantes = df['Visitantes'].max()
max_vendas = df['Vendas'].max()

min_itens = df['Itens'].min()
min_visitantes = df['Visitantes'].min()
min_vendas = df['Vendas'].min()

## Conjunto dos valores médios
conjunto_medias = df.mean()
# Valores médios separado em variavéveis por colunas
media_itens = df['Itens'].mean()
media_visitantes = df['Visitantes'].mean()
media_vendas = df['Vendas'].mean()

## Conjunto dos desvios padrões
conjunto_desvios = df.std(axis=0)
# Desvios padrões separado em variavéveis por colunas
desvio_itens = df['Itens'].std()
desvio_visitantes = df['Visitantes'].std()
desvio_vendas = df['Vendas'].std()

print('=== Itens ====================================')
print(f'O máximo de itens disponíveis foi {max_itens}')
print(f'O mínimo de itens disponíveis foi {min_itens}')
print(f'Média dos itens {media_itens}')
print(f'Desvio padrão dos itens {desvio_itens}')

print('=== Visitantes ===============================')
print(f'O máximo de visitantes foi {max_visitantes}')
print(f'O mínimo de visitantes foi {min_visitantes}')
print(f'Média dos visitantes {media_visitantes}')
print(f'Desvio padrão dos visitantes {desvio_visitantes}')

print('=== Vendas ===================================')
print(f'O máximo de vendas foi {max_vendas}')
print(f'O mínimo de vendas foi {min_vendas}')
print(f'Média das vendas {media_vendas}')
print(f'Desvio padrão das vendas {desvio_vendas}')