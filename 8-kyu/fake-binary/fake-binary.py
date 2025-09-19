def fake_bin(x):
    result = []
    for num in x:
        num = int(num)
        if num >= 5:
            result.append("1")
        else:
            result.append("0")
    
    return "".join(result)