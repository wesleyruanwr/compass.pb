def listas(list):
    qtd = (len(list)//3)     # as duas barras '//' garantem que sera uma divisao inteira
    global a, b, c
    a = list[:qtd]
    b = list[qtd:qtd*2]
    c = list[qtd*2:]    
    

a = []
b = []
c = []
listas([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(a, b, c)
