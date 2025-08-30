# Program to print only alphabets from a string

text = input("Enter a string: ")

only_alphabets = ""

for ch in text:
    if ch.isalpha():   # check if character is an alphabet
        only_alphabets += ch

print("Alphabets in the string:", only_alphabets)
