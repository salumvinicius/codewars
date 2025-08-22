def rot13(message):
    resultado = ''
    for letra in message:
        if letra.isalpha():
            letra_asc = ord(letra)
            letra_asc = letra_asc + 13
        
            if letra.isupper():
                if letra_asc > ord('Z'):
                    letra_asc -= 26
            else:
                if letra_asc > ord('z'):
                    letra_asc -= 26
            
            resultado += chr(letra_asc)
        
        else:
            resultado += letra
    return resultado
​