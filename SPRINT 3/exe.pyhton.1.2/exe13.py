a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []


def potencia(i):
    result = i ** 2
    b.append(result)


def my_map(lista, f):
    for i in lista:
        f(i)


my_map(a, potencia)
print(b)