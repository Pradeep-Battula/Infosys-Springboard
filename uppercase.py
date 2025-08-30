# Program to print all uppercase letters from a string

text = input("Enter a string: ")

uppercase_letters = ""

for ch in text:
    if ch.isupper():   # check if character is uppercase
        uppercase_letters += ch

print("Uppercase letters in the string:", uppercase_letters)
