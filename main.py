from operations import operation, select, continueRunning

# if python code is meant to be ran as a executable ==> use this conditional to make sure program is ran from right entrypoint
# in short, this application can only be ran from main.py file
if __name__=='__main__':
    isRunning = True
    while isRunning:
        num1, num2, op = select()
        result = operation(num1, num2, op)
        print(result)
        isRunning = continueRunning()