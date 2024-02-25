import random

list_num = [random.randint(1, 1000) for _ in range(250)]
list_num.reverse()

print("\nLista revertida:")
print(list_num)
