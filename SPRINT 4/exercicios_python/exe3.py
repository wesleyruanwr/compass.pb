from functools import reduce
def calcula_saldo(lancamentos) -> float:
    debito = lambda tupla: (tupla[0] if tupla[1] == 'C' else -tupla[0])
    trans = map(debito, lancamentos)
    num = reduce(lambda x, y: x + y, trans, 0)
    return num

lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

result = calcula_saldo(lancamentos)
print(f'Valor: {result}')