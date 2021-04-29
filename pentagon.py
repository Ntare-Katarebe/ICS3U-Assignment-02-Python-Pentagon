#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: April 2021
# This program calculates the perimeter of a pentagon
#    with sides inputted from the user

import math


def main():
    # this function calculates the perimeter of a pentagon
    print("We will be calculating the perimeter of a pentagon")
    # input
    side = int(input("Enter the side length (mm): "))
    # process
    perimeter = 5 * side
    # output
    print("Perimeter is {} mm".format(perimeter))


if __name__ == "__main__":
    main()
