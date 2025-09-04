def is_pangram(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = []
    string = st.lower()
    for letra in string:
        if letra not in letters and letra.isalpha():
            letters.append(letra)
    if len(letters) == 26:
        return True
    else:
        return False