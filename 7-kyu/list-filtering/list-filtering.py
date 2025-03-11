def filter_list(l):
    list = []
    for x in l:
        if type(x) == int:
            list.append(x)
    
    return list