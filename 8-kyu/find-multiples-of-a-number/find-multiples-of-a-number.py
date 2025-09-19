def find_multiples(integer, limit):
    res = []
    for num in range(integer , limit + 1, integer):
        res.append(num)
    
    return res