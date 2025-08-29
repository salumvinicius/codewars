def narcissistic( value ):
    result = 0
    for x in str(value):
        digito = int(x)
        result += digito ** len(str(value))
        
    return result == value