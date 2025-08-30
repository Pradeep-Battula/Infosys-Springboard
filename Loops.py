# Loops

Loops allow you to repeat a block of code multiple times based on a condition.

for Loop

The for loop iterates over a sequence (like a list, tuple, string, or range) and executes a block of code for each item.

Syntax:
for item in sequence:
    # code block

Example:
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


Output:

apple
banana
cherry

while Loop

The while loop executes a block of code as long as a given condition is true.

Syntax:
while condition:
    # code block

Example:
counter = 1

while counter <= 5:
    print(counter)
    counter += 1


Output:

1
2
3
4
5
