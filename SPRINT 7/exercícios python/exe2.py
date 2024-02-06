#Apresente a média da coluna contendo o número de filmes.

import pandas as pd

df = pd.read_csv('actors.csv')
mediaFilmes = df['Number of Movies'].mean()

print(f'A quantidade media de filmes e', mediaFilmes)