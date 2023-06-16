
#Version 1.4


# Input and Operator
MAX_RETRIES = 3

while True:
    input1 = input2 = operator = None
    for i in range(MAX_RETRIES):
        try:
            
            print("\n")# Skips line for the output
            input1 = float(input("Enter First Number  : "))# Asks for first input 
            print("\n")# Skips line for the output
            
            operator = input("Enter operator (+, -, *, /): ")# Asks for operator listed  
            if operator not in ('+', '-', '*', '/'):
                print("Invalid operator. Please enter one of the following: +, -, *, /")#error message
                continue
            
            print("\n")# Skips line for the output
            input2 = float(input("Enter Second Number : "))# Asks for second input 
            print("\n")# Skips line for the output
            if input2 == 0 and operator == '/':
                print("Invalid input. Cannot divide by zero.")#error message
                input2 = None
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")#error message
    if input1 is None or input2 is None or operator is None:
        print("You exceeded the number of attempts to correct your input.")#error message
        break

# Perform calculation and gives output and rounds it to 2 desimals
    if operator == '+':
        result = input1 + input2
        print(f"{input1} + {input2} = {round(result, 2)}")
    elif operator == '-':
        result = input1 - input2
        print(f"{input1} - {input2} = {round(result, 2)}")
    elif operator == '*':
        result = input1 * input2
        print(f"{input1} * {input2} = {round(result, 2)}")
    elif operator == '/':
        if input2 == 0:
            print ("Invalid Input. Cannot devide by Zero")
        else:
            result = input1 / input2
            print(f"{input1} / {input2} = {round(result, 2)}")

# Ask to repeat and repromt back to the top 
    print()
    repeat = input("Perform another calculation? (y/n): ")#repromt
    if repeat.lower() != 'y':
        break
    print()