import pandas as pd 


try:
    df = pd.read_csv('ClassicDisco.csv' , sep = ',' , encoding= 'utf-8')
    # print(df) metodos de impressão
    # print(df.head()) 
    # print(df.to_string()) 
    # print(df.tail())  imprime as ultimas linhas
    # print(df.info()) mostra as informaçoes
    # print(df.describe())  da estatistica
    # pd.set_option('display.min_rows', 20)
    # print(df)
    # lendo coluna específica
    # artista = df['Track']
    # print(artista)
    # print(artista.to_string())
    # popularidade = df[df['Popularity'] > 20]
    # print(popularidade)
    # print(popularidade [['Track', 'Popularity']])
    # michael_jackson = df[df['Artist']== 'Michael Jackson']
    # print(michael_jackson[['Album', 'Artist']])
    # df.to_csv('Base_modificada.csv', index=False, sep=',', encoding= 'utf - 8')
    df.to_excel('classic_disco_modificado.xls', index=False ,engine='openpyxl')

except Exception as e:
    print(f'Erro {e}')
    exit()