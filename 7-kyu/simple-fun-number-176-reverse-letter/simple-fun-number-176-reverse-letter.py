 
def reverse_letter(st):
    result = ""
    for letra in st:
        if letra.isalpha():
            result += letra
        else:
            pass
    
    return reversed(result)
            