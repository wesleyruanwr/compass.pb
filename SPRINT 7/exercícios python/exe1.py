#Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.

import pandas as pd

df = pd.read_csv('actors.csv')
maxFilmesAtor= df.loc[df['Number of Movies'].idxmax()]

print(f'a pessoa que fez mais filmes foi:', maxFilmesAtor['Actor'])
print(f'com', maxFilmesAtor['Number of Movies'], 'filmes')