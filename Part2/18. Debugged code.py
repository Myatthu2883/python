i = 0
while i < 2:
    j = 0
    while j < 2:
        if i == j:
            print(f"i and j are equal: i={i}, j={j}")
        elif i > j:
            print(f"i is greater than j: i={i}, j={j}")
        else:
            print(f"i is less than j: i={i}, j={j}")
        j += 1
    i += 1