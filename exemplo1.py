import pandas as pd


import os


os.system('cls')
dados = {
    'cargos': ['assistente', 'auxiliar', 'gerente', 'auxiliar'],
    'salario': [2500, 1800, 750, 1900]

}

df = pd.DataFrame(dados)
print(df, '\n')
# print(df) transforma os dados em tabela

# Mostra os cargos
serie_cargos = pd.Series(df['cargos'])
# print(serie_cargos)

# mostra o salario
serie_salario = pd.Series(df['salario'])
# print(serie_salario)

# mostra o indice
# print(serie_cargos.index)

# imprime valores da serie
# print(serie_cargos.values)

#
# serie_linha = df.iloc[1]
# print(serie_linha)

# indice textual
# serie_colunas = df.loc[:, 'cargos']
# print(serie_colunas)
# df.index = ['A','B','C']
# serie_colunas = df.loc['A']
# print(serie_colunas, '\n')

# Acessando valores individuais
# print(df.iloc[1]['cargos'])
# print(df.iloc[1]['salario'])

# iloc para localizar por indice
# print(serie_cargos.iloc[0])

# por posição na serie
# print(serie_cargos[serie_cargos.index[0]])

# posição no dataframe
# print(df.iloc[0])


# aplicação de filtro
# print(df[df['cargos'] == 'auxiliar'])
salarios = df.loc[df['cargos'] == 'auxiliar', 'salario'].values
print(salarios)