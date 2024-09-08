def merge_Sort(left, right):
    new = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    
    new.extend(left[i:])
    new.extend(right[j:])
    return new

A = [0, 3, 4, 10, 11]
B = [1, 8, 13, 24]

result = merge_Sort(A, B)
print(result)