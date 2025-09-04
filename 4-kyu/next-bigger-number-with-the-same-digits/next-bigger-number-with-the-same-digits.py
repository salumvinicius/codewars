def next_bigger(n):
    # 1. Converter o número em uma lista de dígitos.
    digitos = list(str(n))
    
    # 2. Achar o "pivô".
    #    Iteramos de trás para frente, procurando o primeiro dígito que
    #    é menor que o seu vizinho da direita.
    for i in range(len(digitos) - 2, -1, -1):
        if digitos[i] < digitos[i+1]:
            # Pivô encontrado na posição 'i'.
            pivo = digitos[i]
            
            # 3. Achar o "sucessor".
            #    É o menor dígito à direita do pivô que ainda é maior que ele.
            parte_direita = digitos[i+1:]
            sucessor = min(d for d in parte_direita if d > pivo)
            
            # 4. Trocar o pivô com o sucessor.
            #    Primeiro, removemos o sucessor da parte direita.
            parte_direita.remove(sucessor)
            #    Depois, adicionamos o antigo pivô.
            parte_direita.append(pivo)
            #    E então, ordenamos essa parte para que ela seja a menor possível.
            parte_direita.sort()
            
            # 5. Juntar tudo e converter de volta para um número.
            #    Pegamos o início da lista (até onde o pivô estava)...
            inicio = digitos[:i]
            #    ...adicionamos o sucessor...
            inicio.append(sucessor)
            #    ...e juntamos com o resto já ordenado.
            resultado_lista = inicio + parte_direita
            
            # Converte a lista ['6','3','5','7','8'] em "63578" e depois em 63578
            return int("".join(resultado_lista))
​
    # 6. Se o loop terminar, significa que os dígitos já estão na maior
    #    ordem possível (ex: 54321). Retornamos -1.
    return -1
​
# Vamos testar com os exemplos que discutimos:
print(f"O próximo número maior que 513 é: {next_bigger(513)}")
print(f"O próximo número maior que 2017 é: {next_bigger(2017)}")
print(f"O próximo número maior que 58763 é: {next_bigger(58763)}")
print(f"O próximo número maior que 9 é: {next_bigger(9)}")
print(f"O próximo número maior que 531 é: {next_bigger(531)}")