# Data types define the kind of value a variable can hold. Understanding these basic data types is crucial for working with Python. Here are the main categories of data types in Python:
#1. Numeric Types

#Integer (int): Whole numbers, both positive and negative, without decimals.

age = 25       # Example of an integer
temperature = -5  # Negative integer

#Float (float): Decimal numbers (i.e., numbers with a fractional part).

price = 19.99   # Example of a float
temperature = -5.5  # Negative float

#Complex (complex): Numbers that have a real and an imaginary part.

z = 2 + 3j  # Example of a complex number

#Operations with numeric types:

#You can perform arithmetic operations like +, -, *, /, and more.

a = 5
b = 2
sum = a + b    # 7
division = a / b  # 2.5

#2. Text Type

#String (str): A sequence of characters enclosed in single, double, or triple quotes.

name = "Alice"          # String using double quotes
greeting = 'Hello!'     # String using single quotes
multi_line = ""
/*"This
is a multi-line
string."""*/
# String using triple quotes

#Strings are immutable, which means once they are created, their values cannot be changed. You can, however, create new strings by manipulating existing ones.

name = "Alice"
new_name = name.upper()  # Converts the string to uppercase
print(new_name)  # "ALICE"

#3. Sequence Types

List (list): An ordered collection of items that can be of different data types. Lists are mutable, meaning you can modify them after creation.

fruits = ["apple", "banana", "cherry"]  # List of strings
numbers = [1, 2, 3, 4, 5]  # List of integers
mixed = [1, "apple", 3.14, True]  # List with mixed data types

#Tuple (tuple): Similar to lists, but immutable. Once created, you cannot modify the elements of a tuple.

coordinates = (10, 20)  # Tuple of integers
colors = ("red", "green", "blue")  # Tuple of strings

#Range (range): Represents a sequence of numbers, typically used in loops. It generates numbers based on a start, stop, and step.

r = range(5)  # Generates numbers 0 to 4
for num in r:
    print(num)

#4. Mapping Type

#Dictionary (dict): A collection of key-value pairs. Keys must be unique and are typically strings, while values can be any data type.

student = {"name": "John", "age": 25, "grade": "A"}

#You can access dictionary values by their keys:

print(student["name"])  # Output: John
student["age"] = 26  # Update the age

#5. Set Types

#Set (set): An unordered collection of unique elements. Sets are mutable, but the elements must be immutable.

fruits = {"apple", "banana", "cherry"}  # Set of strings
numbers = {1, 2, 3, 4, 5}  # Set of integers

#Sets are useful when you want to store a collection of unique items and perform operations like union, intersection, and difference.

a = {1, 2, 3}
b = {2, 3, 4}
union = a | b  # {1, 2, 3, 4}
intersection = a & b  # {2, 3}

#6. Boolean Type

#Boolean (bool): A type that can only have two values: True or False.

is_active = True
is_valid = False

#Boolean logic can be used with comparison and logical operators, such as and, or, not.

x = 10
y = 5
result = x > y  # True

#7. Binary Types

#Bytes (bytes): Immutable sequences of bytes.

b = b"hello"  # Immutable bytes object

#Bytearray (bytearray): Mutable sequences of bytes.

byte_arr = bytearray([65, 66, 67])  # ['A', 'B', 'C']
byte_arr[0] = 90  # Modify value (mutable)

#8. None Type

#None (NoneType): Represents the absence of a value or a null value.

nothing = None

#You will often see None used as a placeholder, or when a function does not explicitly return anything.

#Type Conversion (Typecasting)

#You can convert between different data types using type casting:

#To Integer: int()

x = "10"
y = int(x)  # Converts string to integer

#To Float: float()

x = "3.14"
y = float(x)  # Converts string to float

#To String: str()

x = 10
y = str(x)  # Converts integer to string

#To List: list()

x = (1, 2, 3)
y = list(x)  # Converts tuple to list

#Example of Data Types:

# Variables with different types
name = "Alice"  # String
age = 25        # Integer
height = 5.6    # Float
is_student = True  # Boolean
marks = [85, 90, 78]  # List
coordinates = (10, 20)  # Tuple

# Print type of variables
print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(height))  # <class 'float'>
print(type(is_student))  # <class 'bool'>
print(type(marks))  # <class 'list'>
print(type(coordinates))  # <class 'tuple'>
