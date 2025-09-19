def solution(number):
    res = 0
    for number in range(number):
        if number % 3 == 0 or number % 5 == 0:
            res += number
    return res
  