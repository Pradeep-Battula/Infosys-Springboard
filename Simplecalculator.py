# Simple Calculator in Python

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation: ")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1' or choice == '+':
    print(f"Result = {num1 + num2}")
elif choice == '2' or choice == '-':
    print(f"Result = {num1 - num2}")
elif choice == '3' or choice == '*':
    print(f"Result = {num1 * num2}")
elif choice == '4' or choice == '/':
    if num2 != 0:
        print(f"Result = {num1 / num2}")
    else:
        print("Error! Division by zero.")
else:
    print("Invalid choice!")
