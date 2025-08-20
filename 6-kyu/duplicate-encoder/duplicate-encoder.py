def duplicate_encode(word):
    string = word.lower()
    result = ""
    for i in string:
        if string.count(i) == 1:
            result += "("
        else:
            result += ")"
    return result