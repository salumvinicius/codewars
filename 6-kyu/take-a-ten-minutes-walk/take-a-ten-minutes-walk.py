def is_valid_walk(walk):
    pos_x = 0
    pos_y = 0
    if len(walk) != 10:
        return False
    
    if len(walk) == 10:
        for i in walk:
            if i == 'n':
                pos_x += 1
        
            elif i == 's':
                pos_x -= 1
        
            elif i == 'w':
                pos_y -= 1
        
            elif i == 'e':
                pos_y += 1
    
    return True if pos_x == 0 and pos_y == 0 else False