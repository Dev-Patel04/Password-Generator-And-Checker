# Define the function to check password validity
def IsValidPass(password):
    # Check if the password length is more than 8 characters
    if len(password) > 8:
        # Initialize flags for each type of character
        lowerCase, upperCase, number, symbols = False, False, False, False

        # Iterate over each character in the password
        for char in password:
            if char.islower():  # Check for lowercase letter
                lowerCase = True
            if char.isupper():  # Check for uppercase letter
                upperCase = True
            if char.isdigit():  # Check for digit
                number = True
            if not char.isalnum():  # Check for non-alphanumeric characters, i.e., symbols
                symbols = True

        # Return True if all types of characters are present
        return lowerCase and upperCase and number and symbols
    else:
        # Return False if the password is not longer than 8 characters
        return False

# Prompt the user to enter a password
password = input("Enter Your Password: ")

# Call the IsValidPass function and print appropriate message based on its return value
if IsValidPass(password):
    print("This Is A Valid Strong Password")
else:
    print("This Password Is Weak")
