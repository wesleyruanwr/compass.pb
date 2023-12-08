lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for c, i in enumerate(lista):
    rev = i[::-1]   # "[::-1]" é um operador de fatiamento que inicia do final por cponta do -1
    if rev == i:
        print(f'A palavra: {i} é um palíndromo')
    else:
        print(f'A palavra: {i} não é um palíndromo')
