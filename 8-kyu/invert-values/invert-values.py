def invert(lst):
    list = []
    
    for numbers in lst:
        list.append(numbers - numbers *2)
    
    return list