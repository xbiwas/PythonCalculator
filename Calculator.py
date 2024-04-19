print("Welcome to do some of the calculations")
print("Select first number")
num1 = int(input())
print("Select second Number")
num2 = int(input())

print("Now what do you wanna do with those two numbers")
print("DO you wanna add it, subtract it, multiply it or divide it")
print("Please select an operator from the list below")
operators = ["+", "-", "*", "/"]
print("The operators are: ", operators)
selectOperator = input()

if selectOperator == operators[0]:
    result = num1 + num2
    print(result)
elif selectOperator == operators[1] :
    result = num1 - num2
    print(result)
elif selectOperator == operators[2] :
    result = num1 * num2
    print(result)
else:
    print("You have selected an invalid operator")

