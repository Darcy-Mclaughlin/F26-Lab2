# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 9/23/2026
# Purpose: Practice using if and else statments.
# Usage: ./lab2b.py

# TO DO 1:
# Follow the instructions given in the README.md file.

"""
### lab2b.py
#### Using if-else statement
- Fill in the required fields in the comment section.
- Use the input() function and ask the user to enter a 4 digit integer. Save this value in the variable `num`.
- The program should print out "George Orwell" if the number is exactly 1984, and otherwise prints “Not quite right!”. Use `if`, and `else` statement.
"""

num = input("Please enter a 4 digit integer: ")
if num == "1984":
    print("George Orwell")
else:
    print("Not quite right!")
