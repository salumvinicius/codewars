def move_zeros(lst):
    resultado = lst
    for numero in lst:
        if numero == 0:
            resultado.remove(numero)
            resultado.append(numero)
    
    return resultado