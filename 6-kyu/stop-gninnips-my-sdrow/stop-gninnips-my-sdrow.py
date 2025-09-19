def spin_words(sentence):
    lista = sentence.split()
    resultado = []
    print(lista)
    for palavra in lista:
        if len(palavra) >= 5:
            palavra_contra = ''
            for letra in reversed(palavra):
                palavra_contra += letra
            resultado.append(palavra_contra)
        else:
            resultado.append(palavra)
    return " ".join(resultado)