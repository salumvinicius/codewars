def two_sum(numbers, target):
    # Dicionário para guardar o número e seu índice: {numero: indice}
    nums_vistos = {}
    
    # Percorre a lista uma única vez, obtendo o índice e o valor
    for indice_atual, numero_atual in enumerate(numbers):
        # Calcula qual número precisamos para completar o alvo
        complemento = target - numero_atual
        
        # Verifica se o complemento já foi visto (está no dicionário)
        if complemento in nums_vistos:
            # Se sim, encontramos o par!
            # Retorna o índice do complemento que guardamos e o índice atual
            return (nums_vistos[complemento], indice_atual)
        
        # Se não encontrou, adiciona o número atual e seu índice ao dicionário
        # para que possa ser encontrado por futuros elementos da lista
        nums_vistos[numero_atual] = indice_atual