#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 9/23/2026
# Purpose: Learn how and practice using nested if, elif, and else statments..
# Usage: ./lab2g.py

# TO DO 1: Follow the instructions given in README.md file
# Initialize constant variables for the tax rates and rate limits.

"""
Fill in required fields in comment section.
Create a program calculating tax with the image above
The script should include a variable income.
The value of income should be a number (preferably in the thousands) inputted by the user.
The script should also include a variable status.
The value of status will either be "single" or "married" entered by the user.
Use nested if, elif, and else statements to create a working model of the image above.
Also use relational operators to compare income and status with the threshold values given in your slides.
Test your program with multiple different numbers.
"""

income = float(input("Please enter your income: "))
status = input("Please enter your status (single/married): ").lower()

if status == "single":
    if income <= 32000
        tax = income * 0.10
    else
        tax = (income
