

def perform_operation(num1, num2, operation):
    if operation == "subtract":
        return num1-num2   
    elif operation == "add":
        return num1+num2
    elif operation == "multiply":
        return num1 * num2
    else:
        if num2 != 0:
            return num1/num2
        elif num2 == 0:
            return print("You can't divde by zero")
        else :
            return print("Invalid inpute")






