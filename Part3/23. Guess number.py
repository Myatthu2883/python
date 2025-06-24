#Import the random module to generate a random number
import random

#Function to handle the guessing game
def guess_number():
    #Generate a random number between 1 and 9 (inclusive)
    number_to_guess = random.randint(1, 9)
    
    #Infinite loop that keeps running until the correct guess
    while True:
        #Asking the user to enter a number between 1 and 9
        user_guess = int(input("Enter your guess (between 1 and 9): "))
        
        #Check if the guessed number matches the generated number
        if user_guess == number_to_guess:
            #If the guess is correct, print success message and break the loop
            print("Guessed correctly!")
            break
        else:
            #If the guess is incorrect, prompt the user to try again
            print("Wrong guess, try again!")

#Call the function to start the game
guess_number()