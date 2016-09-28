# File: hw3_part3.py
# Author: Uzoma Uwanamodo
# Date: 9/26/2016
# Section: 04
# E-mail: uu3@umbc.edu
# Description:
# Determines whether the water is a solid/liquid/gas
# Collaboration:
# I did not collaborate with anyone on this assignment

def main():
    KELVIN = 273 # Add 273 to celsius amount for Kelvin
    temperature = float(input("Please enter the temperature: ")) # ask user for temperature
    scale = KELVIN if input("Please enter C for Celsius, or 'K' for Kelvin: ") == "K" else 0 # ask user for scale
    if temperature - scale > 100:
        print("At this temperature, water is a gas") # >100C (373K)
    elif temperature - scale > 0:
        print("At this temperature, water is a liquid") # 0-100C (273-373K)
    else:
        print("At this temperature, water is a (frozen) solid") # <0C (273K)
        
main()