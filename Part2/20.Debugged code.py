def compare_number(x, y):
    if x > y:
        print(f"{x} is greater than {y}")
    elif x == y:
        print(f"{x} is equal to {y}")
    else:
        print(f"{x} is less than {y}")
numbers1 = [18, 27]
numbers2 = [32, 12]
for i in numbers1:
    for j in numbers2:
        compare_number(i, j)
