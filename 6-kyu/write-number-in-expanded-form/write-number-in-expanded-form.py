def expanded_form(num):
    res = []
    for i , numero in enumerate(str(num)):
        if numero != '0':
            quantidade_zero = len(str(num)) - i - 1
            res.append(numero + '0' * quantidade_zero)
    
    return " + ".join(res)