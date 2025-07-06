def reverse_txt(txt):
    return txt[::-1]
print(reverse_txt("Python Advanced"))

def calculator():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Select operation ['+', '-', '/', '*']: ").lower()
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "/":
        return num1 / num2
    elif operation == "*":
        return num1 * num2
    else:
        return "Invalid operation"
    
print(calculator()
