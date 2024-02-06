#Apresente o nome do ator/atriz com a maior média por filme.

import pandas as pd

df = pd.read_csv('actors.csv')
df['Average per Movie'] = df['Total Gross'] / df['Number of Movies']
atorMaiorMedia = df.loc[df['Average per Movie'].idxmax()]

print('a maior media por filme e de: ',atorMaiorMedia['Actor'])

