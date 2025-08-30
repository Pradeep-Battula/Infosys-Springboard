# Program to print a square of numbers

n = int(input("Enter the value of n: "))

count = 1  # Start counting from 1

for i in range(n):
    # Loop through columns
    for j in range(n):
        print(count, end=" ")
        count += 1
    print()
