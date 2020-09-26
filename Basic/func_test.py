def calculate(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        return num1 / num2
    elif op == "*":
        return num1 * num2
    else:
        return "invalid Input"


num1 = int(input("Enter number 1 : "))
op = input("Enter operator : ")
num2 = int(input("Enter number 2 : "))
print(f"{num1}{op}{num2} = {calculate(num1, num2, op)}")
