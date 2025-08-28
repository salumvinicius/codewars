def to_jaden_case(string):
    # 1. Cria uma lista vazia para guardar as palavras capitalizadas
    resultado = []
    
    # 2. Usa .split() para separar a string em uma lista de palavras
    palavras = string.split()
    
    # 3. Faz um loop "for" para passar por cada palavra
    for palavra in palavras:
        # 4. Capitaliza a palavra e a adiciona na lista "resultado"
        resultado.append(palavra.capitalize()) # .title() também funciona bem aqui
        
    # 5. Usa .join() para unir a lista de volta em uma única string
    return " ".join(resultado)
​