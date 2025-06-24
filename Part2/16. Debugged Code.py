numbers = [5, 10, 15, 20, 25]

for num in numbers:
    if num < 10:
        print(f"{num} is less than 10")
    elif num >= 10 and num < 20:
        print(f"{num} is between 10 and 20")
    elif num == 15:
        print(f"{num} is exactly 15")
    else:
        print(f"{num} is greater than or equal to 20")