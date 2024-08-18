import art
import os

print(art.logo)


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculate():
    cont = True
    a = float(input("What is your first number?   "))
    while cont:
        operator = input(f"What is your operator? Choose between: {', '.join(operators)}:   ")
        b = float(input("What is your second number?  "))
        operation = operators[operator]

        ans = operation(a, b)
        print(f"Answer: {ans}")
        computer = input("Would you like to, 'y', continue calculating with this number... or start over, 'n'?     ")

        if computer == "n":
            cont = False
            print(" \n"*3)
            break
        else:
            a = ans

    calculate()


calculate()
