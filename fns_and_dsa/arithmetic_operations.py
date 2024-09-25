

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

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
        else :
            return print("Invalid inpute")



if __name__ == "__main__":
    main()



