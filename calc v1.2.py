# Input and Operator ######################################################################################
MAX_RETRIES = 3

while True:
    input1 = input2 = operator = None
    for i in range(MAX_RETRIES):
        try:
            print("\n")
            input1 = float(input("Enter First Number  : "))
            print("\n")
            operator = input("Enter operator (+, -, *, /): ")
            if operator not in ('+', '-', '*', '/'):
                print("Invalid operator. Please enter one of the following: +, -, *, /")
                continue
            print("\n")
            input2 = float(input("Enter Second Number : "))
            print("\n")
            if input2 == 0 and operator == '/':
                print("Invalid input. Cannot divide by zero.")
                input2 = None
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    if input1 is None or input2 is None or operator is None:
        print("You exceeded the number of attempts to correct your input.")
        break

    # Perform calculation ###################################################################################
    if operator == '+':
        result = input1 + input2
        print(f"{input1} + {input2} = {round(result, 2)}")
    elif operator == '-':
        result = input1 - input2
        print(f"{input1} - {input2} = {input1(result, 2)}")
    elif operator == '*':
        result = input1 * input2
        print(f"{input1} * {input2} = {input1(result, 2)}")
    elif operator == '/':
        print(f"{input1} / {input2} = {input1(result, 2)}")

    # Ask to repeat ########################################################################################
    print()
    repeat = input("Perform another calculation? (y/n): ")
    if repeat.lower() != 'y':
        break
    print()