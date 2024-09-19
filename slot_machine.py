#A function is something we can call to execute a certain block of code and continuously return a value
import random

MAX_LINES = 3 #Global constant
MAX_BET = 100
MIN_BET = 1


ROWS = 3
COLS = 3

#Random Selection
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#Choosing which line to be betted on
def check_winnings(columns, lines, bet, values):
    #Only the lines they bet on
    winnings = 0
    winning_lines = []
    for line in range(lines): #looping through every row that is checking the user bet on
        symbol = columns[0][line]  #Symbol being checked is on the first rwo of the column
        for column in columns: #Loop through every single column to check the column
            symbol_to_check = column[line]
            if symbol != symbol_to_check: #Symbol check if they are not the same
                break  #Which means we will go tho the next line because the first line did not check/win
        else:
            #If the symbol is the same for the whole line
            winnings += values[symbol] * bet  #User won
            winning_lines.append(line + 1)
            
    return winnings, winning_lines


#Generating outcome using the symbol count randomly
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []  #Defining the columns list
    for _ in range(cols):  #Generate a column for every single column we have
        #Picking random values for each row in our column
        column = []
        current_symbols = all_symbols[:] #Copying a list
        for _ in range(rows): #looping through the number of values needed to generate
            value =  random.choice(current_symbols) # Picks a random value from the list
            current_symbols.remove(value) #Removes value so we can't pick it again
            column.append(value) #Adding the value to our column
            
        columns.append(column)
    
    return columns

#Printing the generation code 
def print_slot_machine(columns):
    #Transposing
    for row in range(len(columns[0])): #Assuming that we have at least 1 column 
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
            
        print()
            
            
#For collecting user input 
def deposit():   
    while True: #Continually ask the user to enter a deposit amount until i'm given a valid amount
        amount = input("What would you like to deposit? $")
        #Check if the amount is a number
        if amount.isdigit():  
            amount = int(amount)
        #Check if the number is greater than zero
            if amount > 0:
                break #Ends the while loop
            else:
                print("Your amount must be greater than 0.")
        else:
            print("Please enter a number.")
            
    return amount

#Collecting the bet
def get_number_of_lines():
    while True: #Continually ask the user to enter a deposit amount until i'm given a valid amount
        lines = input("Enter the number of lines to bet on( 1-" + str(MAX_LINES) + ")? ")
        #Check if the lines is a number
        if lines.isdigit():  
            lines = int(lines)
        #Check if the line is less than or equal 1
            if 1 <= lines <= MAX_LINES:
                break #Ends the while loop
            else:
                print("Kindly, enter valid number of lines.")
        else:
            print("Please enter a number.")
            
    return lines

#Amount i want to bet on each line
def get_bet():
    while True: #Continually ask the user to enter a deposit amount until i'm given a valid amount
        amount = input("What amount would you like to bet on each line? $")
        #Check if the amount is a number
        if amount.isdigit():  
            amount = int(amount)
        #Check if the number is greater than zero
            if MIN_BET <= amount <= MAX_BET:
                break #Ends the while loop
            else:
                print(f"Your amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
            
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet =  bet * lines
        
        if total_bet > balance:
            print(f"You don't have enough to bet that amount, Your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    
    #Generating the slots Machine
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet
    
#To call the function
def main():  #Just incase i want to rerun the program
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance =+ spin(balance) #Updating the balance
    
    print(f"You left with ${balance}")
    
main()