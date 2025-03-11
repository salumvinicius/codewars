def is_isogram(string):
    string = string.lower()
    
    unique_letters = set()
    
    for letter in string:
        if letter in unique_letters:
            return False
        unique_letters.add(letter)
    
    return True