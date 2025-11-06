"""
=========================================
🎯 Project: Random Password Generator
👨‍💻 Author: Ahmed Waled
📅 Date: November 6, 2025
💡 Description: 
    This program generates a random password 
    based on user input for the number of 
    letters, digits, and symbols.
=========================================
"""

import random
import string

print("Welcome to the Password Generator!")

    # Ask user for inputs
length_password = int(input("Enter the total number of characters in the password: "))
letters = int(input("Enter the number of letters in the password: "))
numbers = int(input("Enter the number of numbers in the password: "))
symbols = int(input("Enter the number of symbols in the password: "))

    # Check if the total matches
total_parts = letters + numbers + symbols

if total_parts != length_password:
    print("\n❌ Error: The total numbers don't match the password length.")
    print(f"You entered total {length_password}, but the sum of parts is {total_parts}.")
 
else:
    # Generate password parts
    password_list = []
    password_list += random.choices(string.ascii_letters, k=letters)
    password_list += random.choices(string.digits, k=numbers)
    password_list += random.choices(string.punctuation, k=symbols)

    # Shuffle and combine
    random.shuffle(password_list)
    password = "".join(password_list)

    # Show the result
    print("\n✅ Your random password is:", password)



