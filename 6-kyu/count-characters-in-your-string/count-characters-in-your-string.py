def count(texto):
    contagem_caracteres = {}
    for caractere in texto:
        if caractere in contagem_caracteres:
            contagem_caracteres[caractere] += 1
        else:
            contagem_caracteres[caractere] = 1
    
    return contagem_caracteres