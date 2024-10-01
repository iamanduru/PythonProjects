import random 

#randrange() generates random number within a specified range
num = random.randrange(1000, 10000)

x = int(input("Guess the 4 digit number: "))

#To test equality of the guess made
if (x == num ):
    print("Yeey! You guessed the number in just 1 try! Sawaa Guru!!")
else: 
    #Count the number of tries
    ctr = 0
    while (x != num ):   #Repeats as long as the player fails
        ctr += 1
        count = 0
        x = str(x)
        num = str(num)   #Converts strings to integers
        correct = ['X'] * 4  #Stores digits which are correct
        
        #For loop runs the digit 4 times since the number has 4 digits
        for i in range (0,4):
            #Checking equality of digits
            if (x[i] == num[i]):
                count += 1
                correct[i] = x[i]
            else:
                continue
            print("You did get", count, "digits(s) correct!")
            print('\n')
            print('\n')
            x = int(input("Enter your next guess: "))
            
    # when none of the digits are guessed correctly.
        elif (count == 0):
            print("None of the numbers in your input match.")
        n = int(input("Enter your next choice of numbers: "))

        # condition for equality.
        if n == num:
        # ctr must be incremented when the n==num gets executed as we have the other incrmentation in the n!=num condition
            ctr+=1
        print("You've become a Mastermind!")
        print("It took you only", ctr, "tries.")