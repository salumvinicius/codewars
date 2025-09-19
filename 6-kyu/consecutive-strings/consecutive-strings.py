def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr):
        return ""
    
    longest = ""
    for i in range(len(strarr) - k + 1):
        current = "".join(strarr[i:i+k])  # junta k strings consecutivas
        if len(current) > len(longest):
            longest = current
    return longest