# Numbers used in operations
global Num1
Num1 = float(input("First number "))
global Num2
Num2 = float(input("Second number "))
global out
out = 1



# Clean repeat, resets all data
def clean_repeat():

    global Num1
    Num1 = float(input("First number "))
    global Num2
    Num2 = float(input("Second number "))
    global out
    out = 1

    select()
    r = input("Do another operation (y/n), or regular repeat(r)? ")
    if r == "y" or r == "Y":
        clean_repeat()
    elif r == "r" or r == "R":
        repeat()
    else:
        print("End!")


# repeats the program if needed
def repeat():
    select()
    r = input("Do another operation (y/n), or clean repeat(c)? ")
    if r == "y" or r == "Y":
        global Num2
        Num2 = float(input("Second number to operate with "))
        repeat()
    elif r == "c" or r== "C":
        clean_repeat()
    else:
        print("End!")



# select what operation you want to do
def select():
    check = str(input("Enter sign of operation "))
    if check == "+":
        add()
    elif check == "-":
        take()
    elif check == "*":
        multi()
    elif check == "/":
        devide()
    else:
        print("That operation hasn't been implemented yet (available: +, -, *, /)")
        select()



# Function for adding numbers
def add():
    global out
    if out == 1:
        out = Num1 + Num2
        print(out)
    else:
        out = out + Num2
        print(out)

# Function for takeaway
def take():
    global out
    if out == 1:
        out = Num1 - Num2
        print(out)
    else:
        out = out - Num2
        print(out)

# Function for multiplying
def multi():
    global out
    if out == 1:
        out = Num1 * Num2
        print(out)
    else:
        out = out * Num2
        print(out)

# Function for dividing
def devide():
    global out
    if out == 1:
        out = Num1 / Num2
        print(out)
    else:
        out = out / Num2
        print(out)

repeat()