import os
from day10_calculator_art import logo

print(logo)


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

repeat = 'n'
while repeat == 'n':
    repeat = 'y'
    num1 = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    while repeat == 'y':
        operator = input("Pick an operation: ")
        if operator not in ['+', '-', '*', '/']:
            break
        num2 = float(input("What's the next number?: "))
        result = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
        num1 = result
        repeat = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if repeat == 'n':
            clear_screen()

print("\nInvalid Input.")
print("Thank you for using our Calculator.")
