def merge_sorted_arrays(arr):
    negative_array = []
    positive_array = []

    for num in arr:
        if num < 0:
            negative_array.append(num)
        else:
            positive_array.append(num)

    negative_array.sort()
    positive_array.sort()

    i, j = 0, 0
    mergearray = []

    while i < len(negative_array) and j < len(positive_array):
        mergearray.append(negative_array[i])  
        mergearray.append(positive_array[j])  
        i += 1
        j += 1

    mergearray.extend(negative_array[i:])
    mergearray.extend(positive_array[j:])

    return mergearray

arr = [10, -1, 9, 20, -3, -8, 22, 9, 7]
result = merge_sorted_arrays(arr)
print(result)