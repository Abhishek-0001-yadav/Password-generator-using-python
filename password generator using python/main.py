print("Select an operator to perform: ")
print("1. ADD")
print("2. SUBSTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The sum of number is" + int(num1) + int(num2))
elif operation == "2":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The substraction of number is" + int(num1) - int(num2))
elif operation == "3":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The Multiplication of number is" + int(num1) * int(num2))
elif operation == "4":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The Division of number is" + int(num1) / int(num2))
else:
    print("Invalid entry")