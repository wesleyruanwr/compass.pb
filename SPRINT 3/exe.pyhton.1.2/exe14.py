def funcao(*args, **kwargs):  #os 2 asteriscos criam um dicionario criado, args e uma tupla
    for parametro in args:
        print(parametro)

    for k, i in kwargs.items():
        print(f'{i}')

funcao(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)