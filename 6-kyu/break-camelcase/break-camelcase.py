def solution(s):
    resultado = []
    
    for i in s:
        if i.isupper():
            resultado.append(' ')
        resultado.append(i)
    
    return ''.join(resultado)
        