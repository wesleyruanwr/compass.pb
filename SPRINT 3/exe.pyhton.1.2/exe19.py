import random

random_list = random.sample(range(500), 50)
ord_list = sorted(random_list)

c = ((len(ord_list)) + 1) /2

mediana = ord_list[c] -1
media = sum(ord_list) / len(ord_list)
valor_minimo = min(ord_list)
valor_maximo = max(ord_list)

print(f'Media: {media}, Mediana {mediana}, Mínimo {valor_minimo}, Máximo: {valor_maximo}')
