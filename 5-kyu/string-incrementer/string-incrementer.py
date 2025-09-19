def increment_string(string):
    
    indice_inicio_numero = len(string)
    for i in range(len(string) - 1, -1, -1):
        if not string[i].isdigit():
            break
        indice_inicio_numero = i
  
    prefixo = string[:indice_inicio_numero]
    numero_str = string[indice_inicio_numero:]
​
​
    if not numero_str:
        return string + "1"
  
    else:
        tamanho_numero = len(numero_str)
    
        novo_numero = int(numero_str) + 1
​
        novo_numero_str = str(novo_numero).zfill(tamanho_numero)
    
        return prefixo + novo_numero_str