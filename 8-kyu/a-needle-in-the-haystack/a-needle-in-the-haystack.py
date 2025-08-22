def find_needle(haystack):
    x = 0
    for i in haystack:
        if i == "needle":
            return f'found the needle at position {x}'
        elif i != "needle":
            x += 1
        