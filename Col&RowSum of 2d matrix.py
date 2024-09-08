matrix = [
    [1, 13, 13], 
    [5, 11, 6 ],  
    [4, 4,  9 ]  
]


Col_sum1=0

for i in range(3):
    Row_sum1=0
    for j in range(3):
        Row_sum1+=matrix[i][j]
        
    print("Row",Row_sum1)
    
for i in range(3):
    Col_sum1=0
    for j in range(3):
        Col_sum1+=matrix[j][i]
    print("Col", Col_sum1)
