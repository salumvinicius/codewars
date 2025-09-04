def find_short(s):
    x = s.split()
    z = []
    for palavra in x:
        if palavra != "":
            z.append(palavra)
    menor = min(z, key=len)
    return len(menor)