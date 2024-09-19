print("Welcome to the quiz!")

playing = input("Do you want to play? ")  #Asks the user to start typing in the console

if playing != "yes":  #Checking if the variable is not equal to yes
    quit()
    
print("Okay! Let's play :) ")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")