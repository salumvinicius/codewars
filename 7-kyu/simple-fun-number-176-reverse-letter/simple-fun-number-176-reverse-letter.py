def reverse_letter(st):
    result = []
    for letra in st:
        if letra.isalpha():
            result.append(letra)
        else:
            pass
        
    return "".join(reversed(result))
            