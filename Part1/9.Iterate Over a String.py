input_string = "hello"  
vowels = "aeiou"  
vowel_count = 0  
for char in input_string:  
    if char in vowels:  
        vowel_count += 1  # Count the vowel
print("Number of vowels:", vowel_count)
