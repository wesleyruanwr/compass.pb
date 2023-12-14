def soma(str):
    num_int = [int(numero) for numero in str.split(',')]
    total = sum(num_int)
    print(total)


soma("1,3,4,6,10,76")