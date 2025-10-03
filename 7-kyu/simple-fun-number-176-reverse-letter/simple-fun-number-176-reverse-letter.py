 
def reverse_letter(st):
    result = ""
    for letra in st:
        if letra.isalpha():
            result += letra
        else:
            pass
    print(reversed(result))
    return reversed(result)
            