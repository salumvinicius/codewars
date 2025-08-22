def binary_array_to_number(arr):
    potencia = 0
    soma = 0
    for i in reversed(arr):
        i = i * (2 ** potencia)
        potencia += 1
        soma += i
    return soma
    