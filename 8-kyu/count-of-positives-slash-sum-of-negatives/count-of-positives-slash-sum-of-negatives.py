def count_positives_sum_negatives(arr):
    positive = []
    negative = []
    if arr == []:
        return []
    
    for i in arr:
        if i != 0:
            if i>0:
                positive.append(i)
            
            elif i<0:
                negative.append(i)
    count = []
    count2 = []
    count.append(len(positive))
    count2.append(sum(negative))
    
    return count + count2
        