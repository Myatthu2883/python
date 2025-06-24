characters = ['A', 'B', 'C']
combinations = []
for char1 in characters:
    for char2 in characters:
        combinations.append(char1 + char2)
print("Character Combinations:", combinations)