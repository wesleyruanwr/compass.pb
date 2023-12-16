def duplicadas(lista):
    lista_unitaria = list(set(lista))   #metodo set para tirar as duplicadas
    return lista_unitaria


a = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
result = duplicadas(a)
print(result)