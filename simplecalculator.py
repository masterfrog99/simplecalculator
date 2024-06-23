print("Welcome!")
n1 = float(input("Put a number: "))
n2 = float(input("Put a number: "))

operator = input("Put an operator: ")
def operation(operator):
    match operator:
        case '+':
            return print(n1 + n2)
        case '*':
            return print(n1 * n2)
        case '-':
            return print(n1 - n2)
        case '/':
            return print(n1 / n2)
        case '**':
            return print(n1 ** n2)
print(operation(operator))
