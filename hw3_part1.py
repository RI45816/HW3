# File: hw3_part1.py
# Author: Uzoma Uwanamodo
# Date: 9/26/2016
# Section: 04
# E-mail: uu3@umbc.edu
# Description:
# Determines if floating point number is positive/negative/zero
# Collaboration:
# I did not collaborate with anyone on this assignment


def main():
    number = float(input("Please enter a floating point number: ")) # Prompt user for floating point number
    if (number == 0): # The number is equal to zero
        print("The number %.1f is equal to zero" % number)
    elif (number < 0 ): # The number is negative
        print("The number %.1f is negative" % number)
    else: # If it's a number, at this point it has to be positive
        print("The number %.1f is positive" % number)

main()