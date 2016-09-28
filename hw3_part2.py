# File: hw3_part2.py
# Author: Uzoma Uwanamodo
# Date: 9/26/2016
# Section: 04
# E-mail: uu3@umbc.edu
# Description:
# Uses clues to determine the type of dog the user is describing.
# Collaboration:
# I did not collaborate with anyone on this assignment

def main():
    print("Please enter 'yes' or 'no' to these questions") # Ask user for binary yes/no response
    bigDog = True if  input("Is the dog a big dog? ") == "yes" else False # Ask the user if the dog is a big dog
    if bigDog:
        fluffyCoat = True if input("Does the dog have a fluffy coat? ") == "yes" else False # Ask the user if the coat if is fluffy
        if fluffyCoat:
            print("\nYour dog is a Samoyed!") # Dog has a fluffy coat and is a big dog
        else:
            earsStickUp = True if input("Do the dog's ears stick up? ") == "yes" else False # Ask the user if the dogs ears stick up
            if earsStickUp:
                print("\nYour dog is a German Shepherd!") # Dog is a big dog, does not have a fluffy coat, and does have ears that stick up
            else:
                print("\nYour dog is a Borzoi!") # Dog is a big dog, does not have a fluffy coat, and does not have ears that stick up
    else:
        curlyTail = True if input("Does the dog have a curly tail? ") == "yes" else False # Ask the user if the dog has a curly tail
        if curlyTail:
            print("\nYour dog is a Shiba Inu!") # Dog is not a big dog and has a curly tail
        else:
            print("\nYour dog is a Corgi!") # Dog is not a big dog and does not have a curly tail

main()