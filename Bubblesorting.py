def bubble_sort(arr1):
    n=len(arr1)
    
    for i in range (n):
        swapped=False
        for j in range(n-i-1):
            if arr1[j]>arr1[j+1]:
                arr1[j+1],arr1[j]=arr1[j],arr1[j+1]
                swapped=True
                if not swapped:
                    break

arr1=[2,-5,-90,3,6,-4,88,4000,30,-7]
bubble_sort(arr1)

print("Sorted array is ", arr1)