def search_array_indices(arr, a):
    for i in range(len(arr)):
        if arr[i] == a:
            print(i)

array = [22, 2, 1, 7, 11, 13, 5, 2, 9]
a = int(input("Enter the number you searched for: "))

search_array_indices(array, a)