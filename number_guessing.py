import random

#telling the user to guess the number
top_of_range = input("Type a number: ")

#Making sure the number typed is actually a number & converting
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number larger than 0!")
else:
    print("Please type a number!")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

#Asking the user to type in the guess for the number till they get it correct.
while True:
    guesses += 1
    user_guess = input("Guess: ")
    if user_guess.isdigit():         #Checking if it's a number and converting
        user_guess = int(user_guess)
    else:
        print("Please type a number!")
        continue
    
    if user_guess == random_number:
        print("Yeeeyy!")
        break
    elif user_guess > random_number:
        print("Too high!")
    else:
        print("Below the number")
        
print("You had", guesses, "guesses")