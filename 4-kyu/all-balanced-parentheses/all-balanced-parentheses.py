def balanced_parens(n):
    results = []
​
    def generate(current_string, open_count, close_count):
        # Ponto de parada: a string está completa
        if len(current_string) == n * 2:
            results.append(current_string)
            return
​
        # Regra 1: Adicionar '(' se ainda pudermos
        if open_count < n:
            generate(current_string + '(', open_count + 1, close_count)
​
        # Regra 2: Adicionar ')' se for válido
        if close_count < open_count:
            generate(current_string + ')', open_count, close_count + 1)
​
    # Inicia o processo
    generate("", 0, 0)
    
    return results
​