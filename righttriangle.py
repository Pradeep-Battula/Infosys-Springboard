# Program to print 2 right-angled triangles of n rows

n = int(input("Enter the number of rows: "))

count = 1 

print("First Triangle:")
for i in range(1, n+1):
    for j in range(i):
        print(count, end=" ")
        count += 1
    print()

count = 1  
print("\nSecond Triangle:")
for i in range(1, n+1):
    for j in range(n, n-i, -1):
        print(count, end=" ")
        count += 1
    print()
