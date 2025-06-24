rows = 3
cols = 4
matrix =[]
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * j)
    matrix.append(row)
print("Generated Matrix:")
for row in matrix:
    print(row)        