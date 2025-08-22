def josephus(items,k):
    resultado = []
    
    ponteiro = 0
    
    while items:
        ponteiro = (ponteiro + k - 1) % len(items)
        resultado.append(items.pop(ponteiro))
    
    return resultado