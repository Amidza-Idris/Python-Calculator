import os

# easy way to calculate instead of making ur bs funtions for every operation
def operation(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        return 'Not valid operation!'

# each time you want to select new numbers+operation entry, we will call this function right below
def select():
    num1 = float(input("Select number 1: "))
    num2 = float(input("Select number 2: "))
    op = str(input("Select operation: "))
    
    #pay attention to how we can return multiple parameters
    return num1, num2, op


def continueRunning():
    isRunning = str(input("Do you want to continue? [PRESS 'Y' or 'y']:  "))
    state = str(input("Do you want to clean console? [PRESS 'Y' or 'y']:  "))

    if state == 'y' or state == 'Y':
        # python os library provides you features to control your system like in commmand prompt
        # here we call just basic clear screen like you would in cmd -> since your console in IDE is just emulated cmd
        os.system('cls')

    # google ternary operator => just very neat and fancy way to write if else statement in one line 
    return True if isRunning == 'Y' or isRunning == 'y' else False





# UR NASTY CODE BELOW!!!
# Function for adding numbers
# def add():
#     global out
#     if out == 1:
#         out = Num1 + Num2
#         print(out)
#     else:
#         out = out + Num2
#         print(out)

# # Function for takeaway
# def take():
#     global out
#     if out == 1:
#         out = Num1 - Num2
#         print(out)
#     else:
#         out = out - Num2
#         print(out)

# # Function for multiplying
# def multi():
#     global out
#     if out == 1:
#         out = Num1 * Num2
#         print(out)
#     else:
#         out = out * Num2
#         print(out)

# # Function for dividing
# def devide():
#     global out
#     if out == 1:
#         out = Num1 / Num2
#         print(out)
#     else:
#         out = out / Num2
#         print(out)