#calculate cat age in cat years
def calculate_cat_years(human_years):
    #If the cat is 1 year old, it equals 15 human years
    if human_years == 1:
        return 15
    # If the cat is 2 years old, it equals 24 human years (15 for the first, 9 for the second)
    elif human_years == 2:
        return 24
    # For cats older than 2 years, add 24 for the first two years, then 4 for each additional year
    else:
        return 24 + (human_years - 2) * 4

# Ask the user to input the cat's age in human years
human_years = int(input("Enter your cat's age in human years: "))

# Call the function to calculate the cat's age in cat years
cat_years = calculate_cat_years(human_years)

# Print the result
print(f"Your cat is {cat_years} cat years old.")
