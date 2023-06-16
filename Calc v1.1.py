while True:
    try:
# Input and Operator ################################################################################      
        print("\n")
        input1 = float(input("Enter First Number  : "))                                          # first number
        print("\n")
        operator = input("Enter operator (+, -, *, /): ")                      # mathematical operator
        if operator not in ('+', '-', '*', '/'):
                print("Invalid operator. Please enter one of the following: +, -, *, /")
                continue
        print("\n")
        input2 = float(input("Enter Second Number : "))                                         # second number
        print("\n")
# Input ##############################################################################################
    except ValueError:
        print("Invalid input. Please enter numbers only.")                 #invalid Input like Letters
        continue
######################################################################################################
#switch case
    if operator == '+':
        print(input1, '+', input2, '=', input1 + input2)                                        #Plus

    elif operator == '-':
        print(input1, '-', input2, '=', input1 - input2)                                        #Minus 
    elif operator == '*' :                              # allow 'x' as a substitute for multiplication
        print(input1, '*', input2, '=', input1 * input2)
# Devide #############################################################################################
    elif operator == '/':
        if input2 == 0:
            print("Invalid input. Cannot divide by zero.")                  #Preventing to devide by 0

            continue
        else:
            
            print(input1, '/', input2, '=', input1 / input2)
##End ################################################################################################   
    print()
    repeat = input("Perform another calculation? (y/n): ")                             #restart to top 
    if repeat.lower() != 'y':
        break
    print()