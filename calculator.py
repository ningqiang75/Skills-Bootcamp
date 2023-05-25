import os


# define a function to check if a given string can be converted to a float number
def number_or_not(a):
    try:
        float(a)
        return True
    except ValueError:
        return False


# define a function that allow users to do calculations
def calculator():
    print("Welcome to the calculator application!\n")
    while True:
        try:

            # get two numbers input from user
            num1 = input("Please enter the first number: ")
            if not number_or_not(num1):
                raise ValueError("Invalid input. Please enter a number.")
            num2 = input("Please enter the second number: ")
            if not number_or_not(num2):
                raise ValueError("Invalid input. Please enter a number.")

            # convert input numbers to floats
            num1 = float(num1)
            num2 = float(num2)

            # get an operator from user
            operator = input("Please enter the operator (+, -, *, /): ")
            if operator not in ['+', '-', '*', '/']:
                raise ValueError("Invalid operator. Please enter +, -, *, or /.")

            # perform operating based on user's input
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':

                # return to the input step if user is going to devide a number by zero
                if num2 == 0:
                    print("Error: Cannot divide by zero\n")
                    continue
                result = round(num1 / num2, 2)

            # print the operation result in readable format
            print(f"The result of {num1} {operator} {num2} is {result}\n")

            # append the operation to the "equations.txt" file
            with open('equations.txt', 'a') as f:
                f.write(f"{num1} {operator} {num2} = {result}\n")
        except ValueError as e:

            # print the error message if there is error
            print(f"Error: {e}\n")
        else:

            # ask user to choose perform another calculation or quit when the last operation was successful
            while True:
                again = input("Would you like to perform another calculation? (y/n): ")
                if again.lower() in ['y', 'n']:
                    break
                print("Invalid input. Please enter y or n.")
            if again.lower() == 'n':
                break


# define a function that allows user to read equations from a file
def read_equations():
    while True:
        try:

            # get file name input from user
            filename = input("Please enter the name of the equations file: ")
            if not os.path.isfile(filename):
                raise FileNotFoundError(f"Error: {filename} does not exist.")

            # read equations from the file if it exist and store them to the variable "equations"
            with open(filename, 'r') as f:
                equations = f.readlines()
            break
        except (FileNotFoundError) as e:

            # print an error message if there is an error
            print(f"Error: {e}\n")
    for equation in equations:
        print(equation.rstrip())


# main code body of the program
while True:
    print("1 - Calculator\n2 - Read equations from file")

    # get option input from user
    choice = input("Please enter your choice: ")
    if choice == '1':
        calculator()
        break
    elif choice == '2':
        read_equations()
        break
    else:
        print("Invalid choice. Please enter 1 or 2.\n")
