def disemvowel(string_):
    x = ["a","e","i","o","u","A","E","I","O","U"]
    return "".join([char for char in string_ if char not in x])