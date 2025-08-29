def printer_error(s):
    error_count = 0
    tintas_aceitaveis = "abcdefghijklm"
    for letra in s:
        if letra not in tintas_aceitaveis:
            error_count += 1
    
    return f"{error_count}/{len(s)}"
            