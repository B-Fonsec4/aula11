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