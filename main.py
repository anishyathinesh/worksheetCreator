# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

print("")
print("Welcome to the Worksheet Generator.")
print("")

print("Type of math operation? (Type +, -, *, or /) : ")
operation = input()
if operation == "-":
    print('Allow negative differences? Type "Y" or "N"')
    negativeDiff = input()
print("Number of problems? ")
numberOfProblems = int(input())
print("Upper operand limit? ")
upperLimit = int(input())


def addition(numberOfProblems, upperLimit):
    for x in range(numberOfProblems):
        num1 = random.randint(0, upperLimit)
        num2 = random.randint(0, upperLimit)
        print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))


def subtraction(numberOfProblems,upperLimit, negativeDiff):
    if negativeDiff == "Y":
        for x in range(numberOfProblems):
            num1 = random.randint(0, upperLimit)
            num2 = random.randint(0, upperLimit)
            print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
    else:
        problemCount = 0
        while problemCount < numberOfProblems:
            num1 = random.randint(1, upperLimit)
            num2 = random.randint(1, upperLimit)
            if num1 > num2:
                quotient = round(int(num1 / num2), 1)
                print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
                problemCount += 1


def multiplication(numberOfProblems, upperLimit):
    for x in range(numberOfProblems):
        num1 = random.randint(0, upperLimit)
        num2 = random.randint(0, upperLimit)
        print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))


def division(numberOfProblems, upperLimit):
    problemCount = 0
    while problemCount < numberOfProblems:
        num1 = random.randint(1, upperLimit)
        num2 = random.randint(1, upperLimit)
        if num1 > num2:
            quotient = round(int(num1 / num2), 1)
            print(str(num1) + " / " + str(num2) + " = " + str(quotient) + " | Remainder = " + str(num1 % num2))
            problemCount += 1

    # for x in range(numberOfProblems):
    #     num1 = random.randint(0, 100)
    #     num2 = random.randint(0, 100)
    #     while num1 > num2:
    #         print(str(num1) + " / " + str(num2) + " = " + round(str(num1 / num2), 1) + " | Remainder = " + num1%num2)


if operation == "+":
    addition(numberOfProblems, upperLimit)
elif operation == "-":
    subtraction(numberOfProblems, upperLimit, negativeDiff)
elif operation == "*":
    multiplication(numberOfProblems, upperLimit)
elif operation == "/":
    division(numberOfProblems, upperLimit)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
