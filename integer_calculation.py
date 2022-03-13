#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: February 2022
# This program calculates the total of two numbers/integers
#   With user input


def main():
    # this function calculates the numbers

    integer1 = int(input("Enter the first number to add (integer): "))
    integer2 = int(input("Enter the second number to add (integer): "))

    # process
    calculation = integer1 + integer2

    # output
    print("")
    print("{} + {} = {}".format(integer1, integer2, calculation))

    print("\nDone")


if __name__ == "__main__":
    main()
