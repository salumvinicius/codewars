def longest(a1, a2):
    palavra = a1 + a2
    palavra = set(palavra)
    palavra = "".join(str(item) for item in palavra)
    palavra = sorted(palavra)
    return "".join(palavra)