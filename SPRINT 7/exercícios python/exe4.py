# Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
import pandas as pd

df = pd.read_csv('\\Users\\Wesley Ruan\\compass.pb\\SPRINT 7\\exercícios python\\actors.csv')
frequencFilmes= df['#1 Movie'].value_counts()
filmesFrequentes= frequencFilmes[frequencFilmes == frequencFilmes.max()]

print("Filme(s) mais frequente(s) e sua respectiva frequência:")
for movie, frequency in frequencFilmes.items():
    print("Filme:", movie)
    print("Frequência:", frequency)
