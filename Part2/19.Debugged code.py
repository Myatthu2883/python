def check_numbers(x, y):
    if x >= y:
        print(f"{x} is greater than or equal to {y}")
    else:
        print(f"{x} is less than {y}")
i , j = 0,0
while i < 2:
    while j < 2:
        check_numbers(i, j)
        j += 1
    i += 1
    j = 0