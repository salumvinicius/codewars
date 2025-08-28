def rgb(r, g, b):
    result = ""
    if 255 >= r >= 0:
        result += hex(r)[2:].upper().zfill(2)
    elif r > 255:
        result += hex(255)[2:].upper().zfill(2)
    elif r < 0:
        result += hex(0)[2:].upper().zfill(2)
    if 255 >= g >= 0:
        result += hex(g)[2:].upper().zfill(2)
    elif g > 255:
        result += hex(255)[2:].upper().zfill(2)
    elif g < 0:
        result += hex(0)[2:].upper().zfill(2)
    if 255 >= b >= 0:
        result += hex(b)[2:].upper().zfill(2)
    elif b > 255:
        result += hex(255)[2:].upper().zfill(2)
    elif b < 0:
        result += hex(0)[2:].upper().zfill(2)
    
    
    return result
    
    
        
​