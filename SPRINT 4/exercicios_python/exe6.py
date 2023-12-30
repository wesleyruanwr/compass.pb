def maiores_que_media(conteudo:dict)->list:
    media = sum(conteudo.values()) / len(conteudo)
    maimedia = [(prod, preco) for prod, preco in conteudo.items() if preco > media]
    maimediaord = sorted(maimedia, key=lambda x: x[1])
    return maimediaord

exe = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

resultado = maiores_que_media(exe)
print(resultado)
