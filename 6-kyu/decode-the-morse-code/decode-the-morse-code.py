from preloaded import MORSE_CODE
​
def decode_morse(morse_code):
    frase = ''
    morse_code = morse_code.strip().replace("   "," | ")
    for letter in morse_code.split(" "):
        if letter != '|':
            frase += MORSE_CODE[letter]
        
        if letter == '|':
            frase += ' '
    
    return frase