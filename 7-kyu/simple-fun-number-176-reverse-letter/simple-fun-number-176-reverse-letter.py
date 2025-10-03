 
def reverse_letter(st):
    result = ""
    for letra in st:
        if letra.isalpha():
            result += letra
        else:
            pass
    print(result)
    return reversed(result)
            