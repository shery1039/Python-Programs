def Minimum(array, start, end):
    min_index = start
    for i in range(start, end + 1):
        if array[i] < array[min_index]:
            min_index = i
    return min_index

a = int(input("How many numbers you want to enter: "))
array = []

for i in range(a):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

start = int(input("Enter the starting index: "))
end = int(input("Enter the ending index: "))

min_index = Minimum(array, start, end)
print(f"The minimum element is at index: {min_index}")