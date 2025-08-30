Loop Control Statements

These are used to change the flow of a loop.

break

break exits the loop completely when a certain condition is met.

Example:
for num in range(10):
    if num == 5:
        break  # exit the loop when num is 5
    print(num)


This will output:

0
1
2
3
4

continue

continue skips the current iteration and moves to the next one, without terminating the loop.

Example:
for num in range(10):
    if num == 5:
        continue  # skip the iteration when num is 5
    print(num)


Output:

0
1
2
3
4
6
7
8
9

pass

pass is a placeholder that does nothing but can be used where code is required syntactically, but you don't want to execute anything.

Example:
for num in range(5):
    if num == 3:
        pass  # do nothing when num is 3
    else:
        print(num)


Output:

0
1
2
4

Nested Loops

You can nest loops inside other loops. A nested loop is often used for multi-dimensional data (like lists of lists).

Example:
for i in range(3):  # Outer loop
    for j in range(3):  # Inner loop
        print(f"i = {i}, j = {j}")


Output:

i = 0, j = 0
i = 0, j = 1
i = 0, j = 2
i = 1, j = 0
i = 1, j = 1
i = 1, j = 2
i = 2, j = 0
i = 2, j = 1
i = 2, j = 2

Else Clause with Loops

Both for and while loops can have an else clause that is executed when the loop completes normally (not by a break statement).

Example:
for i in range(5):
    print(i)
else:
    print("Loop completed!")


Output:

0
1
2
3
4
Loop completed!


If you use break inside the loop, the else part won't execute:

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed!")


Output:

0
1
2


No "Loop completed!" is printed because the loop was broken early.
