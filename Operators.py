# Operators are symbols that perform operations on variables and values.

1. Arithmetic Operators

These operators are used to perform basic arithmetic operations.

Operator	Description	Example
+	Addition	5 + 3 results in 8
-	Subtraction	5 - 3 results in 2
*	Multiplication	5 * 3 results in 15
/	Division	5 / 2 results in 2.5
//	Floor Division	5 // 2 results in 2 (ignores remainder)
%	Modulus	5 % 2 results in 1 (remainder of division)
**	Exponentiation	5 ** 3 results in 125 (5 raised to the power of 3)
2. Comparison Operators

These operators compare two values and return a boolean value (True or False).

Operator	Description	Example
==	Equal to	5 == 3 results in False
!=	Not equal to	5 != 3 results in True
>	Greater than	5 > 3 results in True
<	Less than	5 < 3 results in False
>=	Greater than or equal to	5 >= 3 results in True
<=	Less than or equal to	5 <= 3 results in False
3. Logical Operators

These are used to combine conditional statements.

Operator	Description	Example
and	Returns True if both conditions are True	True and False results in False
or	Returns True if at least one condition is True	True or False results in True
not	Reverses the result of the condition	not True results in False
4. Assignment Operators

These operators are used to assign values to variables.

Operator	Description	Example
=	Assigns value	x = 5 assigns 5 to x
+=	Add and assign	x += 5 is equivalent to x = x + 5
-=	Subtract and assign	x -= 5 is equivalent to x = x - 5
*=	Multiply and assign	x *= 5 is equivalent to x = x * 5
/=	Divide and assign	x /= 5 is equivalent to x = x / 5
//=	Floor divide and assign	x //= 5 is equivalent to x = x // 5
%=	Modulus and assign	x %= 5 is equivalent to x = x % 5
**=	Exponentiate and assign	x **= 5 is equivalent to x = x ** 5
5. Bitwise Operators

These operators are used for operations on binary numbers.

Operator	Description	Example
&	Bitwise AND	5 & 3 results in 1
`	`	Bitwise OR
^	Bitwise XOR (exclusive OR)	5 ^ 3 results in 6
~	Bitwise NOT	~5 results in -6
<<	Left shift	5 << 1 results in 10
>>	Right shift	5 >> 1 results in 2
6. Identity Operators

These operators compare the memory locations of two objects.

Operator	Description	Example
is	Returns True if two variables point to the same object	x is y
is not	Returns True if two variables do not point to the same object	x is not y
7. Membership Operators

These are used to test if a value is found in a sequence (list, tuple, string, etc.).

Operator	Description	Example
in	Returns True if the value is present in the sequence	'a' in 'apple' results in True
not in	Returns True if the value is not present in the sequence	'z' not in 'apple' results in True
8. Ternary (Conditional) Operator

This is a shorthand way of writing an if-else statement.

Operator	Description	Example
x if condition else y	Returns x if condition is True, else y	5 if 3 > 2 else 0 results in 5

Example Code for Operators:

# Arithmetic Operators
x = 10
y = 3
print(x + y)  # Addition (10 + 3 = 13)
print(x - y)  # Subtraction (10 - 3 = 7)
print(x * y)  # Multiplication (10 * 3 = 30)
print(x / y)  # Division (10 / 3 = 3.3333...)
print(x // y) # Floor Division (10 // 3 = 3)
print(x % y)  # Modulus (10 % 3 = 1)
print(x ** y) # Exponentiation (10 ** 3 = 1000)

# Comparison Operators
print(x == y)  # False (10 is not equal to 3)
print(x != y)  # True (10 is not equal to 3)
print(x > y)   # True (10 is greater than 3)

# Logical Operators
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# Assignment Operators
x += 5  # x = x + 5
print(x)  # 15

# Bitwise Operators
print(x & y)  # AND (10 & 3 = 2)

# Membership Operators
print('a' in 'apple')  # True

# Ternary Operator
result = 'Positive' if x > 0 else 'Negative'
print(result)  # Positive
