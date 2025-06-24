rows = 3  
cols = 4  
matrix = []  
i = 0  
while i < rows:  
    row = []  
    j = 0  
    while j < cols:  
        row.append(i * j)  
        j += 1  
    matrix.append(row)  
    i += 1  
    
print("Generated Matrix:")  
for row in matrix:
    print(row) 
