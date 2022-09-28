#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Sept 2022
# This program calculates the circumference of a circle

import constants


def main():
    # This function calculates the circumference of a circle

    # input
    radius_of_circle = int(input("Enter the radius of the circle (mm): "))

    # process
    circumference_of_circle = constants.TAU * radius_of_circle

    # output
    print("")
    print("The circumference is {0} mm.".format(circumference_of_circle))

    print("\nDone.")


if __name__ == "__main__":
    main()
