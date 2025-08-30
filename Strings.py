# String handling refers to operations that allow you to manipulate and interact with string data types. Strings are sequences of characters enclosed in single quotes (') or double quotes (").
1. String Declaration

You can define strings in Python using single or double quotes:

string1 = 'Hello'
string2 = "World"

2. String Concatenation

To combine strings, you use the + operator:

greeting = 'Hello' + ' ' + 'World'
print(greeting)  # Output: Hello World

3. String Repetition

You can repeat a string by multiplying it with a number:

greeting = 'Hello ' * 3
print(greeting)  # Output: Hello Hello Hello 

String Slicing

Strings in Python support slicing, allowing you to extract a portion of the string by specifying a start, stop, and step index.

Syntax:
string[start:stop:step]

start: The starting index (inclusive).

stop: The ending index (exclusive).

step: The step size (optional).

Examples:
s = "Hello, World!"

# Extract characters from index 0 to 4 (5 is exclusive)
print(s[0:5])  # Output: Hello

# Extract characters from index 7 to end
print(s[7:])   # Output: World!

# Extract every second character
print(s[::2])  # Output: Hlo ol!

# Reverse the string
print(s[::-1])  # Output: !dlroW ,olleH

String Methods

Python provides a rich set of built-in string methods that make string manipulation easy.

1. len(): Get the length of a string
s = "Hello"
print(len(s))  # Output: 5

2. lower(): Convert a string to lowercase
s = "Hello"
print(s.lower())  # Output: hello

3. upper(): Convert a string to uppercase
s = "Hello"
print(s.upper())  # Output: HELLO

4. strip(): Remove leading and trailing whitespace
s = "   Hello   "
print(s.strip())  # Output: Hello

5. replace(old, new): Replace occurrences of a substring with a new substring
s = "Hello, World!"
print(s.replace("World", "Python"))  # Output: Hello, Python!

6. split(): Split a string into a list based on a delimiter (default is space)
s = "Hello, World!"
print(s.split(", "))  # Output: ['Hello', 'World!']

7. join(iterable): Join elements of a sequence (like a list) into a single string, separated by the string it's called on
words = ['Hello', 'World']
print(" ".join(words))  # Output: Hello World

8. find(substring): Return the index of the first occurrence of a substring. Returns -1 if not found.
s = "Hello, World!"
print(s.find("World"))  # Output: 7

9. count(substring): Count how many times a substring appears in the string
s = "Hello, World! Hello again!"
print(s.count("Hello"))  # Output: 2

10. startswith(prefix): Check if a string starts with the given prefix
s = "Hello"
print(s.startswith("He"))  # Output: True

11. endswith(suffix): Check if a string ends with the given suffix
s = "Hello"
print(s.endswith("lo"))  # Output: True

12. isalpha(): Check if all characters in the string are alphabetic
s = "Hello"
print(s.isalpha())  # Output: True

s2 = "Hello123"
print(s2.isalpha())  # Output: False

13. isdigit(): Check if all characters are digits
s = "12345"
print(s.isdigit())  # Output: True

s2 = "123a5"
print(s2.isdigit())  # Output: False

14. isupper() / islower(): Check if all characters are in uppercase or lowercase
s = "HELLO"
print(s.isupper())  # Output: True

s2 = "hello"
print(s2.islower())  # Output: True

15. title(): Capitalize the first letter of each word in the string
s = "hello world"
print(s.title())  # Output: Hello World

16. zfill(width): Pad a string with leading zeros to a specified width
s = "42"
print(s.zfill(5))  # Output: 00042
