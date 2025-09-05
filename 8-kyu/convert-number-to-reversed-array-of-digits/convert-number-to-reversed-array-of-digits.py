def digitize(n):
    num = list(str(n))
    numero = []
    for i in num:
        numero.append(int(i))
    
    return numero[::-1]