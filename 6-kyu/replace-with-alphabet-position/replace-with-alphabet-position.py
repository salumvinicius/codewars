def alphabet_position(text):
    result = []
    lower_text = text.lower()
    for x in lower_text:
        if x.isalpha():
            result.append(str(ord(x) - ord("a") + 1))
    return " ".join(result)
    