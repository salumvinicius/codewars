def expanded_form(num):
    res = []
    for i , numero in enumerate(str(num)):
        if numero != 0:
            res.append(numero + '0' * len(str(num) - 1))
    
    return res