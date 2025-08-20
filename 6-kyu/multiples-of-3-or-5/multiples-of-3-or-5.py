def solution(number):
    soma = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            soma += i
    return soma
  