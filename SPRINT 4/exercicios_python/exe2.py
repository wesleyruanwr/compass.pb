def conta_vogais(texto:str)-> int:
    vog = ['a', 'e', 'i', 'o', 'u']
    minus = lambda m: m.lower() in vog
    tot = list(filter(minus, texto))
    
    return (len(tot))