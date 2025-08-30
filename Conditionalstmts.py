# Control structures are used to control the flow of execution based on conditions or repetitions. The main control structures include conditional statements (if, elif, else) and loops (for, while).

1. Conditional Statements

Conditional statements allow you to execute certain code based on whether a condition is true or false.

if, elif, else

if: The if statement evaluates a condition, and if it's true, the corresponding block of code runs.

elif (else if): If the first if condition is false, the elif condition will be checked.

else: If none of the if or elif conditions are true, the else block will execute.

Syntax:
if condition1:
    # code block if condition1 is True
elif condition2:
    # code block if condition2 is True
else:
    # code block if neither condition is True

Example:
age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are an adult now.")
else:
    print("You are an adult.")
