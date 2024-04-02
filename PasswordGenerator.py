import random

# Character sets
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCase = upperCase.lower()
digits = "0123456789"
symbols = "~`!@#$%^&*()_-+={[}]|\:;<,>.?/"

# Flags to include character types
upper , lower, nums, symbol = True, True, True, True

# Initialize the pool of characters based on flags
password = ""

if upper: 
    password += upperCase
if lower: 
    password += lowerCase
if nums: 
    password += digits
if symbol: 
    password += symbols

# Ask user for the desired password length
length = int(input("Enter the desired length of the password: "))
amount = 10  # Number of passwords to generate

# Generate and print passwords
for x in range(amount):
    password = "".join(random.sample(password, length))
    print(password)