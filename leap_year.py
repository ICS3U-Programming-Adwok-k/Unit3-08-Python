#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: April 6th, 2025
# This program asks the user for a year in integers and
# checks whether the year is a leap year or not.


def main():
    # We ask the user for the year in string.
    year_as_string = input("Please enter the year: ")

    try:
        # We change the year to an int
        year = int(year_as_string)

        # if year is <= 0 we ask for a positive number.
        if year <= 0:
            print("Please enter a positive number.")

        else:
            # When year % 4 and year % 100 and year % 400 == 0
            # The year is a leap year.
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print("This is a leap year.")

                        # All these else statements belong to the above if statements
                    else:
                        print("This is not a leap year")
                else:
                    print("This is a leap year.")
            else:
                print("This is not a leap year.")
    except:
        # if user submits an unknown input that input is valid.
        print("This is an invalid input.")

    finally:
        # We say this once everything is executed.
        print("Thank you and have a nice day!")


if __name__ == "__main__":
    main()
