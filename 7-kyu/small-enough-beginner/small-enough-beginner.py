def small_enough(array, limit):
    res = []
    for numero in array:
        if numero > limit:
            return False
        else:
            res.append(numero)
    if res == array:
        return True