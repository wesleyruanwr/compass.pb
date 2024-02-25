import random
import names

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f"Gerando {qtd_nomes_aleatorios} nomes")

dados = []
for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

nome_arquivo = "nomes_aleatorios.txt"
with open(nome_arquivo, "w") as arquivo:
    for nome in dados:
        arquivo.write(nome + "\n")

print(f"Arquivo '{nome_arquivo}' gerado!")
