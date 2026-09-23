#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date:23/09/2026
# Purpose: Create a variable, check its type and print the variable.
# Usage: ./lab2a.py

# TO DO 1: Follow the instructions given in README.md file

x = input("Please enter a number: ")
print("The type of x is:", type(x))
x=int(x)
if x >= 6:
    print("x is greater than or equal to 6!")
    if x >= 4 and x < 12:
        print("x is greater than or equal to 4 and less than 12!")
