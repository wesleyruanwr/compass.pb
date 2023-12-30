def calcular_valor_maximo(operadores, operandos):
    oper = zip(operadores, operandos)

    ope = lambda op, tupla: {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }[op](tupla[0], tupla[1])

    result = list(map(lambda x: ope(*x), oper))
    valormax = max(result)
    return valormax

operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]
resultmax = calcular_valor_maximo(operadores, operandos)

print(resultmax)