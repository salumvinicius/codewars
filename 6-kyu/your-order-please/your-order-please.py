def order(sentence):
    lista = []
    for palavra in sentence.split():
        for letra in palavra:
            if letra.isdigit():
                lista.append(letra + palavra)
    lista = sorted(lista)
    resultado = []
    for palavra_1 in lista:
        resultado.append(palavra_1[1:])
    return " ".join(resultado)