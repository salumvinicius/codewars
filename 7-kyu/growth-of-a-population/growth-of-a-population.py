def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        years += 1
        p0 = p0 + p0 * percent//100 + aug
    print(p0)
    print(p)
    return years