# Program to find sum of n terms in the series: (x)^2, (xx)^2, (xxx)^2 ...

# Input values
x = int(input("Enter the digit x: "))
n = int(input("Enter the number of terms n: "))

total_sum = 0

for i in range(1, n + 1):
    # Create the number by repeating digit x, i times
    num = int(str(x) * i)
    total_sum += num ** 2

print(f"The sum of {n} terms in the series is: {total_sum}")
