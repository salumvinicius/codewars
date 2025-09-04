def reverse_words(text):
    text = text.split(" ")
    final = []
    for palavra in text:
        final.append(palavra[::-1])
    
    return " ".join(final)