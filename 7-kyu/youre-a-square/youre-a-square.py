def is_square(n):    
    if n < 0:
        return False
    root = n ** 0.5
    return root % 1 == 0