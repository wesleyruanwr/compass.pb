'''Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa. Como saída, imprima o ano em que a pessoa completará 100 anos de idade.'''

for cont in range(1,4):
    num = (int(input(f'Digite o {cont}º numero: ')))
    if num % 2 == 0:
        print(f'Par: {num}')
    else:
        print(f'Ímpar: {num}')
