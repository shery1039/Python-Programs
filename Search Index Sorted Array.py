def search_array_indices_sortedArray(array,a):
    count=0
    for i in range(len(array)):
        count+=1
        if array[i]==a:
            print(count)


array=[0,1,2,3,4,5,6,7,8]
a=int(input("Enter the index of number you want to search for in sorted index: "))
search_array_indices_sortedArray(array,a)
