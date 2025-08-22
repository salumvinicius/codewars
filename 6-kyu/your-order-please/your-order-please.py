def order(sentence):
    sentence = sentence.split()
    resultado = [''] * len(sentence)
    for i in sentence:
        for x in i:
            if x.isdigit():
                indice = int(x) - 1
                resultado[indice] = i
    
    return ' '.join(resultado)