import pandas as pd


import os

os.system('cls')


dados = {
    'filmes':['Os Vingadores', 'Ghost', 'As Branquelas', 'Esqueceram de mim'],
    'gênero': ['Ação', 'Romance', 'Comédia','Comédia'],
    'ano': [2020, 1990, 2004, 1995]

}
df = pd.DataFrame(dados)

print(df, '\n')

# mostra filmes
s_filmes = pd.Series(df['filmes'])
print(30* '=')
print(f'aqui é a série filmes \n {s_filmes}') 

# mostra o gênero
s_genero = pd.Series(df['gênero'])
print(30*'=')
print(f'aqui é a serie gênero \n {s_genero}')

# mostra o ano
s_ano = pd.Series(df['ano'])
print(30*'=')
print('Aqui mostra o ano')
print(30*'=')

print(s_ano)

# Aplicando filtro
tipo_filme = df.loc[df['gênero'] == 'Comédia']
print(30*'=')
print('Aqui ta filtrando por comedia')
print(30*'=')

print(tipo_filme)

