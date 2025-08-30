# Program to count vowels in a string

# Input from user
text = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Count vowels
count = 0
for ch in text:
    if ch in vowels:
        count += 1

print(f"The number of vowels in the string is: {count}")
