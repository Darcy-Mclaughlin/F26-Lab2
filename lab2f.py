# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 9/23/2026
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2f.py

# TO DO 1: Follow the instructions given in README.md file

"""
Fill in the required fields in the comment section.
Create a variable called name.
Create another variable called age.
The script should assign the string sys.argv[1] (first argument) to the variable "name"
The script should assign the string sys.argv[2] (second argument) to the variable "age".
The script should use if-elif structure and should print the EXACT OUTPUT as shown below.
"""

import sys

num_args = len(sys.argv) - 1   
if num_args < 2:
    print("This program requires two arguments.")
else:
        name = sys.argv[1]
        age = sys.argv[2]
        if num_args == 3:
            print(f"Hello {name}, you are {age} years old and this script has received three arguments.")
        else:
            print(f"Hello {name}, you are {age} years old and this script has received {num_args} arguments.")    


