import re                                                                       # Regular expressions for pattern matching                                           


while True:                                                                     # Main program loop
    try:                                                                        # Try-Except block for error handling
        equation = input('\nType your equation:')
        if 'q' in equation:                                                     # 'q' to exit the program
            break
        
        equation = equation.strip().replace('**','^').replace(',','.').replace('x','*').replace(':','/')          # Remove whitespace from the equation and replace ** with ^ to avoid errors and confusion with a single *, and other possible variations of operators. 
        

        numbers = re.findall(r'(?:\d*\.)?\d+', equation)                        # Creating a regular expression pattern to find all numbers in the equation, including decimals
        
        operators = re.findall(r'[-+*/^:]', equation)                           # Find all operators in the equation
        

        
        if equation.startswith('-'):                                            # Check if the equation starts with a minus sign
            numbers[0] = '-' + numbers[0]                                       # Add a minus sign to the first number in the equation
            del operators[0]                                                    # Delete the minus sign from the operators list
        elif equation.startswith('+'):                                          # Check if the equation starts with a plus sign
            del operators[0]                                                    # Delete the plus sign from the operators list as it is redundant

        
            
        if len(operators) == 2:                                                 # If we have two operators between the numbers 
            if operators[0] == '-' and operators[1] == '-':                     # If the first operator is '-' and second is '-'
                operators[0] = '+'                                              # Change the first operator to '+'
                del operators[1]                                                # Delete the second operator
            elif operators[0] == '+' and operators[1] == '-':
                del operators[0]
            elif operators[0] == '+' and operators[1] == '+':
                del operators[1]
            elif operators[0] == '*' and operators[1] == '-':            
                del operators[1]
                numbers[1] = '-' + numbers[1]    
            elif operators[0] == '/' and operators[1] == '-':
                del operators[1]
                numbers[1] = '-' + numbers[1]
            elif operators[0] == '^' and operators[1] == '-':
                del operators[1]
                numbers[1] = '-' + numbers[1]
            else:
                print("Don't know")
            
        #print(operators)
        #print(numbers)         
            
        if len(operators) > 2:                                                  # Check if the equation has more than two operators
            numbers = []                                                        # Clear the numbers list
            operators = []                                                      # Clear the operators list
            print('Error: Too many operators.')
        
        
        if len(numbers) > 2:                                                    # Check if the equation has two numbers, if more then the message is displayed and the program continues
            print('Only two numbers in equation are allowed.')
            continue

        number1 = float(numbers[0])                                             # Creating number1 variable
        number2 = float(numbers[1])                                             # Creating number2 variable

        
        result = None                                                           # Create a variable to store the result

        operator = operators[0]                                                 # Create a variable to store the operator from the operators list
        
        if operator == '+':                                                     # Check if the operator is '+'
                result = number1 + number2                                      # Add the two numbers
        elif operator == '-':                                                   # And so on...     
                result = number1 - number2
        elif operator == '*':
                result = number1 * number2
                
        elif operator == '^':                                                   # Check if the operator is '^' for exponential calculation
            try:                                                                
                result = number1 ** number2
                    
            except OverflowError:                                               # Check if the result is too large to display
                    print('Result too large to display. \nPlease reduce the exponent or set the limit for integer string conversion by defining sys.set_int_max_str_digits(your_number_of_digits) ')
                    continue

        elif operator == '/' :
            try:
                    result = number1 / number2
            except ZeroDivisionError:
                    print("Error: Cannot divide by zero.")
                    continue
                
                     
        result = round(result,2)                # If the result is a float we round the result to two decimal places

        if  result == int(result):              # Check if the result is a whole number and if true:
            result = int(result)                # Convert the result to an integer

        print(f'Result:{result}')

    except :
        continue
