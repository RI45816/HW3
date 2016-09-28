# File: hw3_part4.py
# Author: Uzoma Uwanamodo
# Date: 9/26/2016
# Section: 04
# E-mail: uu3@umbc.edu
# Description:
# Convert day of month into a weekday, starting with Sunday at day 1
# Collaboration:
# I did not collaborate with anyone on this assignment

def main():
    HIGHEST_DATE = 30 # The highest allowed date, date cannot exceed this value
    LOWEST_DATE = 1 # The lowest date, date cannot go below this value
    WEEKDAY = 7 # Only seven days in the week, divide the date by this number
    WEEKDAYS = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    date = int(input("Please enter the day of the month: ")) # Ask user for day of the month
    if date not in range(LOWEST_DATE, HIGHEST_DATE):
        print("The date %s is an invalid day." % date) # Date is not between 1-30
    else:
        date = date % WEEKDAY - 1 # Get the date to index form
        print("Today is a %s!" % WEEKDAYS[date])
        
main()
        