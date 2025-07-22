# Simple Calculator in Python
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def modulo(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x % y
def power(x, y):
    return x ** y
while True:
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    print("6. Power")
    print("7. Exit")
    choice = input("\nEnter choice (1-7): ")
    if choice == '7':
        print("Exiting calculator. Goodbye!")
        break
    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid input. Please try again.")
        continue
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        continue
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    result = divide(num1, num2)
    print(f"{num1} / {num2} = {result}")
elif choice == '5':
    result = modulo(num1, num2)
    print(f"{num1} % {num2} = {result}")
elif choice == '6':
    print(f"{num1} ^ {num2} = {power(num1, num2)}")
