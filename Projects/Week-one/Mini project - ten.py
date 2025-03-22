# 10. **Random Password Generator**  

import random

# Define the characters to use in the password
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

# Combine all characters
all_characters = letters + numbers + symbols

# Ask the user for password length
password_length = int(input("Enter password length: "))

# Create an empty password string
password = ""

# Generate the password using a loop
for i in range(password_length):
    password += random.choice(all_characters)

# Print the generated password
print("Generated Password:", password)
