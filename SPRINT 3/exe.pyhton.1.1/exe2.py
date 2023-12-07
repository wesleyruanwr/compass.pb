for cont in range(1,4):
    num = (int(input(f'Digite o {cont}º numero: ')))
    if num % 2 == 0:
        print(f'Par: {num}')
    else:
        print(f'Ímpar: {num}')
