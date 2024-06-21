import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count ={
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}
symbol_values ={
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}
def get_slot_machine_spint(rows, cols, symbols):
    all_symbols = []
    
    for symbole , symbole_count in symbols.items():
        for _ in range(symbole_count):
            all_symbols.append(symbole)
            
    columns = []
    
    for _ in range(cols):
        column= []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return(columns)

def print_slot_machines(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], '|', end = '|')
            else:
                print(column[row], end ="")
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit ? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0.")
                
        else:
            print("Please enter an integer.")
            
    return amount

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter an integer.")
            
    return amount

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings = winnings + (values[symbol]* bet)
            winning_lines.append(line+1)
    return winnings, winning_lines
            
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines(1-"+ str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid number of lines.")
        else:
            print("Please enter an integer.")
    return lines
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough balance to bet. your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet will be: ${total_bet}.")
    
    slots = get_slot_machine_spint(ROWS, COLS, symbol_count)
    print_slot_machines(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_values)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *winning_lines)
    
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin or q to quit ")
        if answer == 'q':
            break
        balance += spin(balance)
        
    print(f"You lef with ${balance}")
    

   
main()