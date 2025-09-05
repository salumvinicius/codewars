def DNA_strand(dna):
    result = ""
    for letra in dna:
        if letra == "A":
            result += "T"
        if letra == "T":
            result += "A"
        if letra == "G":
            result += "C"
        if letra == "C":
            result += "G"
    
    return result