num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        sum = num1 + num2
        print(f"result is {sum}")
    case "-":
        sub = num1-num2
        print(f"result is {sub}")
    case "*":
        mul = num1*num2
        print(f" result is{mul}")
    case "/": 
        if num2 != 0:
            div = num1/num2
            print(f"reslut is {div}")
        else:
            print("Cannot divide by Zero.")
