def move_zeros(lst):
    for x in lst:
        if x == 0:
            lst.remove(x)
            lst.append(x)
    return lst